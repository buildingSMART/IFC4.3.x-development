import os
import sys
import json

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

json.dump(result, open("xmi_concepts.json", "w", encoding="utf-8"), indent=1)
