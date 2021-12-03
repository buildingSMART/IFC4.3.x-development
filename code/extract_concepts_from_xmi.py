import os
import sys
import json
import re
import glob

from collections import defaultdict

import express
from xmi_document import xmi_document
from concept_extractor import extractor

try:
    fn = sys.argv[1]
except:
    fn = os.path.join(os.path.dirname(__file__), '..', 'schemas', 'IFC.xml')

xmi_doc = xmi_document(fn)
# ctx = extractor("../mvdXML/IFC4_ADD2.mvdxml")

definitions = list(xmi_doc)
definitions_by_name = {x.name: x for x in definitions}
entities = [e for e in definitions if e.type == "ENTITY"]
name_to_id = {c.name: c.id for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Class"]}

def get_predefined_types_enum(e):
    # can be an xmi_item in case of selects, otherwise express definition
    vs = e.values if hasattr(e, 'values') else e.definition.values
    for nm in vs:
        yield f"{e.name}.{nm}"

def get_predefined_types_for_entity(e):
    if "PredefinedType" in dict(e.definition.attributes):
        type_attr = dict(e.definition.attributes)["PredefinedType"]
        type_name = type_attr.split(" ")[-1]
        type_def = definitions_by_name[type_name].definition
        type_optional = "OPTIONAL" in type_attr
        if isinstance(type_def, express.select):
            for option in type_def.values:
                yield from get_predefined_types_enum(definitions_by_name[option])
        else:
            yield from get_predefined_types_enum(type_def)

result = defaultdict(list)

all_templates = glob.glob(os.path.join(os.path.dirname(fn), "../docs/templates/**/*.md"), recursive=True)
  
    
def flatten(iterable):
    if isinstance(iterable, (list, tuple)):
        for x in iterable:
            yield from flatten(x)
    else:
        yield iterable


def get_all_attributes(nm):
    d = dict(definitions_by_name[nm].definition.attributes)
    for inv in definitions_by_name["IfcObject"].definition.inverses:
        k,v = inv.split(" : ")
        k = k.strip()
        v = re.findall('OF (\w+)', v)[0]
        d[k] = v
    st = definitions_by_name[nm].definition.supertype
    if st:
        d.update(get_all_attributes(st))
    return d


def parse_bindings(concept):
    tmpl = [t for t in all_templates if os.path.abspath(t).split(os.sep)[-2].lower().replace(" ", "") == concept.lower()][0]
    concept_block = re.findall(r"concept\s*\{.+?\}", open(tmpl, encoding='utf-8').read(), flags=re.S)[0]
    for a,b,c in re.findall(r'(\w+):(\w+)\[binding="(.+?)"\]', concept_block):
        t = get_all_attributes(a).get(b).replace("OPTIONAL ", "")
        yield c, (a,b), xmi_doc.xmi.by_id[definitions_by_name[t].id]
    

def yield_supertypes(a):
    yield a
    try:
        yield from yield_supertypes(xmi_doc.xmi.by_id[(a | "generalization").general])
    except: pass


for xmi_concept, v in xmi_doc.concepts.items():
    for e in entities:
        
        # mvd_concept = [k for k in ctx.grouping.keys() if k[0].replace(" ", "") == xmi_concept][0]
        
        if xmi_concept == "PropertySetsforObjects":
            # binding_names = [x[0] for x in mvd_concept[1:]] 
            binding_names = "ApplicableEntity", "PredefinedType", "PsetName"
            if e.id in v:
                for binding in v[e.id]:
                    if not isinstance(binding, tuple):
                        # @todo investigate
                        binding = (binding,)
                    others = list(map(xmi_doc.xmi.by_id.__getitem__, binding))
                    result[xmi_concept].append(dict(zip(binding_names, [e.name, "", others[0].name])))
                        
            for pt in get_predefined_types_for_entity(e):
                if name_to_id.get(pt) and name_to_id.get(pt) in v:
                    for binding in v[name_to_id.get(pt)]:
                        if not isinstance(binding, tuple):
                            # @todo investigate
                            binding = (binding,)
                        others = list(map(xmi_doc.xmi.by_id.__getitem__, binding))
                        result[xmi_concept].append(dict(zip(binding_names, [e.name, pt.split(".")[1], others[0].name])))
                    
for xmi_concept, pairs in xmi_doc.concept_associations.items():
    if xmi_concept == "ObjectTyping":
        bindings = list(parse_bindings(xmi_concept))
        
        for p in pairs:
            elems = tuple(map(xmi_doc.xmi.by_id.__getitem__, p))
            
            def get_binding(el):
                for nm, attr, nd in bindings:
                    if nd in set(yield_supertypes(el)):
                        return nm
                        
            elem_binds = list(map(get_binding, elems))
            
            # a single element should not be bound, that is the ApplicableEntity
            assert len([x for x in elem_binds if x is None]) == 1
            elem_binds[elem_binds.index(None)] = "ApplicableEntity"
            
            binding_names = ["ApplicableEntity"] + [b[0] for b in bindings if b[0] in elem_binds]
            elem_names = [e.name for e in elems]
            d = {x: elem_names[elem_binds.index(x)] for x in binding_names}
            
            result[xmi_concept].append(d)

json.dump(result, open("xmi_concepts.json", "w", encoding="utf-8"), indent=1)
