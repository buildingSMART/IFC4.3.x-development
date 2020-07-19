import os
import re
import sys
import html
import operator

import xmi

try:
    fn = sys.argv[1]
    try:
        OUTPUT = open(sys.argv[2], "w", encoding='utf-8')
    except IndexError as e:
        OUTPUT = sys.stdout
except:
    print("Usage: python to_po.py <schema.xml>", file=sys.stderr)
    exit()

xmi_doc = xmi.doc(fn)
bfn = os.path.basename(fn)

schema_name = xmi_doc.by_tag_and_type["packagedElement"]['uml:Package'][1].name.replace("exp", "").upper()
schema_name = "".join(["_", c][c.isalnum()] for c in schema_name)
schema_name = re.sub(r"_+", "_", schema_name)
schema_name = schema_name.strip('_')

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
    """
    A generator that yields tuples of <a, b> with
    a: location in file
    a: a fully qualifying key as tuple
    b: the documentation string
    """
    
    def process(node):
        loc = xmi_doc.locate(node)
        # import pdb; pdb.set_trace()
        docs = (node/"properties")[0].documentation
        return loc, (schema_name, valid_key(node.name)), docs
    
    for d in xmi_doc.by_tag_and_type["element"]["uml:DataType"]:
        yield process(d)
        
    for c in xmi_doc.by_tag_and_type["element"]["uml:Class"]:
        yield process(c)
        
        stereotype = (c/"properties")[0].stereotype
        if stereotype is not None: 
            stereotype = stereotype.lower()            
        
        if stereotype == "enumeration":
        
            def try_get_order(a):
                try:
                    return int([t for t in a/("tag") if t.name == "ExpressOrdering"][0].value)
                except IndexError as e:
                    return 0
                    
            values = map(operator.itemgetter(1), sorted(map(lambda a: (try_get_order(a), a), c/("attribute"))))
            for v in values:
                loc = xmi_doc.locate(v)
                docs = (v|"properties").documentation
                yield loc, (schema_name, valid_key(c.name), valid_key(v.name)), docs
                
        else:
            for la in c/("attribute"):
                loc = xmi_doc.locate(la)
                docs = (la|"properties").documentation
                yield loc, (schema_name, valid_key(c.name), valid_key(la.name)), docs
        
def format(s):
    return '"%s"' % re.sub(MULTIPLE_SPACE_PATTERN, ' ', ''.join([' ', c][c.isalnum() or c in '.,'] for c in s)).strip()
    
for i, ((ln, col), p, d) in enumerate(generate_definitions()):
    print('#:', bfn, ':', ln, sep='', file=OUTPUT)
    
    print("msgid", "_".join(p[1:]),  file=OUTPUT)
    print("msgstr", format(p[-1]),  file=OUTPUT)
    print(file=OUTPUT)
    
    print("msgid", "_".join(p[1:] + ("DEFINITION",)),  file=OUTPUT)
    print("msgstr", format(strip_html(d or '')),  file=OUTPUT)
    print(file=OUTPUT)
    
    if (i % 1000) == 0 and i:
        print(i, "items written", file=sys.stderr)
