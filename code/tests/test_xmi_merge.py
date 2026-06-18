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


def test_validate_defers_when_generator_fails(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(xmi_merge, "validate_uml_files", lambda _repo: [])
    monkeypatch.setattr(
        xmi_merge, "run_generator", lambda _repo: (1, "generator failed")
    )

    assert xmi_merge.validate_command(tmp_path) == 1
    assert "generator failed" in capsys.readouterr().err
