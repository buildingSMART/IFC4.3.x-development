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
    i = S.find('\n')
    if i != -1:
        S = S[:i]
    return re.sub(HTML_TAG_PATTERN, '', S)
    
def valid_key(s):
    return ''.join(c if c.isalnum() else '_' for c in s).strip('_')

def generate_definitions():
    for item in xmi_doc:
        loc = xmi_doc.xmi.locate(item.node)
        yield loc, (valid_key(item.node.name),), item.documentation
        
        if item.type in {"ENUM", "ENTITY", "PSET"}:
            for subitem in item:
                loc = xmi_doc.xmi.locate(subitem.node)
                yield loc, (valid_key(item.node.name), valid_key(subitem.name)), (subitem.documentation or subitem.name)
        
def quote(s):
    return '"%s"' % s
        
def format(s):
    return quote(re.sub(MULTIPLE_SPACE_PATTERN, ' ', ''.join([' ', c][c.isalnum() or c in '.,'] for c in s)).strip())
    
def annotate(s):
    return re.sub(all_names, lambda match: "[[%s]]" % match.group(0), s)
    
print('msgid ""', file=OUTPUT)
print('msgstr ""', file=OUTPUT)
print('"X-Crowdin-SourceKey: msgstr\\n"', file=OUTPUT)
print(file=OUTPUT)
    
for i, ((ln, col), p, d) in enumerate(generate_definitions()):
    print('#:', bfn, ':', ln, sep='', file=OUTPUT)
    
    print("msgid", quote("_".join(p)),  file=OUTPUT)
    print("msgstr", format(p[-1]),  file=OUTPUT)
    print(file=OUTPUT)
    
    print("msgid", quote("_".join(p + ("DEFINITION",))),  file=OUTPUT)
    print("msgstr", annotate(format(strip_html(d or ''))),  file=OUTPUT)
    print(file=OUTPUT)
    
    if (i % 1000) == 0 and i:
        print(i, "items written", file=sys.stderr)
