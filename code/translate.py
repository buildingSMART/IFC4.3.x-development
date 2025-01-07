import os
import gettext
import tempfile
import subprocess
import polib
import sys

CACHE_DIR = tempfile.gettempdir()  # Temporary directory for storing compiled .mo files

def translate(resource):
    """Translate the given resource into the specified language
    If no translations exist, the program compiles .po files into .mo files, saves them in the cache (and makes them available on the server). 
    Each .po file is converted to a .mo file locally using msgfmt, an external library from gettext.
      A combined .mo file is created for each language and saved using polib. 
      If the .mo file for a specific language already exists, it can be retrieved from the cache.

    Alternatively, translations can be done with a one-to-one mapping between .po and .mo files
    (e.g., IfcBuildingControlsDomain_(Dutch).po becomes IfcBuildingControlsDomain_(Dutch).mo).
    This method distributes the translation effort, translating only the relevant .po file when a language is selected.

    In the cumulative method, selecting a language translates all content at once, which is faster and simpler—just call translate('IfcWall', 'Dutch').
    """
    translations_map = {}

    for lang in language_file_map.keys():
        translations = load_translations(lang)
        if not translations:
            continue

        def get_filtered_translations(resource):
            # Use gettext's translation methods to get the resource, description, and definition
            keys_and_patterns = [
                (resource, resource),
                (f"{resource}_DESCRIPTION", f"{resource}_DESCRIPTION"),
                (f"{resource}_DEFINITION", f"{resource}_DEFINITION")
            ]

            # Filter default values out of the ttranslation, i.e. gettext simply returns the original msgid if the matching msgid is empty
            translations_filtered = [
                None if (translation := translations.gettext(key)) and translation.startswith(pattern) else translation
                for key, pattern in keys_and_patterns
            ]

            return tuple(translations_filtered)

        resource_translation, description_translation, definition_translation = get_filtered_translations(resource)

        resource_pattern = f'[[{resource}]]' # e.g. in case a definition is something like '[[IfcBeam]]'とは、主に曲げに耐えることによって荷重に耐えることができる水平な、あるいはほぼ水平な構造部材のことである。建築的な観点からこのような部材を表すこともある。耐荷重である必要はない。'
        if definition_translation and definition_translation.startswith(resource_pattern):
            definition_translation = definition_translation.replace(resource_pattern, '').lstrip()

        translations_map[lang] = {
                "resource_translation": resource_translation or "",
                "description": description_translation or "",
                "definition": definition_translation or ""
            }
    return translations_map

def build_language_file_map():
    """Build a mapping of languages to their translation directories."""
    language_file_map = {}
    translations_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'translate_repo', 'translations')

    for lang_dir in os.listdir(translations_dir):
        full_lang_dir = os.path.join(translations_dir, lang_dir)
        if os.path.isdir(full_lang_dir):
            for po_file in os.listdir(full_lang_dir):
                if po_file.endswith('.po'):
                    lang_name = po_file.split('_(')[-1].split(').po')[0]
                    language_file_map[lang_name] = full_lang_dir  # Store full path to language directory
                    break

    return language_file_map

def compile_po_to_mo(po_file_path, mo_file_path):
    """Compile the .po file to a .mo file using msgfmt (external gettext utility)."""
    try:
        subprocess.run(['msgfmt', po_file_path, '-o', mo_file_path], check=True)
        return mo_file_path
    except subprocess.CalledProcessError as e:
        print(f"Error compiling {po_file_path} to .mo: {e}")
        return None

def save_composite_translation_as_mo(composite_translation, mo_file_path):
    """Save the composite translation as a .mo file using polib."""
    po = polib.POFile()

    # Populate the POFile object with entries from the composite translation catalog
    for msgid, msgstr in composite_translation._catalog.items():
        entry = polib.POEntry(msgid=msgid, msgstr=msgstr)
        po.append(entry)

    po.save_as_mofile(mo_file_path)

def load_translations(lang):
    """Load the translations for a given language using compiled .mo files."""
    lang_dir = language_file_map.get(lang)
    if not lang_dir:
        print(f"Language '{lang}' is not supported.")
        return None

    #combines all translations
    composite_mo_file_path = os.path.join(CACHE_DIR, f"{lang}_composite.mo")

    # If the composite .mo file exists, just load and return it
    if os.path.exists(composite_mo_file_path):
        return gettext.GNUTranslations(open(composite_mo_file_path, "rb"))

    # Otherwise, compile all .po files into a composite translation file
    composite_translation = None

    for po_file in os.listdir(lang_dir):
        if po_file.endswith(f'({lang}).po'):
            po_file_path = os.path.join(lang_dir, po_file)
            temp_mo_file_path = os.path.join(CACHE_DIR, f"temp_{lang}.mo")  # Temporary .mo for each .po

            compiled_mo_file = compile_po_to_mo(po_file_path, temp_mo_file_path)
            if not compiled_mo_file:
                continue

            try:
                translation = gettext.GNUTranslations(open(compiled_mo_file, "rb"))
                if composite_translation:
                    composite_translation._catalog.update(translation._catalog)
                else:
                    composite_translation = translation

            except FileNotFoundError:
                print(f"Error: Temp .mo file not found for {po_file}")
                continue

    # Write the composite translation to a .mo file
    if composite_translation:
        save_composite_translation_as_mo(composite_translation, composite_mo_file_path)

    return composite_translation


language_file_map = build_language_file_map()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translations.py <resource>")
        sys.exit(1)

    resource = sys.argv[1]

    result = translate(resource)
