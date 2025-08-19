import os
import gettext
import polib
import re
import sys
import shutil
import argparse
import json
import time
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed
from flask import request, has_request_context
from functools import lru_cache

TRANSLATIONS_SRC_DIR = os.environ.get(
    "TRANSLATIONS_SRC_DIR",
    os.path.join(os.path.dirname(__file__), "translate_repo", "translations")
)
TRANSLATIONS_BUILD_DIR = os.environ.get(
    "TRANSLATIONS_BUILD_DIR",
    os.path.join(os.path.dirname(__file__), "compiled_translations")
)

# for storing hashes in case new translations come in 
PO_HASH_PATH = os.environ.get(
    'PO_HASH_PATH',
    os.path.join(TRANSLATIONS_BUILD_DIR, 'po_hash_map.json')
)

@lru_cache(maxsize=1)
def build_language_file_map():
    """Build a mapping of languages to their translation directories.
     Returns:
     {
         'German' : ../translations_repository/translations/de-DE,
         'Dutch': ../translations_repository/translations/nl-NL,
         etc
     }
    Detects from filenames like: Domain_(Lang).po, 
    e.g. IfcSharedFacilitieselements_(Italian).po
    """
    language_file_map = {}

    for lang_dir in os.listdir(TRANSLATIONS_SRC_DIR):
        full_lang_dir = os.path.join(TRANSLATIONS_SRC_DIR, lang_dir)
        if os.path.isdir(full_lang_dir):
            for po_file in os.listdir(full_lang_dir):
                if po_file.endswith('.po'):
                    lang_name = po_file.split('_(')[-1].split(').po')[0]
                    language_file_map[lang_name] = full_lang_dir 
                    break
    return language_file_map

def find_po_files(base_dir):
    """Yield absolute paths to all .po files under base_dir (recursive)."""
    for root, _, files in os.walk(base_dir):
        for name in files:
            if name.lower().endswith(".po"):
                yield os.path.join(root, name)


def mo_output_path(po_path, translations, compiled_translations):
    """
    Mirror the translations directory structure for the compiled translations.
    Example:
      translations/translations/NL/IfcWall_(Dutch).po
      -> compiled_translations/translations/NL/IfcWall_(Dutch).mo
    """
    rel = os.path.relpath(po_path, translations)
    rel_mo = os.path.splitext(rel)[0] + ".mo"
    return os.path.join(compiled_translations, rel_mo)


def compile_po_to_mo(po_path, mo_path):
    """Compile .po to .mo using polib."""
    po = polib.pofile(po_path)
    os.makedirs(os.path.dirname(mo_path), exist_ok=True)
    po.save_as_mofile(mo_path)


def _sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()  
    
def build_cache(clean=False, use_hash=False, jobs=1):
    """
    Build/refresh compiled .mo files from .po sources under TRANSLATIONS_SRC_DIR, mirroring
    the directory structure into TRANSLATIONS_BUILD_DIR.

    Modes
    -----
    - First run (no manifest) or --clean: hash mode (robust),
    - Default (periodically checking for translations): mtime mode (fast).
    - --hash: force hash mode (robust)
    """
    start_time = time.time()
    
    try:
        with open(PO_HASH_PATH, "r", encoding="utf-8") as f:
            old_po_hash_map = json.load(f)
    except FileNotFoundError:
        old_po_hash_map = {}
        use_hash = True  # first run: force hash

    # --clean implies hash (incl manifest reset) + compiled translations directory
    if clean and os.path.isdir(TRANSLATIONS_BUILD_DIR):
        shutil.rmtree(TRANSLATIONS_BUILD_DIR)
    os.makedirs(TRANSLATIONS_BUILD_DIR, exist_ok=True)
    
    if not os.path.isdir(TRANSLATIONS_SRC_DIR):
        print(f"[ERROR] Translations dir not found: {TRANSLATIONS_SRC_DIR}", file=sys.stderr)
        return 2
    

    po_files = sorted(find_po_files(TRANSLATIONS_SRC_DIR))
    if not po_files:
        print(f"[WARN] No .po files found under: {TRANSLATIONS_SRC_DIR}")
        return 0

    # pruned : in the (unlikely?) case a .po file is deleted, the corresponding .mo must also be removed
    new_po_hash_map = {}
    compiled = skipped = pruned = errors = 0
    expected_mos = set()
    tasks = [] # lst[(po, mo)]
    
    for po in po_files:
        try:
            mo = mo_output_path(po, TRANSLATIONS_SRC_DIR, TRANSLATIONS_BUILD_DIR)
            expected_mos.add(os.path.normpath(mo))
            
            if use_hash:
                digest = _sha256(po)                
                rel = os.path.normpath(os.path.relpath(po, TRANSLATIONS_SRC_DIR))
                new_po_hash_map[rel] = digest
                should_compile = (old_po_hash_map.get(rel) != digest) or (not os.path.exists(mo))
            else:
                # mtime-based check (faster)
                should_compile = (not os.path.exists(mo)
                                  or os.path.getmtime(po) > os.path.getmtime(mo))
            
            if should_compile:
                tasks.append((po, mo))
            else:
                skipped += 1
                
        except Exception as e:
            errors += 1
            print(f"[ERR] {po}: {e}", file=sys.stderr)
    
    def _compile_one(po, mo):
        os.makedirs(os.path.dirname(mo), exist_ok=True)
        compile_po_to_mo(po, mo)
        return po, mo
    
    if jobs <= 1:
        for po, mo in tasks:
            try:
                _compile_one(po, mo)
                compiled += 1
                print(f"[OK] {po} -> {mo}")
            except Exception as e:
                errors += 1
                print(f"[ERR] {po}: {e}", file=sys.stderr)
    
    else:
        with ThreadPoolExecutor(max_workers=jobs) as ex:
            futs = {ex.submit(_compile_one, po, mo): (po, mo) for po, mo in tasks}
            for fut in as_completed(futs):
                po, mo = futs[fut]
                try:
                    fut.result()
                    compiled += 1
                    print(f"[OK] {po} -> {mo}")
                except Exception as e:
                    errors += 1
                    print(f"[ERR] {po}: {e}", file=sys.stderr)
    
    # remove .mo if outdated and write hash map
    if use_hash:
        for root, _, files in os.walk(TRANSLATIONS_BUILD_DIR):
            for name in files:
                if not name.lower().endswith(".mo"):
                    continue
                mo_path = os.path.normpath(os.path.join(root, name))
                if mo_path not in expected_mos:
                    try:
                        os.remove(mo_path)
                        pruned += 1
                        print(f"[PRUNED] {mo_path}")
                    except Exception as e:
                        errors += 1
                        print(f"[ERR] prune {mo_path}: {e}", file=sys.stderr)

        with open(PO_HASH_PATH, "w", encoding="utf-8") as f:
            json.dump(new_po_hash_map, f, indent=2)

    end_time = time.time()
    print(f"\nDone. compiled={compiled}, errors={errors}, TRANSLATIONS_BUILD_DIR={TRANSLATIONS_BUILD_DIR} in {end_time - start_time} seconds")
    return 0 if errors == 0 else 1


def compiled_lang_dir_for(lang):
    """
    We mirrored the input dir tree under TRANSLATIONS_BUILD_DIR.
    So: find the source lang dir, then compute the compiled lang dir by relpath.
    """
    src_map = build_language_file_map()
    src_lang_dir = src_map.get(lang)
    if not src_lang_dir:
        raise ValueError(f"Unknown language '{lang}'. Available: {sorted(src_map.keys())}")
    rel = os.path.relpath(src_lang_dir, TRANSLATIONS_SRC_DIR)
    return os.path.join(TRANSLATIONS_BUILD_DIR, rel)


def find_nested_po(base):
    from pathlib import Path
    base = Path(base)
    nested = []
    for lang_dir in base.iterdir():
        if not lang_dir.is_dir() or lang_dir.name in {"pot", "psd"}:
            continue
        for p in lang_dir.rglob("*.po"):
            if p.parent != lang_dir:   # deeper than the language root
                nested.append(p)
    return nested


def iter_mo_files_for_lang(lang):
    lang_dir = compiled_lang_dir_for(lang)
    if not os.path.isdir(lang_dir):
        print('compiled translations not found, check the cache build')
        return []
    mos = []
    for fn in os.listdir(lang_dir):
        if fn.endswith(".mo") and fn.endswith(f"({lang}).mo"):
            mos.append(os.path.join(lang_dir, fn))
    # Fallback: if names don’t include (lang), take all .mo
    if not mos:
        mos = [os.path.join(lang_dir, fn) for fn in os.listdir(lang_dir) if fn.endswith(".mo")]
    return sorted(mos)


def identity_filter(val, msgid):
    """
    Treat as untranslated if source text is a placeholder (i.e. equal msgid and msgstr)
    """
    if not val:
        return ""
    val = val.strip()
    # treat as untranslated only if EXACTLY the same as msgid
    return "" if val == msgid else val

def load_merged_catalog(lang):
    """
    Merge all catalogs for a language. First non-identity translation wins.
    Returns a dict: {msgid: msgstr}
    """
    merged = {}
    for mo_path in iter_mo_files_for_lang(lang):
        try:
            with open(mo_path, "rb") as f:
                cat = gettext.GNUTranslations(f)
        except Exception:
            continue

        for k, v in getattr(cat, "_catalog", {}).items():
            if not isinstance(k, str) or k =='': 
                continue
            if not v:
                continue
            if k not in merged and (iv := identity_filter(v, k)):
                merged[k] = iv
    return merged

def is_all_caps_tag(s: str) -> bool:
    # Consider ENUM tags like DOUBLE, DOUBLE_PANEL_HORIZONTAL, USERDEFINED etc.
    parts = s.split("_")
    if not parts:
        return False
    has_alpha = any(any(c.isalpha() for c in p) for p in parts)
    return has_alpha and all(p == p.upper() for p in parts)

def strip_wikilinks(text, resource = None, drop_base = False):
    WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
    def repl(m):
        inner = m.group(1)
        if drop_base and resource and inner == resource:
            return "" 
        return inner  
    return re.sub(r"\s{2,}", " ", WIKILINK_RE.sub(repl, text)).strip()

def translate_resource(lang, resource):
    """
    Returns:
      {
        "resource_translation": "…",
        "DESCRIPTION": "… or ''",
        "DEFINITION": "… or ''",
        "<OTHER_ENUM>": "…", (optional)
        ...
      }
    """
    catalog = load_merged_catalog(lang)
    out = {"resource_translation": identity_filter(catalog.get(resource, ""), resource) or ""}

    prefix = resource + "_"

    # Always include description and definition fields (even if untranslated -> '')
    for field in ("DESCRIPTION", "DEFINITION"):
        key = prefix + field
        val = identity_filter(catalog.get(key, ""), key) or ""
        out[field] = val

    # Add all remaining ENUM (caps) variants
    for msgid, msgstr in catalog.items():
        if not msgid.startswith(prefix):
            continue
        suffix = msgid[len(prefix):]
        if not is_all_caps_tag(suffix):
            continue
        if suffix in out:  # skip forced fields we already set
            continue
        val = identity_filter(msgstr, msgid)
        if val:
            out[suffix] = val

    # remove wikileaks (e.g. '[[IfcBeam]]' --> 'IfcBeam')
    for k, v in list(out.items()):
        if isinstance(v, str) and v:
            out[k] = strip_wikilinks(v, resource=resource, drop_base=False)

    return out

def list_languages():
    # get a list of available languages 
    langs = build_language_file_map()
    return(sorted(langs.keys()))

def get_translations(resource):
    return {lang: translate_resource(lang, resource) for lang in list_languages()}


def _country_code_to_flag(cc: str) -> str:
    """Convert ISO 3166-1 alpha-2 to a flag emoji."""
    if not cc or len(cc) != 2 or not cc.isalpha():
        return "🌐"
    cc = cc.upper()
    return "".join(chr(0x1F1E6 + ord(c) - ord("A")) for c in cc)


@lru_cache(maxsize=1)
def build_language_flag_map():
    """
    Returns: { 'Dutch': '🇳🇱', 'Portuguese_Brazilian': '🇧🇷', ... }
    """
    flag_map = {}
    for language, lang_path in build_language_file_map().items():
        region = os.path.basename(os.path.basename(lang_path)).split("-")[-1].upper()
        if language == "Serbian": #todo handle serbian translations separately
            region = "RS"
        flag_map[language] = _country_code_to_flag(region) if region else "🌐"
    flag_map['English, UK'] = _country_code_to_flag('GB')
    return flag_map


def get_language_icon(language):
    """Return a single flag for a language name."""
    def _flag_map():
        return build_language_flag_map()

    if not language and has_request_context():
        language = request.cookies.get("languagePreference", "English, UK")
    return _flag_map().get(language or "English, UK", "🇬🇧")


def main(argv=None):
    """
    Translation Cache Builder & Translator
    --------------------------------------

    Build / Update Translation Cache
    --------------------------------
    # 1. Initial build (first run)
    #    Creates a mirror directory with compiled .mo translations.
    python translate.py build-cache
    or 
    import translate; build_cache()

    # 2. Fast update (default)
    #    Use file modification times (mtime) to recompile only changed .po files.
    python translate.py build-cache

    # 3. Hash-based update
    #    Compares hashes of .po files; recompiles only when content changes.
    #    Also updates the .po → hash mapping file (po_hash_map.json).
    python translate.py build-cache --hash
    or
    import translate; build_cache(use_hash=True)

    # 4. Full clean rebuild
    #    Deletes the compiled translations directory, then does a full hash-based rebuild.
    #    (--clean automatically implies --hash)
    python translate.py build-cache --clean
    or
    import translate; build_cache(clean=True, use_hash=True)
    
    # 5. Multi-threaded build ; compile in parallel
    #    The -j/--jobs flag controls the number of worker threads.
    Examples:
    python translate.py build-cache --hash -j 4
    or
    import translate; build_cache(use_hash=True, jobs=4)


    Translate
    --------------------
    # Translate a specific resource key to the given language or to all languages.
    # The language name must match exactly the one found in .po filenames (can be listed by calling 'list_languages()' )
    python translate.py translate <resource> --lang "<LanguageName>"

    Examples:
        python translate.py translate IfcWall --lang "Dutch"
        python translate.py translate PartitioningType --lang "Portuguese, Brazilian"
        
    or 
        translate_resource('Dutch', 'IfcWall')
        translate_resource ('Portuguese, Brazilian', 'IfcPartioningType')
        
    In case no language is specified, the resource will be translated to all available languages
    Examples: 
        python translate.py translate IfcWall 
    or  
        get_translations(resource)
    
    List all available Languages
    --------------------
    # Show all languages detected from the translations repository.
    python translate.py list-languages
    or 
    list_languages()
    """
    if argv is None:
        # option to call main directly
        argv = sys.argv[1:]

    if not argv:
        top = argparse.ArgumentParser(description="Translations helper")
        top.add_argument("cmd", choices=["build-cache", "translate", "list-languages"], help="Command to run")
        top.print_help(sys.stderr)
        return 2

    cmd, rest = argv[0], argv[1:]

    if cmd == "build-cache":
        p = argparse.ArgumentParser(prog="translate.py build-cache",
                                    description="Compile all .po files into .mo (mirrors tree)")
        p.add_argument("--clean", action="store_true",help="Clean compiled .mo files before building")
        p.add_argument("--hash", action="store_true", help="Use hash map to detect new translations")
        p.add_argument("-j", "--jobs", type=int, default=1, help="Parallel workers for compilation (default: 1, single-threaded)"
)
        args = p.parse_args(rest)
        
        use_hash = args.hash or args.clean # use hash the first time after cleaning the compiled translations
        rc = build_cache(clean=args.clean, use_hash=use_hash, jobs=args.jobs)
        
        sys.exit(rc)

    elif cmd == "translate":
        p = argparse.ArgumentParser(prog="translate.py translate",
                                    description="Translate a specific resource key")
        p.add_argument("resource", help="Base resource id, e.g., IfcWall or PartitioningType")
        p.add_argument("--lang",
                       help="Human language name (as found in filenames), e.g., 'Dutch' or 'Portuguese, Brazilian'")
        args = p.parse_args(rest)
        
        if args.lang:
            try:
                output = translate_resource(lang=args.lang, resource=args.resource)
            except ValueError as e:
                lang_map = build_language_file_map()
                print(f"[ERROR] {e}", file=sys.stderr)
                print(f"Known languages: {', '.join(sorted(lang_map.keys()))}", file=sys.stderr)
                sys.exit(2)
        else:
            output = get_translations(args.resource)
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return 0
    
    elif cmd == "list-languages":
        print(list_languages())
        return 0

    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        print("Use one of: build-cache, translate", file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
