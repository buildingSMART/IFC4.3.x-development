# imports the markdown definitions for properties from the bSI/IFC repository

import os
import sys
import glob

from collections import defaultdict

dr = sys.argv[1]
odr = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "docs", "schemas")

md_files = glob.glob(os.path.join(dr, "**", "Documentation.md"), recursive=True)
xml_files = glob.glob(os.path.join(dr, "**", "Doc*.xml"), recursive=True)

to_ignore = {"ChangeSets", "ModelViews", "Properties", "Publications", "Templates", "Quantities", "Primitives"}

def yield_relevant(fns):
    for fn in fns:
        parts = fn[len(dr)+1:].split(os.sep)[::-1]
        
        if set(parts) & to_ignore:
            # currently not imported
            continue
            
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
            

from xml.dom.minidom import parse

for fn, of, name, type, schema, group in yield_relevant(xml_files):

    if type == "GlobalRules":
        continue

    if not os.path.exists(os.path.dirname(of)):
        os.makedirs(os.path.dirname(of))

    print(fn)
    dom = parse(fn)
    
    pairs = [
        ("Attributes", dom.getElementsByTagName("DocAttribute")),
        ("Formal Propositions", dom.getElementsByTagName("DocWhereRule")),
        ("UniqueRules", dom.getElementsByTagName("DocUniqueRule")),
        ("Items", dom.getElementsByTagName("DocConstant"))
    ]

    num_elems = sum(len(p[1]) for p in pairs)
    i = 1
    
    with open(of, "a", encoding="utf-8") as f:
    
        if num_elems:
            print(file=f)
    
        for lbl, elems in pairs:
            if elems:
                print("##", lbl, end="\n\n", file=f)
                for elem in elems:

                    if elem.tagName == 'DocConstant':
                        # in case of constants we need to lookup the definition in another
                        # XML file. We can then use the same logic on Name and Documentation
                        href = elem.getAttribute("href")
                        cnst_fn = os.path.join(dr, 'Constants', href[0].lower(), href + ".xml")
                        if not os.path.exists(cnst_fn):
                            name = href.split("_", 1)[0]
                            elem = None
                        else:
                            dom2 = parse(cnst_fn)
                            elem = dom2.getElementsByTagName("DocConstant")[0]

                    print("###", elem.getAttribute("Name") if elem is not None else name, file=f)

                    docstring = ""
                    # can be None in case of missing constant
                    if elem is not None:
                        doc = elem.getElementsByTagName("Documentation")
                        if doc and doc[0].childNodes:
                            docstring = doc[0].childNodes[0].data

                    print(docstring, file=f)
                        
                    if i < num_elems:
                        print(file=f)
                    i += 1
