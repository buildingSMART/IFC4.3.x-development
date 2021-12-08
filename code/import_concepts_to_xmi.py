import sys
import glob
import operator
import itertools

import xml_dict
import append_xmi
import concept_extractor

from append_xmi import XMI

def norm(v):
    return v.lower().replace(" ", "").replace("_", "")

if __name__ == "__main__":
    fn = sys.argv[1]
    
    ctx = append_xmi.context("..\schemas\IFC.xml")
    try:
        gu_package = ctx.package_by_name("GeneralUsage")
    except:
        ifc_package = ctx.package_by_name("IFC4x3_RC4")
        views_package = ctx.insert(ifc_package, append_xmi.uml_package("Views"))
        gu_package = ctx.insert(views_package, append_xmi.uml_package("GeneralUsage"))
    
    x = concept_extractor.extractor(fn)
    
    realizations = set()
    def v(nd, _):
        if nd.attributes.get(XMI.type) == "uml:Realization":
            realizations.add(frozenset((nd.attributes["supplier"], nd.attributes["client"])))
    ctx._recurse(v)
    
    concept_name = "Spatial Containment"
    concept_name_short = concept_name.replace(" ", "")
    concept_package = ctx.insert(gu_package, append_xmi.uml_package(concept_name_short))
    
    key = [k for k in x.grouping.keys() if k[0] == concept_name][0]
    parameters = key[1:]
    values = x.grouping[key]
    
    itertools.groupby(sorted([v[0:2] for v in values]), key=operator.itemgetter(0))
    mapping = dict([(g, frozenset([vv[1] for vv in vs])) for g, vs in itertools.groupby(sorted([v[0:2] for v in values]), key=operator.itemgetter(0))])
    options = set(mapping.values())
    option_to_class = {}
    
    for opt in options:
        nm = "".join(o[3:] for o in sorted(opt))
        opt_class = append_xmi.uml_class(nm)
        option_to_class[opt] = opt_class
        ctx.insert(concept_package, opt_class)
        for entity in opt:
            ctx.insert(concept_package, append_xmi.uml_association(
                [opt_class.id, ctx.to_id("uml:Class", entity)],
                owners = [None, opt_class.xml]
            ))
            
    for appl, opt in mapping.items():
        ent_class = ctx.to_node[("uml:Class", appl)]
        ctx.insert(concept_package, append_xmi.uml_association(
            [ent_class.attributes[XMI.id], option_to_class[opt].id],
            owners = [None, ent_class]
        ))
        
        
    # Property Sets
    
    concept_name = "Property Sets for Objects"
    concept_name_short = concept_name.replace(" ", "")
    concept_package = ctx.insert(gu_package, append_xmi.uml_package(concept_name_short))
    
    for fn in glob.glob("../reference_schemas/psd/Pset_*.xml"):
        xd = xml_dict.read(fn)
        pset = xd.child_with_tag("Name").text
        appl = [n.text for n in xd.child_with_tag("ApplicableClasses").children]
        
        try:
            pset_id = ctx.to_id("uml:Class", pset)
        except KeyError as e:
            print(f"Undefined pset {pset}")
            continue
            
        for entity in appl:
        
            if "/" in entity:
                if "(" in entity:
                    type_enum = entity.split("/")[1].replace(".)", "").replace("(", "")
                    if type_enum.startswith("."):
                        type_enum = entity.split("/")[0] + type_enum
                else:
                    parts = entity.split("/")
                    type_enum = f"{parts[0]}TypeEnum.{parts[1]}"
                try:
                    ctx.to_id("uml:Class", type_enum)
                    entity = type_enum
                except KeyError as e:
                    print(f"Undefined type enum {type_enum}")
                    entity = parts[0]
    
            try:
                entity_id = ctx.to_id("uml:Class", entity)
            except KeyError as e:
                print(f"Undefined entity {entity}")
                continue
            
            assoc = append_xmi.uml_assoc_class(f"{entity}{concept_name_short}{pset}", (entity_id, pset_id))
            ctx.insert(concept_package, assoc)
    
    
    """
    
    key = [k for k in x.grouping.keys() if k[0] == concept_name][0]
    parameters = key[1:]
    values = x.grouping[key]
    
    for row in values:
        d = dict(zip([p[0] for p in parameters], row[1:]))
        
        if not d.get("PsetName"):
            continue
        
        entity = row[0]
        pset = d.get("PsetName")
        
        if entity == "IfcBuildingElement":
            entity = "IfcBuiltElement"
        
        if d.get("PredefinedType") and d.get("PredefinedType").isupper():
            pdtype = f"{entity}TypeEnum.{d.get('PredefinedType')}"
            try:
                ctx.to_id("uml:Class", pdtype)
                entity = pdtype
            except KeyError as e:
                print(f"Undefined predefined type {pdtype}")
                continue
            
        try:
            entity_id = ctx.to_id("uml:Class", entity)
        except KeyError as e:
            print(f"Undefined entity {entity}")
            continue
            
        try:
            pset_id = ctx.to_id("uml:Class", pset)
        except KeyError as e:
            print(f"Undefined pset {pset}")
            continue            
            
        assoc = append_xmi.uml_assoc_class(f"{entity}{concept_name_short}{pset}", (entity_id, pset_id))
        ctx.insert(concept_package, assoc)

    """
   
    # Axis (3D) Geometry
    axis_geom_package = ctx.insert(gu_package, append_xmi.uml_package("Axis3DGeometry"))
    axis_geom = append_xmi.uml_class("Axis3DGeometry")
    ctx.insert(axis_geom_package, axis_geom)
    
    keys = [k for k in x.grouping.keys() if k[0].startswith("Axis ") and not "2D" in k[0]]
    axis_concepts = x.concept_starting_with("Axis ")
    axis_entities = set(v[0] for v in axis_concepts)
    
    for entity in axis_entities:
        ids = [axis_geom.id, ctx.to_id("uml:Class", entity)]
        assoc = append_xmi.uml_assoc_class(f"{entity}AxisGeometryUsage", ids)
        ctx.insert(axis_geom_package, assoc)
        
        
    # Axis 2D Geometry
    concept_name = "Axis 2D Geometry"
    concept_name_short = concept_name.replace(" ", "")
    concept_package = ctx.insert(gu_package, append_xmi.uml_package(concept_name_short))
    concept_class = append_xmi.uml_class("Axis2DGeometry")
    ctx.insert(concept_package, concept_class)
    
    key = [k for k in x.grouping.keys() if k[0] == concept_name][0]
    axis_concepts = x.grouping[key]
    axis_entities = set(v[0] for v in axis_concepts)
    
    for entity in axis_entities:
        ids = [axis_geom.id, ctx.to_id("uml:Class", entity)]
        assoc = append_xmi.uml_assoc_class(f"{entity}AxisGeometryUsage", ids)
        ctx.insert(axis_geom_package, assoc)
        
        
    # Port Nesting
    concept_name = "Port Nesting"
    concept_name_short = concept_name.replace(" ", "")
    concept_package = ctx.insert(gu_package, append_xmi.uml_package(concept_name_short))
    
    key = [k for k in x.grouping.keys() if k[0] == concept_name][0]
    parameters = key[1:]
    values = x.grouping[key]
    
    parameter_id_mapping = [{} for _ in parameters]
    
    for column_id, ((rule_id, (entity_name, attribute_name)), pmap) in enumerate(zip(parameters, parameter_id_mapping), start=1):

        nd = ctx.to_node[entity_name]
        while True:
            attrs = [ch for ch in nd.children if ch.attributes[XMI.type] == "uml:Property" and ch.attributes['name'] == attribute_name]
            if attrs:
                attr_nodes = [attrs[0]]
                break
            else:
                gens = [ch for ch in nd.children if ch.tag == "generalization"]
                if gens:
                    nd = ctx.to_node[gens[0].attributes['general']]
                else:
                    attr_nodes = None
                    break
                    
        if attr_nodes is None:
        
            def subclasses(x):
                yield x
                for s in ctx.subclasses[x]:
                    yield from subclasses(s)
                    
            scs = list(subclasses(entity_name))
            
            attr_nodes = []
            
            for sc in scs:
                attrs = [ch for ch in ctx.to_node[sc].children if ch.attributes[XMI.type] == "uml:Property" and ch.attributes['name'] == attribute_name]
                if attrs:
                    attr_nodes.append(attrs[0])            
        
        for attr in attr_nodes:
            
            attr_type_id = [ch for ch in attr.children if ch.tag == "type"][0].attributes[XMI.idref]
            attr_type = ctx.to_node[attr_type_id]
            attr_type_name = attr_type.attributes['name']
            
            if attr_type.attributes[XMI.type] == "uml:Enumeration":
            
                enum_values = [ch.attributes['name'] for ch in attr_type.children if ch.tag == "ownedLiteral"]
                for ev in enum_values:
                    full_name = f"{attr_type_name}.{ev}"
                    if full_name in ctx.to_node:
                        vid = pmap[norm(ev)] = ctx.to_node[full_name].attributes[XMI.id]
                        eid = attr_type.attributes[XMI.id]
                        ids = (vid, eid)
                        if frozenset(ids) not in realizations:
                            realizations.add(frozenset(ids))
                            ctx.insert(attr_type.parent, append_xmi.uml_realization(*ids))
                    else:
                        assert attr_type.parent.attributes[XMI.type] == "uml:Package"
                        enum_value_class = append_xmi.uml_class(full_name)
                        ctx.insert(attr_type.parent, enum_value_class)
                        ids = (enum_value_class.id, attr_type.attributes[XMI.id])
                        realizations.add(frozenset(ids))
                        ctx.insert(attr_type.parent, append_xmi.uml_realization(*ids))
                        pmap[norm(ev)] = enum_value_class.id
            
            else:
            
                assert len(attrs) == 1
            
                column = sorted(set(v[column_id] for v in values))
                new_enum = append_xmi.uml_enumeration(f"{concept_name_short}{rule_id}Values", column)
                ctx.insert(concept_package, new_enum)
                for col in column:
                    full_name = f"{concept_name_short}{rule_id}Values.{col}"
                    enum_value_class = append_xmi.uml_class(full_name)
                    ctx.insert(concept_package, enum_value_class)
                    ctx.insert(concept_package, append_xmi.uml_realization(enum_value_class.id, new_enum.id))
                    pmap[norm(col)] = enum_value_class.id

    def lookup_and_warn(i, pmap, p):
        v = pmap.get(norm(p))
        if v is None:
            print(f"Not valid: '{p}' for type {parameters[i][1][0]}.{parameters[i][1][1]} on parameter '{parameters[i][0]}'")
        return v
                
    for row in values:
        entity = row[0]
        params = row[1:]
        ids = list(filter(None, [lookup_and_warn(i, pmap, p) for i, (pmap, p) in enumerate(zip(parameter_id_mapping, params)) if p]))
        ids = [ctx.to_id("uml:Class", entity)] + ids
        assoc = append_xmi.uml_assoc_class(f"{entity}{concept_name_short}Usage", ids, type="uml:Association")
        ctx.insert(concept_package, assoc)
        
        
    # Object Typing
    concept_name = "Object Typing"
    concept_name_short = concept_name.replace(" ", "")
    concept_package = ctx.insert(gu_package, append_xmi.uml_package(concept_name_short))
    
    key = [k for k in x.grouping.keys() if k[0] == concept_name][0]
    parameters = key[1:]
    values = x.grouping[key]
    column_id = list(map(operator.itemgetter(0), parameters)).index("RelatingType") + 1
    for ent_ty in [(row[0], row[column_id]) for row in values]:
        try:
            ids = [ctx.to_id("uml:Class", x) for x in ent_ty]
        except:
            print(f"Undefined entity {ent_ty}")
            continue
        assoc = append_xmi.uml_assoc_class(f"{ent_ty[0]}{concept_name_short}Usage", ids)
        ctx.insert(concept_package, assoc)
        
    ctx.write("..\schemas\IFC_with_concepts.xml")