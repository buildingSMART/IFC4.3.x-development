from pathlib import Path

import pytest

from tools import xmi_merge
from tools.xmi_merge import MergeConflict, SourceDocument, merge_documents


HEADER = '<?xml version="1.0" encoding="UTF-8"?>\n'
MODEL_OPEN = (
    '<uml:Model xmlns:xmi="http://www.omg.org/spec/XMI/20131001" '
    'xmlns:uml="http://www.eclipse.org/uml2/5.0.0/UML" '
    'xmi:id="model" name="model">\n'
    '  <packagedElement xmi:type="uml:Package" xmi:id="package" name="package">\n'
)
MODEL_CLOSE = "  </packagedElement>\n</uml:Model>\n"


def document(*elements: str) -> str:
    body = "".join(f"    {element}\n" for element in elements)
    return HEADER + MODEL_OPEN + body + MODEL_CLOSE


def node(identifier: str, name: str | None = None) -> str:
    return (
        f'<packagedElement xmi:type="uml:Class" xmi:id="{identifier}" '
        f'name="{name or identifier}"/>'
    )


def write_versions(tmp_path: Path, base: str, current: str, other: str):
    paths = [tmp_path / name for name in ("base.uml", "current.uml", "other.uml")]
    for path, content in zip(paths, (base, current, other)):
        path.write_text(content, encoding="utf-8")
    return paths


def ids(path: Path) -> list[str]:
    parsed = SourceDocument(path)
    return list(parsed.nodes_by_id)


def test_merges_complete_additions_at_same_location(tmp_path):
    base, current, other = write_versions(
        tmp_path,
        document(),
        document(node("a")),
        document(node("b")),
    )
    result = merge_documents(base, current, other)
    merged = tmp_path / "merged.uml"
    merged.write_bytes(result)

    assert ids(merged) == ["model", "package", "a", "b"]
    assert b'id="a"' in result
    assert b'id="b"' in result


def test_merges_nested_additions_without_sharing_closing_tags(tmp_path):
    base, current, other = write_versions(
        tmp_path,
        document(),
        document(
            '<packagedElement xmi:type="uml:Class" xmi:id="a" name="a">\n'
            '      <generalization xmi:type="uml:Generalization" xmi:id="a_gen"/>\n'
            "    </packagedElement>"
        ),
        document(
            '<packagedElement xmi:type="uml:Class" xmi:id="b" name="b">\n'
            '      <generalization xmi:type="uml:Generalization" xmi:id="b_gen"/>\n'
            "    </packagedElement>"
        ),
    )
    result = merge_documents(base, current, other)
    merged = tmp_path / "merged.uml"
    merged.write_bytes(result)

    SourceDocument(merged)
    assert b'id="a_gen"' in result
    assert b'id="b_gen"' in result


def test_takes_one_sided_edit_and_other_side_addition(tmp_path):
    base, current, other = write_versions(
        tmp_path,
        document(node("existing", "old")),
        document(node("existing", "changed")),
        document(node("existing", "old"), node("added")),
    )
    result = merge_documents(base, current, other)

    assert b'name="changed"' in result
    assert b'id="added"' in result


def test_defers_when_both_sides_add_different_nodes_with_same_id(tmp_path):
    base, current, other = write_versions(
        tmp_path,
        document(),
        document(node("duplicate", "current")),
        document(node("duplicate", "other")),
    )

    with pytest.raises(MergeConflict, match="both sides added different"):
        merge_documents(base, current, other)


def test_defers_when_input_contains_duplicate_ids(tmp_path):
    base, current, other = write_versions(
        tmp_path,
        document(),
        document(node("duplicate"), node("duplicate")),
        document(),
    )

    with pytest.raises(MergeConflict, match="duplicate xmi:id"):
        merge_documents(base, current, other)


def test_defers_on_two_sided_leaf_edit(tmp_path):
    base, current, other = write_versions(
        tmp_path,
        document(node("existing", "base")),
        document(node("existing", "current")),
        document(node("existing", "other")),
    )

    with pytest.raises(MergeConflict, match="both sides changed"):
        merge_documents(base, current, other)


def test_resolves_conflict_markers_by_keeping_both_sides(tmp_path):
    path = tmp_path / "conflicted.uml"
    path.write_text(
        "before\n"
        "<<<<<<< current\n"
        "current\n"
        "||||||| base\n"
        "base\n"
        "=======\n"
        "other\n"
        ">>>>>>> other\n"
        "after\n",
        encoding="utf-8",
    )

    assert xmi_merge.has_conflict_markers(path)
    assert xmi_merge.resolve_conflict_markers_keep_both(path)
    assert path.read_text(encoding="utf-8") == "before\ncurrent\nother\nafter\n"


def test_replays_same_point_zero_context_insertions_in_base_coordinates(tmp_path):
    current_diff = (
        b"@@ -3,0 +4,1 @@\n"
        + b'+    <packagedElement xmi:type="uml:Class" xmi:id="current" name="current"/>\n'
    )
    other_diff = (
        b"@@ -3,0 +4,1 @@\n"
        + b'+    <packagedElement xmi:type="uml:Class" xmi:id="other" name="other"/>\n'
    )

    result = xmi_merge._replay_zero_context_diffs(
        document().encode("utf-8"), current_diff, other_diff, "test.uml"
    )
    path = tmp_path / "merged.uml"
    path.write_bytes(result)

    assert ids(path) == ["model", "package", "current", "other"]


def test_replay_zero_context_rejects_two_sided_replacement():
    current_diff = (
        b"@@ -4 +4 @@\n"
        + b'-    <packagedElement xmi:type="uml:Class" xmi:id="base" name="base"/>\n'
        + b'+    <packagedElement xmi:type="uml:Class" xmi:id="base" name="current"/>\n'
    )
    other_diff = (
        b"@@ -4 +4 @@\n"
        + b'-    <packagedElement xmi:type="uml:Class" xmi:id="base" name="base"/>\n'
        + b'+    <packagedElement xmi:type="uml:Class" xmi:id="base" name="other"/>\n'
    )

    with pytest.raises(MergeConflict, match="both sides changed"):
        xmi_merge._replay_zero_context_diffs(
            document(node("base")).encode("utf-8"),
            current_diff,
            other_diff,
            "test.uml",
        )


def test_merges_added_uml_documents_by_combining_package_children(tmp_path):
    result = xmi_merge._merge_added_documents(
        document(node("current")).encode("utf-8"),
        document(node("other")).encode("utf-8"),
        "added.uml",
    )
    path = tmp_path / "added.uml"
    path.write_bytes(result)

    assert ids(path) == ["model", "package", "current", "other"]


def test_removes_duplicate_packaged_elements_retaining_first(tmp_path):
    path = tmp_path / "duplicates.uml"
    path.write_text(
        document(
            node("duplicate", "first"),
            node("duplicate", "second"),
            node("unique"),
        ),
        encoding="utf-8",
    )

    assert xmi_merge.remove_duplicate_packaged_elements(path) == 1
    result = path.read_text(encoding="utf-8")
    assert 'name="first"' in result
    assert 'name="second"' not in result
    assert ids(path) == ["model", "package", "duplicate", "unique"]


def test_removes_identical_duplicate_package_import(tmp_path):
    path = tmp_path / "duplicates.uml"
    package_import = (
        '  <packageImport xmi:type="uml:PackageImport" xmi:id="ip_IfcTunnelDomain">\n'
        '    <importedPackage xmi:type="uml:Package" href="IfcTunnelDomain.uml#pk_IfcTunnelDomain"/>\n'
        "  </packageImport>\n"
    )
    path.write_text(
        HEADER
        + (
            '<uml:Model xmlns:xmi="http://www.omg.org/spec/XMI/20131001" '
            'xmlns:uml="http://www.eclipse.org/uml2/5.0.0/UML" '
            'xmi:id="model" name="model">\n'
        )
        + package_import
        + package_import
        + '  <packagedElement xmi:type="uml:Package" xmi:id="package" name="package"/>\n'
        + "</uml:Model>\n",
        encoding="utf-8",
    )

    assert xmi_merge.remove_duplicate_xmi_id_elements(path) == 1
    assert path.read_text(encoding="utf-8").count('xmi:id="ip_IfcTunnelDomain"') == 1
    assert ids(path) == ["model", "ip_IfcTunnelDomain", "package"]


def test_rejects_nonidentical_duplicate_non_packaged_element(tmp_path):
    path = tmp_path / "duplicates.uml"
    path.write_text(
        document(
            '<packagedElement xmi:type="uml:Enumeration" xmi:id="enum" name="Enum">\n'
            '      <ownedLiteral xmi:type="uml:EnumerationLiteral" xmi:id="literal" name="A"/>\n'
            '      <ownedLiteral xmi:type="uml:EnumerationLiteral" xmi:id="literal" name="B"/>\n'
            "    </packagedElement>"
        ),
        encoding="utf-8",
    )

    with pytest.raises(MergeConflict, match="non-identical ownedLiteral"):
        xmi_merge.remove_duplicate_xmi_id_elements(path)


def test_validate_defers_when_generator_fails(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(xmi_merge, "validate_uml_files", lambda _repo: [])
    monkeypatch.setattr(
        xmi_merge, "run_generator", lambda _repo: (1, "generator failed")
    )

    assert xmi_merge.validate_command(tmp_path) == 1
    assert "generator failed" in capsys.readouterr().err
