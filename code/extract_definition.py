import re
import os
import html


MULTIPLE_LINEBREAK_PATTERN = re.compile("\n+")
FORMULA_PATTERN = re.compile(r'(Base|General) formula')
DOLAR_PATTERN = re.compile(r'\$\$')
ASTERIX_PATTERN = re.compile(r'\*\*')
SENTENCE_WITH_PSET_PATTERN = re.compile(r'[^.?!]*\b(_Pset|_Qto)\b[^.?!]*[.?!]')
HEADING_PATTERN = re.compile(r'\#+')
KEYWORDS = ['NOTE', 'Note: ', 'DIAGRAM', 'CHANGE', 'IFC4', 'HISTORY', 'REFERENCE', 'EXAMPLE', 'DEPRECATION']


def extract_definition(txt, return_short=True, return_marked=False, print_split=False):
    """ Parse the original text and return only the semantic definition or place a marker at its end. """

    heading = txt.split('\n\n', 1)[0]+'\n\n'
    txt = txt[len(heading):]
    MARKER = '<!-- end of definition -->'

    if not return_short and not return_marked:
        return txt

    try:
        txt = html.unescape(txt)
    except TypeError:
        # Error when content is a link, for example: "https://github.com/buildingSMART/IFC4.3.x-development/edit/master/docs/schemas/core/IfcProductExtension/Types/IfcAlignmentTypeEnum.md#L0 has no content"
        txt = ''
    s1 = re.search(DOLAR_PATTERN, txt).start() if re.search(DOLAR_PATTERN, txt) else -1      # formula
    s2 = re.search(FORMULA_PATTERN, txt).start() if re.search(FORMULA_PATTERN, txt) else -1  # formula
    s3 = re.search(MULTIPLE_LINEBREAK_PATTERN, txt).start() if re.search(MULTIPLE_LINEBREAK_PATTERN, txt) else -1  # line break  
    s4 = -1
    for k in KEYWORDS:
        x = txt.find(k)
        if x>s4:
            s4=x
    s5 = re.search(SENTENCE_WITH_PSET_PATTERN, txt).start() if re.search(SENTENCE_WITH_PSET_PATTERN, txt) else -1
    s6 = re.search(HEADING_PATTERN, txt).start() if re.search(HEADING_PATTERN, txt) else -1
    i = min([x for x in [s1, s2, s3, s4, s5, s6, 1e5] if x >= 0])
    
    if txt[i-1] in [":","-","–"]:
        i = find_last_bullet_end_position(txt, i)

    # Execute
    if i >= 0 and i != 1e5:
        if print_split:
            print('\n\n\033[92m'+heading + txt[:i] + '\033[91m' + txt[i:i+500]+'...\033[0m')
        if return_short:
            return txt[:i]
        elif return_marked:
            return heading + txt[:i] + MARKER + txt[i:]


def find_last_bullet_end_position(text, i):
    """ Finds the last bullet point of the current list. """
    lines = text[i:].split('\n')
    bullet_length = 0
    for line in lines:
        if line.strip() == '':
            bullet_length += 1
        elif line.strip().startswith('*'):
            bullet_length += len(line) +1
        elif line.strip().startswith('and'):
            bullet_length += len(line) +1
        else:
            return i + bullet_length -1

def enrich_all_markdowns(directory_path, save=False):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file[len(file)-3:] == '.md' and file != 'README.md':
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        new_def = extract_definition(file.read(), return_short=False, return_marked=True, print_split=True)
                    if save:
                        with open(file_path, 'w', encoding='utf-8') as file:
                            file.write(new_def)
                except Exception as e:
                    print(f"Failed to read {file_path}: {e}")


if __name__ == "__main__":
       
    directory_path = "..\docs\schemas"
    enrich_all_markdowns(directory_path, save=False)