"""Structure-aware merge support for the repository's UML/XMI files.

The module has two entry points:

* ``driver`` implements Git's custom merge-driver protocol for one UML file.
* ``merge`` runs ``git merge --no-commit`` with the driver enabled and then
  validates every UML file plus the EXPRESS generator.

The merge algorithm is intentionally conservative. It recursively combines
complete XML elements, keyed primarily by ``xmi:id``, while preserving their
original byte representation. Ambiguous edits are left unresolved for a human.
"""

from __future__ import annotations

import argparse
import heapq
import os
import re
import shlex
import subprocess
import sys
import tempfile
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Sequence
from xml.parsers import expat

XMI_ID = "xmi:id"


class MergeConflict(RuntimeError):
    """Raised when a structural merge cannot be proven safe."""


@dataclass
class SourceNode:
    name: str
    attrs: dict[str, str]
    start: int
    start_tag_end: int
    self_closing: bool
    parent: SourceNode | None = None
    end_tag_start: int | None = None
    end: int | None = None
    children: list[SourceNode] = field(default_factory=list)
    content: list[str | SourceNode] = field(default_factory=list)

    @property
    def xmi_id(self) -> str | None:
        return self.attrs.get(XMI_ID)


@dataclass(frozen=True)
class _ConflictBlock:
    current: tuple[bytes, ...]
    other: tuple[bytes, ...]


@dataclass(frozen=True)
class _DiffOperation:
    side: str
    start: int
    end: int
    old: tuple[bytes, ...]
    new: tuple[bytes, ...]


class SourceDocument:
    """Parsed XML plus source byte ranges for every element."""

    def __init__(self, path: Path):
        self.path = path
        self.data = path.read_bytes()
        self.root: SourceNode | None = None
        self.nodes_by_id: dict[str, SourceNode] = {}
        self.duplicate_ids: list[str] = []
        self._stack: list[SourceNode] = []
        self._parser = expat.ParserCreate()
        self._parser.StartElementHandler = self._start_element
        self._parser.EndElementHandler = self._end_element
        self._parser.CharacterDataHandler = self._character_data
        self._parser.CommentHandler = self._comment
        try:
            self._parser.Parse(self.data, True)
        except expat.ExpatError as exc:
            raise MergeConflict(f"{path}: invalid XML: {exc}") from exc
        if self.root is None:
            raise MergeConflict(f"{path}: no XML root element")

    def raw(self, node: SourceNode) -> bytes:
        if node.end is None:
            raise MergeConflict(f"{self.path}: incomplete element {node.name}")
        return self.data[node.start : node.end]

    def prefix(self) -> bytes:
        assert self.root is not None
        return self.data[: self.root.start]

    def suffix(self) -> bytes:
        assert self.root is not None and self.root.end is not None
        return self.data[self.root.end :]

    def fingerprint(self, node: SourceNode) -> tuple:
        content: list[tuple[str, object]] = []
        for item in node.content:
            if isinstance(item, SourceNode):
                content.append(("child", self.fingerprint(item)))
            else:
                content.append(("text", item))
        return node.name, tuple(sorted(node.attrs.items())), tuple(content)

    def _start_element(self, name: str, attrs: dict[str, str]) -> None:
        start = self._parser.CurrentByteIndex
        start_tag_end = _scan_tag_end(self.data, start)
        tag_body = self.data[start:start_tag_end].rstrip()
        self_closing = tag_body.endswith(b"/>")
        parent = self._stack[-1] if self._stack else None
        node = SourceNode(
            name=name,
            attrs=dict(attrs),
            start=start,
            start_tag_end=start_tag_end,
            self_closing=self_closing,
            parent=parent,
        )
        if parent is not None:
            parent.children.append(node)
            parent.content.append(node)
        elif self.root is None:
            self.root = node
        else:
            raise MergeConflict(f"{self.path}: multiple XML root elements")
        if node.xmi_id:
            if node.xmi_id in self.nodes_by_id:
                self.duplicate_ids.append(node.xmi_id)
            else:
                self.nodes_by_id[node.xmi_id] = node
        self._stack.append(node)

    def _end_element(self, _name: str) -> None:
        node = self._stack.pop()
        if node.self_closing:
            node.end_tag_start = node.start_tag_end
            node.end = node.start_tag_end
            return
        end_tag_start = self._parser.CurrentByteIndex
        node.end_tag_start = end_tag_start
        node.end = _scan_tag_end(self.data, end_tag_start)

    def _character_data(self, data: str) -> None:
        if self._stack and data:
            self._stack[-1].content.append(data)

    def _comment(self, data: str) -> None:
        if self._stack:
            self._stack[-1].content.append(f"<!--{data}-->")


def _scan_tag_end(data: bytes, start: int) -> int:
    quote: int | None = None
    index = start
    while index < len(data):
        value = data[index]
        if quote is not None:
            if value == quote:
                quote = None
        elif value in (ord('"'), ord("'")):
            quote = value
        elif value == ord(">"):
            return index + 1
        index += 1
    raise MergeConflict("unterminated XML tag")


def _node_keys(node: SourceNode) -> list[str]:
    counts: Counter[str] = Counter()
    keys: list[str] = []
    for child in node.children:
        if child.xmi_id:
            keys.append(f"id:{child.xmi_id}")
            continue
        counts[child.name] += 1
        keys.append(f"anon:{child.name}:{counts[child.name]}")
    return keys


def _child_map(node: SourceNode) -> tuple[list[str], dict[str, SourceNode]]:
    keys = _node_keys(node)
    mapping = dict(zip(keys, node.children))
    if len(mapping) != len(keys):
        raise MergeConflict(f"duplicate direct-child identity below {node.xmi_id or node.name}")
    return keys, mapping


def _meaningful_direct_text(node: SourceNode) -> tuple[str, ...]:
    return tuple(
        item
        for item in node.content
        if isinstance(item, str) and item.strip()
    )


def _merge_scalar(base: object, current: object, other: object, label: str) -> object:
    if current == other:
        return current
    if current == base:
        return other
    if other == base:
        return current
    raise MergeConflict(f"both sides changed {label}")


def _merge_attributes(
    base: SourceNode, current: SourceNode, other: SourceNode
) -> tuple[dict[str, str], str]:
    result: dict[str, str] = {}
    for key in sorted(set(base.attrs) | set(current.attrs) | set(other.attrs)):
        missing = object()
        value = _merge_scalar(
            base.attrs.get(key, missing),
            current.attrs.get(key, missing),
            other.attrs.get(key, missing),
            f"attribute {key!r} on {current.xmi_id or current.name}",
        )
        if value is not missing:
            result[key] = value  # type: ignore[assignment]
    if result == current.attrs:
        return result, "current"
    if result == other.attrs:
        return result, "other"
    raise MergeConflict(
        f"disjoint attribute edits require manual merge on {current.xmi_id or current.name}"
    )


def _merge_order(
    included: set[str],
    base_order: Sequence[str],
    current_order: Sequence[str],
    other_order: Sequence[str],
) -> list[str]:
    edges: dict[str, set[str]] = {key: set() for key in included}
    indegree = {key: 0 for key in included}
    for order in (base_order, current_order, other_order):
        filtered = [key for key in order if key in included]
        for left, right in zip(filtered, filtered[1:]):
            if right not in edges[left]:
                edges[left].add(right)
                indegree[right] += 1

    positions: dict[str, tuple[int, int, int, str]] = {}
    large = len(included) + 1
    for key in included:
        positions[key] = (
            current_order.index(key) if key in current_order else large,
            other_order.index(key) if key in other_order else large,
            base_order.index(key) if key in base_order else large,
            key,
        )

    ready = [(positions[key], key) for key, degree in indegree.items() if degree == 0]
    heapq.heapify(ready)
    result: list[str] = []
    while ready:
        _, key = heapq.heappop(ready)
        result.append(key)
        for successor in edges[key]:
            indegree[successor] -= 1
            if indegree[successor] == 0:
                heapq.heappush(ready, (positions[successor], successor))
    if len(result) != len(included):
        raise MergeConflict("the branches impose incompatible XML element ordering")
    return result


def _format_parts(document: SourceDocument, node: SourceNode) -> tuple[bytes, bytes, bytes]:
    if node.self_closing or node.end_tag_start is None:
        raise MergeConflict(f"cannot add children to self-closing element {node.xmi_id or node.name}")
    if node.children:
        prefix = document.data[node.start_tag_end : node.children[0].start]
        separators = [
            document.data[left.end : right.start]
            for left, right in zip(node.children, node.children[1:])
            if left.end is not None
        ]
        suffix = document.data[node.children[-1].end : node.end_tag_start]
        separator = separators[0] if separators else prefix
        gaps = [prefix, *separators, suffix]
        if any(gap.strip() for gap in gaps):
            raise MergeConflict(
                f"non-whitespace content between children of {node.xmi_id or node.name}"
            )
        return prefix, separator, suffix
    gap = document.data[node.start_tag_end : node.end_tag_start]
    if gap.strip():
        raise MergeConflict(f"mixed XML content in {node.xmi_id or node.name}")
    newline = b"\r\n" if b"\r\n" in document.data else b"\n"
    line_start = document.data.rfind(newline, 0, node.start)
    parent_indent = document.data[line_start + len(newline) : node.start]
    child_indent = parent_indent + b"  "
    return newline + child_indent, newline + child_indent, newline + parent_indent


def _merge_node(
    base_doc: SourceDocument,
    base: SourceNode,
    current_doc: SourceDocument,
    current: SourceNode,
    other_doc: SourceDocument,
    other: SourceNode,
) -> bytes:
    base_fp = base_doc.fingerprint(base)
    current_fp = current_doc.fingerprint(current)
    other_fp = other_doc.fingerprint(other)
    if current_fp == other_fp:
        return current_doc.raw(current)
    if current_fp == base_fp:
        return other_doc.raw(other)
    if other_fp == base_fp:
        return current_doc.raw(current)
    if not (base.name == current.name == other.name):
        raise MergeConflict(f"element type changed for {current.xmi_id or current.name}")
    if not current.children and not other.children:
        raise MergeConflict(f"both sides changed leaf element {current.xmi_id or current.name}")

    _, scaffold_name = _merge_attributes(base, current, other)
    direct_text = _merge_scalar(
        _meaningful_direct_text(base),
        _meaningful_direct_text(current),
        _meaningful_direct_text(other),
        f"text content on {current.xmi_id or current.name}",
    )
    if direct_text:
        raise MergeConflict(
            f"cannot combine child edits with text edits on {current.xmi_id or current.name}"
        )

    base_order, base_children = _child_map(base)
    current_order, current_children = _child_map(current)
    other_order, other_children = _child_map(other)
    merged_children: dict[str, bytes] = {}
    all_keys = set(base_children) | set(current_children) | set(other_children)

    for key in all_keys:
        base_child = base_children.get(key)
        current_child = current_children.get(key)
        other_child = other_children.get(key)
        if base_child is None:
            if current_child is not None and other_child is not None:
                if current_doc.fingerprint(current_child) != other_doc.fingerprint(other_child):
                    raise MergeConflict(f"both sides added different elements with identity {key}")
                merged_children[key] = current_doc.raw(current_child)
            elif current_child is not None:
                merged_children[key] = current_doc.raw(current_child)
            elif other_child is not None:
                merged_children[key] = other_doc.raw(other_child)
            continue

        if current_child is None and other_child is None:
            continue
        if current_child is None:
            if other_doc.fingerprint(other_child) == base_doc.fingerprint(base_child):
                continue
            raise MergeConflict(f"delete/modify conflict for {key}")
        if other_child is None:
            if current_doc.fingerprint(current_child) == base_doc.fingerprint(base_child):
                continue
            raise MergeConflict(f"modify/delete conflict for {key}")
        merged_children[key] = _merge_node(
            base_doc,
            base_child,
            current_doc,
            current_child,
            other_doc,
            other_child,
        )

    order = _merge_order(
        set(merged_children), base_order, current_order, other_order
    )
    scaffold_doc, scaffold = (
        (current_doc, current) if scaffold_name == "current" else (other_doc, other)
    )
    if not order:
        start_tag = scaffold_doc.data[scaffold.start : scaffold.start_tag_end]
        end_tag = scaffold_doc.data[scaffold.end_tag_start : scaffold.end]
        return start_tag + end_tag

    prefix, separator, suffix = _format_parts(scaffold_doc, scaffold)
    start_tag = scaffold_doc.data[scaffold.start : scaffold.start_tag_end]
    end_tag = scaffold_doc.data[scaffold.end_tag_start : scaffold.end]
    body = separator.join(merged_children[key] for key in order)
    return start_tag + prefix + body + suffix + end_tag


def merge_documents(base_path: Path, current_path: Path, other_path: Path) -> bytes:
    base_doc = SourceDocument(base_path)
    current_doc = SourceDocument(current_path)
    other_doc = SourceDocument(other_path)
    for document in (base_doc, current_doc, other_doc):
        if document.duplicate_ids:
            duplicates = ", ".join(sorted(set(document.duplicate_ids))[:10])
            raise MergeConflict(f"{document.path}: duplicate xmi:id values: {duplicates}")
    assert base_doc.root and current_doc.root and other_doc.root
    merged_root = _merge_node(
        base_doc,
        base_doc.root,
        current_doc,
        current_doc.root,
        other_doc,
        other_doc.root,
    )
    result = current_doc.prefix() + merged_root + current_doc.suffix()
    _validate_bytes(result, current_path)
    return result


def _validate_bytes(data: bytes, label: Path | str) -> None:
    with tempfile.NamedTemporaryFile(suffix=".uml", delete=False) as handle:
        handle.write(data)
        temp_path = Path(handle.name)
    try:
        document = SourceDocument(temp_path)
        if document.duplicate_ids:
            duplicates = ", ".join(sorted(set(document.duplicate_ids))[:10])
            raise MergeConflict(f"{label}: duplicate xmi:id values: {duplicates}")
    finally:
        temp_path.unlink(missing_ok=True)


def _fallback_text_merge(
    base_path: Path, current_path: Path, other_path: Path, display_path: str
) -> None:
    process = subprocess.run(
        [
            "git",
            "merge-file",
            "-L",
            f"current: {display_path}",
            "-L",
            f"base: {display_path}",
            "-L",
            f"other: {display_path}",
            str(current_path),
            str(base_path),
            str(other_path),
        ],
        check=False,
    )
    if process.returncode < 0:
        raise RuntimeError("git merge-file failed")


def has_conflict_markers(path: Path) -> bool:
    lines = path.read_bytes().splitlines()
    return (
        any(line.startswith(b"<<<<<<< ") for line in lines)
        and any(line.startswith(b"=======") for line in lines)
        and any(line.startswith(b">>>>>>> ") for line in lines)
    )


def _xml_well_formed_error(data: bytes, label: Path | str) -> str | None:
    parser = expat.ParserCreate()
    try:
        parser.Parse(data, True)
    except expat.ExpatError as exc:
        return f"{label}: invalid XML: {exc}"
    return None


def _render_conflict_marker_parts(
    parts: Sequence[bytes | _ConflictBlock],
) -> bytes:
    output: list[bytes] = []
    for part in parts:
        if not isinstance(part, _ConflictBlock):
            output.append(part)
            continue
        output.extend(part.current)
        output.extend(part.other)
    return b"".join(output)


_ZERO_CONTEXT_HEADER = re.compile(
    br"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@"
)


def _parse_zero_context_diff(data: bytes, side: str) -> list[_DiffOperation]:
    lines = data.splitlines(keepends=True)
    operations: list[_DiffOperation] = []
    index = 0
    while index < len(lines):
        match = _ZERO_CONTEXT_HEADER.match(lines[index])
        if match is None:
            index += 1
            continue

        old_start = int(match.group(1))
        old_count = int(match.group(2) or b"1")
        start = old_start if old_count == 0 else old_start - 1
        end = start + old_count
        old: list[bytes] = []
        new: list[bytes] = []
        index += 1
        while index < len(lines) and not lines[index].startswith(b"@@ "):
            line = lines[index]
            if line.startswith(b"\\ "):
                index += 1
                continue
            if line.startswith(b"-") and not line.startswith(b"---"):
                old.append(line[1:])
            elif line.startswith(b"+") and not line.startswith(b"+++"):
                new.append(line[1:])
            elif line.startswith(b" "):
                old.append(line[1:])
                new.append(line[1:])
            index += 1
        operations.append(
            _DiffOperation(side, start, end, tuple(old), tuple(new))
        )
    return operations


def _replay_zero_context_diffs(
    base: bytes,
    current_diff: bytes,
    other_diff: bytes,
    label: Path | str,
) -> bytes:
    base_lines = base.splitlines(keepends=True)
    operations = sorted(
        [
            *_parse_zero_context_diff(current_diff, "current"),
            *_parse_zero_context_diff(other_diff, "other"),
        ],
        key=lambda operation: (
            operation.start,
            operation.end,
            0 if operation.side == "current" else 1,
        ),
    )
    output: list[bytes] = []
    position = 0
    index = 0

    while index < len(operations):
        group = [operations[index]]
        index += 1
        while (
            index < len(operations)
            and operations[index].start == group[0].start
            and operations[index].end == group[0].end
        ):
            group.append(operations[index])
            index += 1

        start = group[0].start
        end = group[0].end
        if start < position:
            raise MergeConflict(
                f"{label}: overlapping zero-context patch hunks near base line {start + 1}"
            )
        expected_old = tuple(base_lines[start:end])
        for operation in group:
            if operation.old != expected_old:
                raise MergeConflict(
                    f"{label}: zero-context patch does not match base near line {start + 1}"
                )

        replacements: list[tuple[bytes, ...]] = []
        for operation in group:
            if operation.new not in replacements:
                replacements.append(operation.new)
        if len(replacements) > 1 and start != end:
            raise MergeConflict(
                f"{label}: both sides changed base lines {start + 1}-{end}"
            )

        output.extend(base_lines[position:start])
        for replacement in replacements:
            output.extend(replacement)
        position = end

    output.extend(base_lines[position:])
    return b"".join(output)


def _git_stage_bytes(repo_root: Path, relative_path: str, stage: int) -> bytes | None:
    process = subprocess.run(
        ["git", "show", f":{stage}:{relative_path}"],
        cwd=repo_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if process.returncode:
        return None
    return process.stdout


def _git_zero_context_diff(
    repo_root: Path, relative_path: str, stage: int
) -> bytes:
    process = subprocess.run(
        [
            "git",
            "diff",
            "--unified=0",
            "--no-ext-diff",
            "--no-color",
            f":1:{relative_path}",
            f":{stage}:{relative_path}",
        ],
        cwd=repo_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if process.returncode:
        message = process.stderr.decode("utf-8", "replace").strip()
        raise MergeConflict(
            f"{relative_path}: cannot diff Git stage 1 against stage {stage}: "
            f"{message or process.returncode}"
        )
    return process.stdout


def resolve_unmerged_file_by_zero_context_patches(
    repo_root: Path, relative_path: str
) -> bool:
    """Resolve an unmerged file by replaying stage 1->2 and 1->3 diffs on stage 1."""

    base = _git_stage_bytes(repo_root, relative_path, 1)
    if base is None:
        return False
    for stage in (2, 3):
        if _git_stage_bytes(repo_root, relative_path, stage) is None:
            return False

    result = _replay_zero_context_diffs(
        base,
        _git_zero_context_diff(repo_root, relative_path, 2),
        _git_zero_context_diff(repo_root, relative_path, 3),
        relative_path,
    )
    if Path(relative_path).suffix.lower() == ".uml":
        error = _xml_well_formed_error(result, relative_path)
        if error:
            raise MergeConflict(error)

    (repo_root / relative_path).write_bytes(result)
    print(
        f"xmi-merge: {relative_path}: resolved by replaying zero-context "
        "stage diffs",
        file=sys.stderr,
    )
    return True


def _document_from_bytes(data: bytes) -> SourceDocument:
    with tempfile.NamedTemporaryFile(suffix=".uml", delete=False) as handle:
        handle.write(data)
        temp_path = Path(handle.name)
    try:
        return SourceDocument(temp_path)
    finally:
        temp_path.unlink(missing_ok=True)


def _single_package_child(document: SourceDocument, label: Path | str) -> SourceNode:
    assert document.root is not None
    if len(document.root.children) != 1:
        raise MergeConflict(f"{label}: add/add UML merge expects one root package")
    package = document.root.children[0]
    if package.name != "packagedElement" or not package.xmi_id:
        raise MergeConflict(f"{label}: add/add UML merge expects one named root package")
    return package


def _merge_added_documents(current: bytes, other: bytes, label: Path | str) -> bytes:
    current_doc = _document_from_bytes(current)
    other_doc = _document_from_bytes(other)
    assert current_doc.root is not None and other_doc.root is not None
    if (
        current_doc.root.name != other_doc.root.name
        or current_doc.root.attrs != other_doc.root.attrs
    ):
        raise MergeConflict(f"{label}: add/add UML roots differ")

    current_package = _single_package_child(current_doc, label)
    other_package = _single_package_child(other_doc, label)
    if (
        current_package.name != other_package.name
        or current_package.attrs != other_package.attrs
    ):
        raise MergeConflict(f"{label}: add/add UML root packages differ")

    current_order, current_children = _child_map(current_package)
    other_order, other_children = _child_map(other_package)
    merged_children: dict[str, bytes] = {}
    for key in current_order:
        merged_children[key] = current_doc.raw(current_children[key])
    for key in other_order:
        other_child = other_children[key]
        current_child = current_children.get(key)
        if current_child is not None:
            if current_doc.fingerprint(current_child) != other_doc.fingerprint(other_child):
                raise MergeConflict(f"{label}: both added different elements with {key}")
            continue
        merged_children[key] = other_doc.raw(other_child)

    order = current_order + [key for key in other_order if key not in current_children]
    prefix, separator, suffix = _format_parts(current_doc, current_package)
    package_start = current_doc.data[
        current_package.start : current_package.start_tag_end
    ]
    package_end = current_doc.data[
        current_package.end_tag_start : current_package.end
    ]
    package_body = separator.join(merged_children[key] for key in order)
    merged_package = package_start + prefix + package_body + suffix + package_end

    root = current_doc.root
    root_start = current_doc.data[root.start : root.start_tag_end]
    root_end = current_doc.data[root.end_tag_start : root.end]
    before_package = current_doc.data[root.start_tag_end : current_package.start]
    after_package = current_doc.data[current_package.end : root.end_tag_start]
    result = (
        current_doc.prefix()
        + root_start
        + before_package
        + merged_package
        + after_package
        + root_end
        + current_doc.suffix()
    )
    _validate_bytes(result, label)
    return result


def resolve_added_file_by_structural_merge(
    repo_root: Path, relative_path: str
) -> bool:
    """Resolve an add/add UML conflict by combining children of the root package."""

    if _git_stage_bytes(repo_root, relative_path, 1) is not None:
        return False
    current = _git_stage_bytes(repo_root, relative_path, 2)
    other = _git_stage_bytes(repo_root, relative_path, 3)
    if current is None or other is None:
        return False

    result = _merge_added_documents(current, other, relative_path)
    (repo_root / relative_path).write_bytes(result)
    print(
        f"xmi-merge: {relative_path}: resolved add/add UML by combining "
        "root package children",
        file=sys.stderr,
    )
    return True


def resolve_conflict_markers_keep_both(path: Path) -> bool:
    """Remove Git conflict markers by retaining current lines followed by other lines."""

    lines = path.read_bytes().splitlines(keepends=True)
    parts: list[bytes | _ConflictBlock] = []
    changed = False
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.startswith(b"<<<<<<< "):
            parts.append(line)
            index += 1
            continue

        changed = True
        index += 1
        current: list[bytes] = []
        while index < len(lines) and not (
            lines[index].startswith(b"||||||| ") or lines[index].startswith(b"=======")
        ):
            current.append(lines[index])
            index += 1
        if index >= len(lines):
            raise MergeConflict(f"{path}: unterminated conflict marker")

        if lines[index].startswith(b"||||||| "):
            index += 1
            while index < len(lines) and not lines[index].startswith(b"======="):
                index += 1
            if index >= len(lines):
                raise MergeConflict(f"{path}: unterminated diff3 conflict marker")

        index += 1
        other: list[bytes] = []
        while index < len(lines) and not lines[index].startswith(b">>>>>>> "):
            other.append(lines[index])
            index += 1
        if index >= len(lines):
            raise MergeConflict(f"{path}: unterminated conflict marker")

        index += 1
        parts.append(_ConflictBlock(tuple(current), tuple(other)))

    if changed:
        path.write_bytes(_render_conflict_marker_parts(parts))
    return changed


def remove_duplicate_xmi_id_elements(path: Path) -> int:
    """Remove later duplicate ``xmi:id`` elements when the duplicate is safe to drop."""

    document = SourceDocument(path)
    assert document.root is not None
    seen: dict[str, SourceNode] = {}
    ranges: list[tuple[int, int]] = []

    def visit(node: SourceNode) -> None:
        if node.xmi_id:
            first = seen.get(node.xmi_id)
            if first is not None:
                if node.end is None or first.end is None:
                    raise MergeConflict(f"{path}: incomplete duplicate {node.xmi_id}")
                if node.name != "packagedElement" and document.raw(node) != document.raw(first):
                    raise MergeConflict(
                        f"{path}: duplicate xmi:id {node.xmi_id} on "
                        f"non-identical {node.name} elements"
                    )
                ranges.append((node.start, node.end))
                return
            seen[node.xmi_id] = node
        for child in node.children:
            visit(child)

    visit(document.root)
    if not ranges:
        return 0

    data = document.data
    for start, end in sorted(ranges, reverse=True):
        data = data[:start] + data[end:]
    _validate_bytes(data, path)
    path.write_bytes(data)
    return len(ranges)


def remove_duplicate_packaged_elements(path: Path) -> int:
    """Compatibility wrapper for the broader duplicate ``xmi:id`` culling."""

    return remove_duplicate_xmi_id_elements(path)


def driver(base: Path, current: Path, other: Path, display_path: str) -> int:
    try:
        result = merge_documents(base, current, other)
    except MergeConflict as exc:
        print(f"xmi-merge: {display_path}: {exc}", file=sys.stderr)
        _fallback_text_merge(base, current, other, display_path)
        return 1
    current.write_bytes(result)
    print(f"xmi-merge: structurally merged {display_path}", file=sys.stderr)
    return 0


def validate_uml_files(repo_root: Path) -> list[str]:
    errors: list[str] = []
    for path in sorted((repo_root / "schemas").glob("*.uml")):
        try:
            document = SourceDocument(path)
        except MergeConflict as exc:
            errors.append(str(exc))
            continue
        if document.duplicate_ids:
            duplicates = ", ".join(sorted(set(document.duplicate_ids))[:10])
            errors.append(f"{path}: duplicate xmi:id values: {duplicates}")
    return errors


def run_generator(repo_root: Path) -> tuple[int, str]:
    with tempfile.TemporaryDirectory(prefix="ifc-xmi-merge-") as temp_dir:
        output_path = Path(temp_dir) / "IFC.exp"
        process = subprocess.run(
            [
                sys.executable,
                "-m",
                "generators.express",
                "../schemas/ifc4x3_add2.uml",
                "--output",
                str(output_path),
            ],
            cwd=repo_root / "code",
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
    return process.returncode, process.stdout


def _repo_root() -> Path:
    process = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if process.returncode:
        raise RuntimeError(process.stderr.strip() or "not inside a Git repository")
    return Path(process.stdout.strip()).resolve()


def _driver_command(script_path: Path) -> str:
    return " ".join(
        [
            shlex.quote(str(Path(sys.executable).resolve())),
            shlex.quote(str(script_path.resolve())),
            "driver",
            '"%O"',
            '"%A"',
            '"%B"',
            '"%P"',
        ]
    )


def install_driver(repo_root: Path, script_path: Path) -> None:
    command = _driver_command(script_path)
    subprocess.run(
        ["git", "config", "merge.ifc-xmi.name", "IFC UML structural merge"],
        cwd=repo_root,
        check=True,
    )
    subprocess.run(
        ["git", "config", "merge.ifc-xmi.driver", command],
        cwd=repo_root,
        check=True,
    )
    print("Installed local Git merge driver 'ifc-xmi'.")


def merge_command(target: str, extra_args: Sequence[str]) -> int:
    repo_root = _repo_root()
    script_path = Path(__file__).resolve()
    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=repo_root,
        text=True,
        stdout=subprocess.PIPE,
        check=True,
    ).stdout
    if status.strip():
        print("xmi-merge: working tree must be clean before starting a merge", file=sys.stderr)
        return 2

    env = os.environ.copy()
    env.update(
        {
            "GIT_CONFIG_COUNT": "2",
            "GIT_CONFIG_KEY_0": "merge.ifc-xmi.name",
            "GIT_CONFIG_VALUE_0": "IFC UML structural merge",
            "GIT_CONFIG_KEY_1": "merge.ifc-xmi.driver",
            "GIT_CONFIG_VALUE_1": _driver_command(script_path),
        }
    )
    process = subprocess.run(
        ["git", "merge", "--no-commit", "--no-ff", *extra_args, target],
        cwd=repo_root,
        env=env,
        check=False,
    )
    unmerged = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=U"],
        cwd=repo_root,
        text=True,
        stdout=subprocess.PIPE,
        check=True,
    ).stdout.splitlines()
    if process.returncode or unmerged:
        print("xmi-merge: merge requires user resolution.", file=sys.stderr)
        for path in unmerged:
            print(f"  unresolved: {path}", file=sys.stderr)
        print("Resolve the files and rerun `python code/tools/xmi_merge.py validate`.", file=sys.stderr)
        return 1
    return validate_command(repo_root)


def validate_command(repo_root: Path | None = None) -> int:
    repo_root = repo_root or _repo_root()
    errors = validate_uml_files(repo_root)
    if errors:
        print("xmi-merge: UML validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        print(
            "The worktree is left for manual repair; use `git merge --abort` to discard the merge.",
            file=sys.stderr,
        )
        return 1
    generator_status, generator_output = run_generator(repo_root)
    if generator_status:
        print("xmi-merge: EXPRESS generation failed:", file=sys.stderr)
        print(generator_output.rstrip(), file=sys.stderr)
        print(
            "The worktree is left for manual repair; use `git merge --abort` to discard the merge.",
            file=sys.stderr,
        )
        return 1
    print("xmi-merge: all UML files parse, xmi:id values are unique, and EXPRESS generation succeeds.")
    merge_head = subprocess.run(
        ["git", "rev-parse", "-q", "--verify", "MERGE_HEAD"],
        cwd=repo_root,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if merge_head.returncode == 0:
        print("The merge remains uncommitted for review.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    driver_parser = subparsers.add_parser("driver", help="Run as a Git merge driver")
    driver_parser.add_argument("base", type=Path)
    driver_parser.add_argument("current", type=Path)
    driver_parser.add_argument("other", type=Path)
    driver_parser.add_argument("path", nargs="?", default="<unknown>")

    merge_parser = subparsers.add_parser(
        "merge", help="Merge a ref and validate the uncommitted result"
    )
    merge_parser.add_argument("target")
    merge_parser.add_argument(
        "git_args",
        nargs=argparse.REMAINDER,
        help="Additional arguments passed before the merge target",
    )

    subparsers.add_parser("validate", help="Validate the current worktree")
    subparsers.add_parser("install", help="Install the driver in local Git config")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "driver":
        return driver(args.base, args.current, args.other, args.path)
    if args.command == "merge":
        return merge_command(args.target, args.git_args)
    if args.command == "validate":
        return validate_command()
    if args.command == "install":
        repo_root = _repo_root()
        install_driver(repo_root, Path(__file__))
        return 0
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
