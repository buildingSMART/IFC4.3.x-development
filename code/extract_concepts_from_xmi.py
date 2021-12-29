import os
import sys
import json
import re
import glob

from collections import defaultdict

import express
import concept_interpretation
from xmi_document import xmi_document
from concept_extractor import extractor


class predefined_type_attribute: pass

class property_set_class: pass


def is_no_concept_node(n):
    """
    The SIMPLE_UNARY concept type is based on a uml:Class
    that is part of the uml:Package for this concept, which
    is then associated to schema classes.
    """
    # @todo check whether is part of enum
    return n.parent.parent.parent.name != "Views"


def parse_bindings(fn, concept, to_xmi=False, definitions_by_name=None):
    all_templates = glob.glob(os.path.join(os.path.dirname(fn), "../docs/templates/**/*.md"), recursive=True)                    
    tmpl = [t for t in all_templates if os.path.abspath(t).split(os.sep)[-2].lower().replace(" ", "") == concept.lower()][0]
    concept_blocks = re.findall(r"concept\s*\{.+?\}", open(tmpl, encoding='utf-8').read(), flags=re.S)
    if not concept_blocks:
        print(f"Warning: no concept block on {concept}")
        return
    
    concept_block = concept_blocks[0]
    for a,b,c in re.findall(r'(\w+):(\w+)\[binding="(.+?)"\]', concept_block):
        
        if to_xmi:
            t = get_all_attributes(a).get(b, '').replace("OPTIONAL ", "").replace("UNIQUE ", "")
            if (a,b) in [('IfcPropertySet', 'Name'), ('IfcElementQuantity', 'Name')]:
                # In UML we have property sets as defined classes, which in
                # IFC are fully late-bound type definitions. Selection of the
                # appropriate psets happens through Name, which is IfcLabel
                # which will match the (p|q)set class name in UML.
                type_node = property_set_class()
            elif not t and b == "PredefinedType":
                # PredefinedType is not really an attribute with a specific
                # type in the sense that all entities define their own version
                # of the attribute and there isn't a general basis for all
                # enumerations.
                type_node = predefined_type_attribute()
            else:
                if " OF " in t:
                    # strip off aggregate information
                    t = t.split(" OF ")[1]
                type_node = xmi_doc.xmi.by_id[definitions_by_name[t].id]
            
            yield c, (a,b), type_node
            
        else:
            if b == "PredefinedType":
                yield c, ('', '')
            else:
                yield c, (a,b)
    

    
if __name__ == "__main__":

    try:
        fn = sys.argv[1]
    except:
        fn = os.path.join(os.path.dirname(__file__), '..', 'schemas', 'IFC.xml')

    xmi_doc = xmi_document(fn)

    definitions = list(xmi_doc)
    definitions_by_name = {x.name: x for x in definitions}
    
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
                

    def get_predefined_types_enum(e):
        # can be an xmi_item in case of selects, otherwise express definition
        vs = e.values if hasattr(e, 'values') else e.definition.values
        for nm in vs:
            yield f"{e.name}.{nm}"


    def yield_supertypes_items(a):
        yield a
        try:
            yield from yield_supertypes_items(definitions_by_name[a.definition.supertype])
        except: pass


    def get_predefined_type_listing(items):
        return dict((e.node.idref, [name_to_node[x] \
        for x in get_predefined_types_for_entity(e)]) for e in items if list(get_predefined_types_for_entity(e)))
        

    def get_all_attributes(nm):
        # In the concept instance diagram, class names may be postfixed
        # with _\d to allow for multiple instances of the same type. When
        # looking up attributes this postfix needs to be removed.
        nm = nm.split("_")[0]
        
        
        d = dict(definitions_by_name[nm].definition.attributes)
        for inv in definitions_by_name[nm].definition.inverses:
            k,v = inv.split(" : ")
            k = k.strip()
            # Either take first symbol after OF, or just first symbol
            # when the inverse attribute is not of type aggregate
            v = (re.findall('OF (\w+)', v) + v.split(" "))[0]
            d[k] = v
        st = definitions_by_name[nm].definition.supertype
        if st:
            d.update(get_all_attributes(st))
        return d


    def yield_supertypes(a):
        yield a
        try:
            yield from yield_supertypes(xmi_doc.xmi.by_id[(a | "generalization").general])
        except: pass


    def make_get_binding(bindings):
        def inner(el):
            for nm, attr, nd in bindings:
                if isinstance(nd, predefined_type_attribute):
                    if el.id in all_predtype_ids:
                        return nm
                elif isinstance(nd, property_set_class):
                    if el.id in psets_and_qsets:
                        return nm
                elif nd in set(yield_supertypes(el)):
                    return nm
        return inner

    non_type_definitions = [x for x in definitions if definitions_by_name["IfcObject"] in yield_supertypes_items(x)]

    entities = [e for e in definitions if e.type == "ENTITY"]
    name_to_node = {c.name: c for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Class"]}
    name_to_id = {c.name: c.id for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Class"]}

    # @nb this includes qsets in the xmi_document iteration,
    #     where qsets are a separate stereotype within pset
    psets_and_qsets = set(n.node.idref for n in definitions if n.type == 'PSET')

    entity_to_predtypes = get_predefined_type_listing(entities)
    all_predtypes = sum(entity_to_predtypes.values(), [])
    all_predtype_ids = set(x.id for x in all_predtypes)

    predtype_to_entity = dict((v.id, k) for k, vs in entity_to_predtypes.items() for v in vs)

    # proritize predtype->entity mappings for the subtypes of ifcobject as opposed to ifctypeobject
    entity_to_predtypes_non_type = get_predefined_type_listing(non_type_definitions)
    predtype_to_entity_non_type = dict((v.id, k) for k, vs in entity_to_predtypes_non_type.items() for v in vs)
    predtype_to_entity.update(predtype_to_entity_non_type)

    result = defaultdict(list)
                        
    for xmi_concept, pairs in xmi_doc.concept_associations.items():
        if concept_interpretation.get(xmi_concept) in (
            concept_interpretation.concept_type.PROPERTY_OR_QUANTITY_SET,
            concept_interpretation.concept_type.OBJECT_TYPING,
            concept_interpretation.concept_type.DIRECTIONAL_GROUPED,
            concept_interpretation.concept_type.SIMPLE_UNARY,
        ):
            bindings = list(parse_bindings(fn, xmi_concept, to_xmi=True, definitions_by_name=definitions_by_name))
            get_binding = make_get_binding(bindings)
            
            for p in pairs:
                elems = tuple(filter(is_no_concept_node, map(xmi_doc.xmi.by_id.__getitem__, p)))
                
                if len(elems) == 1:
                    # If we have a single element, we already know it's the ApplicableEntity,
                    # continuing with the binding process may cause false matches.
                    elem_binds = [None]
                else:
                    elem_binds = list(map(get_binding, elems))
                
                predtype_bind = all_predtype_ids & set(e.id for e in elems)
                if concept_interpretation.get(xmi_concept) == concept_interpretation.concept_type.PROPERTY_OR_QUANTITY_SET and predtype_bind:
                    # when binding to a predefined type, we can infer the ApplicableEntity
                    elem_binds.append(None)
                    elems += (xmi_doc.xmi.by_id[predtype_to_entity[next(iter(predtype_bind))]],)
                    
                # a single element should not be bound, that is the ApplicableEntity
                assert len([x for x in elem_binds if x is None]) == 1
                elem_binds[elem_binds.index(None)] = "ApplicableEntity"
                
                binding_names = ["ApplicableEntity"] + [b[0] for b in bindings if b[0] in elem_binds]
                elem_names = [e.name for e in elems]
                d = {x: elem_names[elem_binds.index(x)] for x in binding_names}
                
                result[xmi_concept].append(d)


    json.dump(result, open("xmi_concepts.json", "w", encoding="utf-8"), indent=1)
