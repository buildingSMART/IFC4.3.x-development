import os
import sys
import glob
import json

from xml.dom.minidom import parse

dr = sys.argv[1]
odr = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "docs", "schemas")

xml_files = glob.glob(os.path.join(dr, "**", "PEnum_*.xml"), recursive=True)

# The PEnums in IfcDoc don't have containment in a Domain. In UML we do,
# so we need to first parse the XMI to map PEnums to a Domain.
hierarchy = json.load(open("hierarchy.json"))
from server import resource_paths
definition_to_package = {a:b[0:2] for a, b in resource_paths(hierarchy)}

constants = {}
for fn in glob.glob(os.path.join(dr, 'Constants', '**', "*.xml"), recursive=True) + \
    glob.glob(os.path.join(dr, 'PropertyConstants', '**', "*.xml"), recursive=True):
    
    dom = parse(fn)
    
    id = dom.childNodes[0].getAttribute("id")
    name = dom.childNodes[0].getAttribute("Name")
    
    definition = ''
    try:
        locs = [x for x in dom.childNodes[0].getElementsByTagName("Localization")[0].childNodes if x.nodeType == x.ELEMENT_NODE and x.tagName == 'DocLocalization']
        assert len(locs) == 1        
        assert locs[0].getAttribute('Locale') == 'en'
        definition = locs[0].getAttribute('Name')
    except: pass
    
    if not definition:
        try:
            definition = dom.childNodes[0].getElementsByTagName("Documentation")[0].childNodes[0].data
        except: pass

    constants[id] = [name, definition]

for fn in xml_files:
    parts = fn[len(dr)+1:].split(os.sep)[::-1]
    name = parts[0].replace(".xml", "")
    try:
        group, schema = definition_to_package[name]
    except:
        continue
    type = "PropertyEnumerations"
    of = os.path.join(
        odr,
        group,
        schema,
        type,
        name + ".md"
    )

    updated = False
    lines = list(open(of, encoding='utf-8'))
    ignored = {'NOTKNOWN', 'UNSET', 'OTHER'}

    dom = parse(fn)
    for elem in dom.getElementsByTagName("DocPropertyConstant"):
        
        href = elem.getAttribute("href")
        cname, docstring = constants[href]

        try:
            idx0 = lines.index(f'### {cname}\n')
        except:
            print(name, cname, "not found")
            print()
            
        try:
            idx1 = list(map(lambda l: l.startswith('### '), lines)).index(True, idx0+1)
        except:
            idx1 = 1000
            
        if lines[idx0+1].strip():
            if lines[idx0+1].strip() != docstring.strip():
                if cname not in ignored:
                    print(name, cname)
                    print()
                    print("current:")
                    print(lines[idx0+1].strip())
                    print("old:")
                    print(docstring.strip())
                    print()
            
        else:
            lines[idx0+1] = docstring.strip() + "\n"
            updated = True
            
    if updated:
        open(of, "w", encoding='utf-8').write("".join(lines))
