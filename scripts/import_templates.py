# imports the markdown definitions for sections from the bSI/IFC repository

import os
import re
import sys
import glob
import json
import itertools

from collections import defaultdict
from xml.etree import ElementTree as ET

IGNORED_TAGS = IGNORED_ATTRS = set()

entity_attributes = json.load(open(os.path.join(
    os.path.abspath(os.path.dirname(__file__)), 
    "..", "server", "entity_attributes.json"
)))

entity_supertype = json.load(open(os.path.join(
    os.path.abspath(os.path.dirname(__file__)), 
    "..", "server", "entity_supertype.json"
)))

def create_entity_definition(e):
    table = [(e, "")]
    while e:
        keys = [x for x in entity_attributes.keys() if x.startswith(e + '.')]
        for k, (is_fwd, ty) in zip(keys, map(entity_attributes.__getitem__, keys)):
            nm = k.split('.')[1]
            
            if is_fwd:
                card = "[0:1]" if "OPTIONAL" in ty else "[1:1]"
            else:
                nm = "<i>%s</i>" % nm
                inv_card = re.findall(r'(\[.+?\])', ty)
                if inv_card:
                    card = inv_card[0]
                else:
                    card = ""
            
            table.append((nm, card))
        e = entity_supertype.get(e)
        
    table = "<<table border=\"0\" cellborder=\"1\" cellspacing=\"0\">%s</table>>" % \
        "".join("<tr>%s</tr>" % "".join("<td port=\"%s%d\">%s</td>" % (r[0],i,c) for i,c in enumerate(r)) for r in table)
    
    return table
    

def get_attribute(x):
    df = entity_attributes.get(x)
    if df:
        return df    
    elif entity_supertype.get(e):
        e, a = x.split(".")
        return get_attribute(entity_supertype[e] + "." + a)
        
    
def reverse_attr(v):
    try:
        is_fwd, df = get_attribute(v)
    except:
        return ""
    if is_fwd:
        return ""
    else:
        return "." + df.split(" FOR ")[-1]

entity_defs = {e: create_entity_definition(e) for e in (set(entity_supertype.values()) & entity_supertype.keys())}

def flatmap(func, *iterable):
    return itertools.chain.from_iterable(map(func, *iterable))

def to_dict(t):
    if t.tag in IGNORED_TAGS:
        return

    # strip out namespace reported by etree as
    # "{http://www.buildingsmart-tech.org/xml/qto/QTO_IFC4.xsd}QtoSetDef"
    items = {'#tag': re.sub(r'\{.+?\}', '', t.tag)}
    
    if list(t):
        items['_children'] = list(flatmap(to_dict, t))
    
    items.update({'@' + k: v for k, v in (t.attrib or {}).items() if k not in IGNORED_ATTRS})
        
    if t.text and t.text.strip():
        items['#text'] = t.text.strip()
        
    yield items
    
def read(fn):
    parser = ET.XMLParser(encoding="utf-8")
    return next(to_dict(ET.parse(fn, parser=parser).getroot()))

dr = sys.argv[1]
odr = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "docs", "templates")

Documentation = "Documentation.md"
DocTemplateDefinition = "DocTemplateDefinition.xml"

def join_with(s):
    return lambda *p: os.path.join(*p, s)
    
make_md = join_with(Documentation)
make_xml = join_with(DocTemplateDefinition)

base = os.path.join(dr, "IFC4x3", "Templates")

templates = sorted(set(map(os.path.dirname, 
    glob.glob(make_md(base, "**"), recursive=True) + \
    glob.glob(make_xml(base, "**"), recursive=True)
)))

for tmpl in templates:
    parts = tmpl[len(base)+1:].split(os.sep)
    of = os.path.join(odr, *parts, "README.md")
    try:
        os.makedirs(os.path.dirname(of))
    except:
        pass
        
    md = make_md(tmpl)
    xml = make_xml(tmpl)
    
    if os.path.exists(md):
        contents = open(md, encoding='utf-8-sig').read().strip()
    else:
        contents = ""

    with open(of, "w", encoding="utf-8") as f:
        print(parts[-1], file=f)
        print("=" * len(parts[-1]), file=f)
        print(file=f)
        print(contents, file=f)
        
        parent_child = defaultdict(list)
            
        def visit(parent, r):           
            if r['#tag'] == "DocTemplateDefinition" or r['#tag'] == "Reference" or r['#tag'] == "Value" or r['#tag'] == "DocModelRuleConstraint":
                # @todo
                return
                
            name = r['@Name']
            if r['#tag'] == "DocModelRuleAttribute":
                name = parent + "." + name
            parent_child[parent].append(name)
            for x in r.get('_children', []):
                for c in x.get('_children', []):
                    visit(name, c)
                    
        
        # import pdb; pdb.set_trace()
        doc = read(xml)
        rules = [c for c in doc.get('_children', []) if c['#tag'] == 'Rules']
        if rules:
            root = doc.get('@Type')
            entity_defs = set()
            print(file=f)
            print("```", file=f)
            print("concept {", file=f)
            
            for c in rules[0].get('_children', []):
                visit(root, c)
                
            for k, vs in list(parent_child.items()):
                if '.' not in k:
                    for v in vs:
                        for v2 in parent_child[v]:
                            entity_defs.add(k)
                            entity_defs.add(v2)
                            
                            print("   ", v.replace(".", ":"), "->", (v2 + reverse_attr(v)).replace(".", ":"), file=f)
                                
            print("}", file=f)
            print("```", file=f)
        