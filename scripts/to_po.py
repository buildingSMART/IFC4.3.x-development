import os
import re
import sys
import html
import operator

from xmi_document import xmi_document

try:
    fn = sys.argv[1]
    try:
        OUTPUT = open(sys.argv[2], "w", encoding='utf-8')
    except IndexError as e:
        OUTPUT = sys.stdout
except:
    print("Usage: python to_po.py <schema.xml>", file=sys.stderr)
    exit()

xmi_doc = xmi_document(fn)
bfn = os.path.basename(fn)

all_names = re.compile("\\b(%s)\\b" % "|".join(sorted((item.name for item in xmi_doc if item.type != "FUNCTION"), key=lambda s: -len(s))))

HTML_TAG_PATTERN = re.compile('<.*?>')
MULTIPLE_SPACE_PATTERN = re.compile(' +')
def strip_html(s):
    S = html.unescape(s)
    i = S.find('\\n')
    if i != -1:
        S = S[:i]
    return re.sub(HTML_TAG_PATTERN, '', S)
    
def valid_key(s):
    return ''.join(c if c.isalnum() else '_' for c in s).strip('_')

def generate_definitions():
    for item in xmi_doc:

        loc = xmi_doc.xmi.locate(item.node) if item.node else None
        yield loc, (valid_key(item.name),), (item.documentation if item.node else item.name)
        
        if item.type in {"ENUM", "ENTITY", "PSET", "PENUM"}:
            for subitem in item:
                loc = xmi_doc.xmi.locate(subitem.node) if subitem.node else None
                yield loc, (valid_key(item.name), valid_key(subitem.name)), ((subitem.documentation or subitem.name) if subitem.node else subitem.name)
        
def quote(s):
    return '"%s"' % s
        
def format(s):
    return quote(re.sub(MULTIPLE_SPACE_PATTERN, ' ', ''.join([' ', c][c.isalnum() or c in '.,'] for c in s)).strip())
    
def annotate(s):
    return re.sub(all_names, lambda match: "[[%s]]" % match.group(0), s)
    
    
print("""# Industry Foundation Classes IFC.
# Copyright (C) 2020 buildingSMART
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\\n"
"Report-Msgid-Bugs-To: http://bugs.kde.org\\n"
"POT-Creation-Date: 2020-09-25 10:09+0200\\n"
"X-Crowdin-SourceKey: msgstr\\n"
"Language-Team: buildingSMART community\\n"
""", file=OUTPUT)

for i, ((ln, col), p, d) in enumerate(generate_definitions()):
    if ln:
        print('#:', bfn, ':', ln, sep='', file=OUTPUT)
    
    print("msgid", quote("_".join(p)),  file=OUTPUT)
    print("msgstr", format(p[-1]),  file=OUTPUT)
    print(file=OUTPUT)
    
    print("msgid", quote("_".join(p + ("DEFINITION",))),  file=OUTPUT)
    print("msgstr", annotate(format(strip_html(d or ''))),  file=OUTPUT)
    print(file=OUTPUT)
    
    if (i % 1000) == 0 and i:
        print(i, "items written", file=sys.stderr)
