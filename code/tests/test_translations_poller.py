import os
from pathlib import Path
import importlib

JOBS = int(os.environ.get("TRANSLATE_JOBS", os.cpu_count() or 1))

def _write_po(path: Path, entries: dict[str, str]):
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = []
    for k, v in entries.items():
        lines.append(f'msgid "{k}"\nmsgstr "{v}"\n')
    path.write_text("\n".join(lines), encoding="utf-8")

def test_translations_rebuild_on_file_change(tmp_path, monkeypatch):
    # arrange
    src_dir = tmp_path / "translations"        # acts like TRANSLATIONS_SRC_DIR
    build_dir = tmp_path / "compiled"          # acts like TRANSLATIONS_BUILD_DIR
    po_hash_path = build_dir / "po_hash_map.json"

    monkeypatch.setenv("TRANSLATIONS_SRC_DIR", src_dir.as_posix())
    monkeypatch.setenv("TRANSLATIONS_BUILD_DIR", build_dir.as_posix())
    monkeypatch.setenv("PO_HASH_PATH", po_hash_path.as_posix())
    monkeypatch.setenv("LANG_MAP_TTL", "1")

    # Fresh import so module reads env
    if "translate" in importlib.sys.modules:
        del importlib.sys.modules["translate"]
    import translate

    # v1: create initial Dutch .po
    po_file = src_dir / "nl-NL" / "IfcWall_(Dutch).po"
    _write_po(po_file, {
        "IfcWall": "Wand",
        "IfcWall_DESCRIPTION": "Beschrijving",
    })

    # First build (clean + hash) → should compile v1
    rc = translate.build_cache(clean=True, use_hash=True, jobs=JOBS, pool="process")
    assert "Dutch" in translate.list_languages()
    out_v1 = translate.translate_resource("Dutch", "IfcWall")
    assert out_v1["resource_translation"] == "Wand"
    assert out_v1["DESCRIPTION"] == "Beschrijving"

    # v2: modify the same .po (simulate “branch update” without git)
    _write_po(po_file, {
        "IfcWall": "MUUR",  # CHANGED
        "IfcWall_DESCRIPTION": "Bijgewerkte beschrijving",  # CHANGED
        "IfcWall_DEFINITION": "Definitie",  # NEW
    })

    # Rebuild (mtime mode is fine; or set use_hash=True if you prefer)
    rc2 = translate.build_cache(jobs=JOBS, pool="process")
    assert rc2 == 0

    # Clear in-proc caches so we don’t wait for TTL
    translate.clear_translation_caches()

    # Verify v2 is visible
    out_v2 = translate.translate_resource("Dutch", "IfcWall")
    assert out_v2["resource_translation"] == "MUUR"
    assert out_v2["DESCRIPTION"] == "Bijgewerkte beschrijving"
    assert out_v2["DEFINITION"] == "Definitie"
