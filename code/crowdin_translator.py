import os
import gettext
import tempfile
import subprocess
import polib
import sys
import re

def get_language_file_map(translations_path):
    language_dict = {}

    for lang_dir in os.listdir(translations_path):
        lang_path = os.path.join(translations_path, lang_dir)
        if os.path.isdir(lang_path):
            po_files = [f for f in os.listdir(lang_path) if f.endswith(".po")]
            if po_files:
                match = re.search(r'\(([^)]+)\)\.po$', po_files[0])
                if match:
                    lang_name = match.group(1)
                    language_dict[lang_dir] = lang_name

    return {y:os.path.join(translations_path, i) for i, y in language_dict.items()}


class CrowdinTranslator:
    CACHE_DIR = tempfile.gettempdir()
    TRANSLATIONS_DIR = os.environ.get('TRANSLATIONS_DIR', os.path.join(os.path.dirname(__file__), 'translate_repo'))
    CROWDIN_FILES  = os.path.join(TRANSLATIONS_DIR, 'translations')
    CROWDIN_REPO_DIR = os.environ.get('CROWDIN_REPO_DIR', os.path.join(os.path.dirname(__file__), 'translate_repo'))

    def __init__(self, translations_dir=None, crowdin_files=None, crowdin_repo_dir=None):
        self.translations_dir = translations_dir or CrowdinTranslator.TRANSLATIONS_DIR
        self.crowdin_files = crowdin_files or os.path.join(self.translations_dir, 'translations')
        self.language_file_map = get_language_file_map(self.crowdin_files)
        self.crowdin_repo_dir = crowdin_repo_dir or CrowdinTranslator.CROWDIN_REPO_DIR
       

    def translate(self, resource):
        """Translate the given resource into the specified language."""
        translations_map = {}

        for lang in self.language_file_map.keys():
            translations = self.load_translations(lang)
            if not translations:
                continue

            def get_filtered_translations(resource):
                keys_and_patterns = [
                    (resource, resource),
                    (f"{resource}_DESCRIPTION", f"{resource}_DESCRIPTION"),
                    (f"{resource}_DEFINITION", f"{resource}_DEFINITION")
                ]

                translations_filtered = [
                    None if (translation := translations.gettext(key)) and translation.startswith(pattern) else translation
                    for key, pattern in keys_and_patterns
                ]
                return tuple(translations_filtered)

            resource_translation, description_translation, definition_translation = get_filtered_translations(resource)
            resource_pattern = f'[[{resource}]]'
            if definition_translation and definition_translation.startswith(resource_pattern):
                definition_translation = definition_translation.replace(resource_pattern, '').lstrip()

            translations_map[lang] = {
                "resource_translation": resource_translation or "",
                "description": description_translation or "",
                "definition": definition_translation or ""
            }
        return translations_map

    def compile_po_to_mo(self, po_file_path, mo_file_path):
        """Compile the .po file to a .mo file using msgfmt."""
        try:
            subprocess.run(['msgfmt', po_file_path, '-o', mo_file_path], check=True)
            return mo_file_path
        except subprocess.CalledProcessError as e:
            print(f"Error compiling {po_file_path} to .mo: {e}")
            return None

    def save_composite_translation_as_mo(self, composite_translation, mo_file_path):
        """Save the composite translation as a .mo file using polib."""
        po = polib.POFile()
        for msgid, msgstr in composite_translation._catalog.items():
            entry = polib.POEntry(msgid=msgid, msgstr=msgstr)
            po.append(entry)
        po.save_as_mofile(mo_file_path)

    def load_translations(self, lang):
        """Load the translations for a given language using compiled .mo files."""
        lang_dir = self.language_file_map.get(lang)
        if not lang_dir:
            print(f"Language '{lang}' is not supported.")
            return None

        composite_mo_file_path = os.path.join(self.CACHE_DIR, f"{lang}_composite.mo")
        if os.path.exists(composite_mo_file_path):
            return gettext.GNUTranslations(open(composite_mo_file_path, "rb"))

        composite_translation = None
        for po_file in os.listdir(lang_dir):
            if po_file.endswith(f'({lang}).po'):
                po_file_path = os.path.join(lang_dir, po_file)
                temp_mo_file_path = os.path.join(self.CACHE_DIR, f"temp_{lang}.mo")

                compiled_mo_file = self.compile_po_to_mo(po_file_path, temp_mo_file_path)
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

        if composite_translation:
            self.save_composite_translation_as_mo(composite_translation, composite_mo_file_path)
        return composite_translation
    
    def load_original(self, resource):
        pot_directory = os.path.join(CrowdinTranslator.CROWDIN_REPO_DIR, 'pot')
        
        original_values = {}
        return original_values

        for pot_file_name in os.listdir(pot_directory):
            if pot_file_name.endswith('.pot'):
                pot_file_path = os.path.join(pot_directory, pot_file_name)
                try:
                    pot_file = polib.pofile(pot_file_path)
                except (IOError, OSError) as e:
                    fix_pot_file(os.path.join(pot_directory, pot_file_name))
                    pot_file = polib.pofile(pot_file_path)
                
                for entry in pot_file:
                    if entry.msgid == resource:
                        original_values["name"] = entry.msgstr or entry.msgid
                    elif entry.msgid == f"{resource}_DEFINITION":
                        original_values["definition"] = entry.msgstr or entry.msgid
                    elif entry.msgid == f"{resource}_DESCRIPTION":
                        original_values["description"] = entry.msgstr or entry.msgid

                if "name" in original_values:
                    break
        return original_values
        

def fix_pot_file(file_path):
    """Fixes unescaped double quotes in .pot files by escaping them with backslashes."""
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    fixed_lines = []
    for line in lines:
        if line.strip().startswith("msgid") or line.strip().startswith("msgstr"):
            match = re.match(r'^(msgid|msgstr) "(.*)"$', line.strip())
            if match:
                key, content = match.groups()
                # Escape unescaped double quotes inside the content
                content = re.sub(r'(?<!\\)"', r'\\"', content)
                fixed_line = f'{key} "{content}"\n'
                fixed_lines.append(fixed_line)
            else:
                fixed_lines.append(line)  
        else:
            fixed_lines.append(line)  

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(fixed_lines)


class HTMLCacheManager:
    CACHED_TRANSLATIONS_DIR = os.environ.get('TRANSLATIONS_DIR', tempfile.gettempdir())
    
    def __init__(self, schema_element, cached_translations_dir=None):
        self.schema_element = schema_element # entities, properties or types
        self.cached_translations_dir = cached_translations_dir or HTMLCacheManager.CACHED_TRANSLATIONS_DIR
        self.resource_dir = os.path.join(self.cached_translations_dir, f"{schema_element}")
        if not os.path.isdir(self.resource_dir):
            os.makedirs(self.resource_dir)

    def get_cached_html(self, resource):
        cached_html_path = os.path.join(self.resource_dir, f"{resource}.html")
        if os.path.isfile(cached_html_path):
            with open(cached_html_path, "r", encoding='utf-8') as f:
                return f.read()
        return None
    
    def write_cached_html(self, resource, rendered_html):
        cached_html_path = os.path.join(self.resource_dir, f"{resource}.html")
        with open(cached_html_path, "w", encoding='utf-8') as f:
            f.write(rendered_html)

LANGUAGE_FLAG_MAP = {
    "English_UK": "🇬🇧",
    "Arabic": "🇸🇦",
    "Chinese Simplified": "🇨🇳",
    "Croatian": "🇭🇷",
    "Czech": "🇨🇿",
    "Danish": "🇩🇰",
    "Dutch": "🇳🇱",
    "English": "🇺🇸",
    "Finnish": "🇫🇮",
    "French": "🇫🇷",
    "German": "🇩🇪",
    "Hindi": "🇮🇳",
    "Icelandic": "🇮🇸",
    "Italian": "🇮🇹",
    "Japanese": "🇯🇵",
    "Korean": "🇰🇷",
    "Lithuanian": "🇱🇹",
    "Norwegian": "🇳🇴",
    "Polish": "🇵🇱",
    "Portuguese": "🇵🇹",
    "Portuguese_Brazilian": "🇧🇷",
    "Romanian": "🇷🇴",
    "Slovenian": "🇸🇮",
    "Spanish": "🇪🇸",
    "Swedish": "🇸🇪",
    "Turkish": "🇹🇷",
}


if __name__ == "__main__":
    #@todo
    # print("Usage: python translations.py translate <resource>")
    # print("Usage: python translations.py build-cache") -> concurrent futures to map over get_language_file_map

    if len(sys.argv) < 2:
        print("Usage: python translations.py <resource>")
        sys.exit(1)

    resource = sys.argv[1]
    language_file_map = get_language_file_map()  # Only for local testing

    translator = CrowdinTranslator(language_file_map)
    result = translator.translate(resource)
    print(result)