# imports the markdown definitions for properties from the bSI/IFC repository

import os
import sys
import glob
import json

from collections import defaultdict

from xml.dom.minidom import parse

dr = sys.argv[1]
odr = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "docs", "schemas")

md_files = glob.glob(os.path.join(dr, "**", "Documentation.md"), recursive=True)
xml_files = glob.glob(os.path.join(dr, "**", "Doc*.xml"), recursive=True) + \
    glob.glob(os.path.join(dr, "**", "PEnum_*.xml"), recursive=True)

to_ignore = {"ChangeSets", "ModelViews", "Properties", "Publications", "Templates", "Quantities", "Primitives"}
to_include = {"PropertyEnumerations"}

# The PEnums in IfcDoc don't have containment in a Domain. In UML we do,
# so we need to first parse the XMI to map PEnums to a Domain.
hierarchy = json.load(open("hierarchy.json"))
from server import resource_paths
definition_to_package = {a:b[0:2] for a, b in resource_paths(hierarchy)}

constants = {}
for fn in glob.glob(os.path.join(dr, 'Constants', '**', "*.xml"), recursive=True) + \
    glob.glob(os.path.join(dr, 'PropertyConstants', '**', "*.xml"), recursive=True):
    
    dom = parse(fn)
    
    name = dom.childNodes[0].getAttribute("Name")
    id = dom.childNodes[0].getAttribute("id")
    try:
        definition = dom.childNodes[0].getElementsByTagName("Documentation")[0].childNodes[0].data
    except:
        definition = ""

    constants[id] = [name, definition]
    
def yield_relevant(fns):
    for fn in fns:
        parts = fn[len(dr)+1:].split(os.sep)[::-1]
        
        if not (set(parts) & to_include):
            # currently not imported
            continue
            
        if "PropertyEnumerations" in parts:
        
            name = parts[0].replace(".xml", "")
            
            if name not in definition_to_package:
                print(f"Not modelled: {name}")
                continue
        
            group, schema = definition_to_package[name]
            type = "PropertyEnumerations"
            
            of = os.path.join(
                odr,
                group,
                schema,
                type,
                name + ".md"
            )
            
            yield fn, of, name, type, schema, group
        else:
            
            if len(parts) < 7:
                # section or schema documentation, not a full path to entity/type
                continue
            
            _, name, type, schema, __, group = parts[0:6]
            
            of = os.path.join(
                odr,
                group.split(' ')[0].lower(),
                schema,
                type,
                name + ".md"
            )
            
            yield fn, of, name, type, schema, group
    
for fn, of, name, type, schema, group in yield_relevant(md_files):
    
    if not os.path.exists(os.path.dirname(of)):
        os.makedirs(os.path.dirname(of))

    with open(fn, encoding="utf-8-sig") as f0:
        with open(of, "w", encoding="utf-8") as f:
            print("#", name, file=f)
            print(file=f)
            print(f0.read().strip().replace("../../../../../../", "../../../../"), file=f)


for fn, of, name, type, schema, group in yield_relevant(xml_files):

    if type == "GlobalRules":
        continue

    if not os.path.exists(os.path.dirname(of)):
        os.makedirs(os.path.dirname(of))

    dom = parse(fn)
    
    pairs = [
        ("Attributes", dom.getElementsByTagName("DocAttribute")),
        ("Formal Propositions", dom.getElementsByTagName("DocWhereRule")),
        ("UniqueRules", dom.getElementsByTagName("DocUniqueRule")),
        ("Items", dom.getElementsByTagName("DocConstant")),
        ("Items", dom.getElementsByTagName("DocPropertyConstant"))
    ]

    num_elems = sum(len(p[1]) for p in pairs)
    i = 1

    with open(of, "a", encoding="utf-8") as f:

        if dom.childNodes[0].tagName == "DocPropertyEnumeration":
            # @nb they don't have a corresponding md in ifcdoc, so
            # we need to create on from the definition
            print(f"# {name}\n", file=f)
            
            try:
                definition = dom.childNodes[0].getElementsByTagName("Documentation")[0].childNodes[0].data
                print(f"{definition}\n", file=f)
            except:
                pass            
    
        elif num_elems:
            print(file=f)
    
        for lbl, elems in pairs:
            if elems:
                print("##", lbl, end="\n\n", file=f)
                for elem in elems:

                    docstring = ""
                    if elem.tagName == 'DocConstant' or elem.tagName == 'DocPropertyConstant':
                        # in case of constants we need to lookup the definition in another
                        # XML file. We can then use the same logic on Name and Documentation
                        href = elem.getAttribute("href")
                        if href:
                            name, docstring = constants[href]
                        else:
                            name = elem.getAttribute("Name")
                            assert name
                            docstring = ""
                    else:
                        name = elem.getAttribute("Name")
                        assert name
                        try:
                            docstring = elem.getElementsByTagName("Documentation")[0].childNodes[0].data
                        except:
                            docstring = ""
                        
                    print(f"### {name}", file=f)
                    print(docstring, file=f)
                        
                    if i < num_elems:
                        print(file=f)
                    i += 1
