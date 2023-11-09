import os
import re
import sys
import html
import operator
from datetime import date

from xmi_document import xmi_document

try:
    fn, output_dir = sys.argv[1:]
except:
    print("Usage: python to_po.py <schema.xml> <output_dir>", file=sys.stderr)
    exit()

xmi_doc = xmi_document(fn)
bfn = os.path.basename(fn)

items = list(xmi_doc)
names = ["USERDEFINED", "NOTDEFINED"]  # adding those two to be translatable values, as they occur in descriptions but will not be listed in bSDD. 
for item in items:
    if item.type != "FUNCTION":
        names.append(item.name)
    # add all enumeration values except two 
    if item.type in ("ENUM", "PENUM"):
        for c in item.children:
            if c.name not in ("USERDEFINED", "NOTDEFINED", "UNSET"):
                if len(c.name) > 1 and not c.name.isnumeric():
                    names.append(c.name)
                else:
                    print("Skipped enum: {}".format(c.name))

all_names = re.compile("\\b(%s)\\b" % "|".join(sorted((names), key=lambda s: -len(s))))

HTML_TAG_PATTERN = re.compile('<.*?>')
MULTIPLE_SPACE_PATTERN = re.compile(' +')
CURLY_BRACKET_PATTERN = re.compile('{.*?}')

def strip_html(s):
    S = html.unescape(s)
    i = S.find('\\n')
    if i != -1:
        S = S[:i]
    x = re.sub(HTML_TAG_PATTERN, '', S)
    y = re.sub(CURLY_BRACKET_PATTERN, '', x)
    return y
    
def valid_key(s):
    return ''.join(c if c.isalnum() else '_' for c in s).strip('_')

def generate_definitions():
    props_seen = set()
    
    for item in xmi_doc:

        loc = xmi_doc.xmi.locate(item.node) if item.node else (None, None)
        yield item.package, loc, (valid_key(item.name),), (item.markdown_definition if item.node else item.name)
        
        if item.type in {"ENUM", "ENTITY", "PSET", "PENUM"}:
            for subitem in item:
                loc = xmi_doc.xmi.locate(subitem.node) if subitem.node else (None, None)
                key = (valid_key(item.name), valid_key(subitem.name))
                if item.type == "PSET":
                    key = key[1:]
                    if subitem.name in props_seen:
                        continue
                    props_seen.add(subitem.name)
                yield item.package, loc, key, ((subitem.markdown_definition or subitem.name) if subitem.node else subitem.name)
        
def quote(s):
    return '"%s"' % s
        
def format(s):
    # remove all redundant characters:
    clean = ''.join(['', c][c.isalnum() or c in '.,()- —'] for c in s)
    return quote(re.sub(MULTIPLE_SPACE_PATTERN, ' ', clean).strip())
    
def annotate(s):
    return re.sub(all_names, lambda match: "[[%s]]" % match.group(0), s)

def normalise(s):
    # Convert IFCsh terms into more human readable (e.g. IfcWallCase --> Wall Case)
    if s.isupper():  # e.g. NOTKNOWN or TRIPLEPANELRIGHT
        #TODO check if new IFC.json already has splited words, or implement it here
        x = s #.title()
    elif s.startswith("Ifc") and s.endswith("Enum") and not " " in s:  # e.g. IfcWallTypeEnum
        # skip Ifc and say "enumeration of wall type"
        y = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", s[3:-4]).title()
        x = "Enumeration of {}".format(x)
    elif s.startswith("Ifc") and not " " in s:  # e.g. IfcWallStandardCase
        # skip Ifc and divide into words: Wall standard case
        x = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", s[3:]).title()
    elif not " " in s:  # e.g. UserDefinedPartitioningType
        # split into words: User defined partitioning type
        x = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", s).title()
    else:
        # #TODO review the list if there are no other missed values to explain.
        # print("REVIEW IF THIS IS A PURE DESCRIPTION OR NOT: {}".format(s))
        x = s
    return x
    
class pot_file:
    def __init__(self, f):
        self.f = f
        now = date.today()
        print("""# Industry Foundation Classes IFC.
# Copyright (C) {year} buildingSMART
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\\n"
"Report-Msgid-Bugs-To: http://bugs.kde.org\\n"
"POT-Creation-Date: {date} {time}\\n"
"X-Crowdin-SourceKey: msgstr\\n"
"Language-Team: buildingSMART community\\n"
""".format(year=now.strftime("%Y"), date=now.strftime(r"%Y-%m-%d"), time=now.strftime("%H:%M")), file=self.f)
        
    def __getattr__(self, k):
        return getattr(self.f, k)
        
class pot_dict(dict):
    def __missing__(self, key):
        v = self[key] = pot_file(open(os.path.join(output_dir, key + ".pot"), "w", encoding="utf-8"))
        return v

        
po_files = pot_dict()       

for i, (package, (ln, col), p, d) in enumerate(generate_definitions()):
    po_file = po_files[package]

    if ln:
        print('#:', bfn, ':', ln, sep='', file=po_file)
    
    print("msgid", quote("_".join(p)),  file=po_file)
    print("msgstr", format(p[-1]),  file=po_file)
    print(file=po_file)
    
    print("msgid", quote("_".join(p + ("DEFINITION",))),  file=po_file)
    print("msgstr", normalise(annotate(format(strip_html(d or '')))),  file=po_file)
    print(file=po_file)
    
    if (i % 1000) == 0 and i:
        print(i, "items written", file=sys.stderr)
