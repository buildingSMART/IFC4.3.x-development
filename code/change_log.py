import os
import re
import ast
from deepdiff import DeepDiff

from collections import defaultdict
from xmi_document import fix_schema_name

changes_by_schema = []
changes_by_type = defaultdict(dict)

is_iso = os.environ.get('ISO', '0') == '1'

def to_dict(decl, depr=[]):
    if type(decl).__name__ == "EntityDeclaration":
        def format_attribute(attr):
            return {
                # 'type': 'attribute',
                'name': attr.name,
                'is_optional': attr.optional,
                'definition': str(attr.type)
            }
            
        def format_inverse(attr):
            name, definition = list(map(str.strip, str(attr).split(":", 1)))
            return {
                # 'type': 'inverse_attribute',
                'name': name,
                'definition': definition
            }
            
        def format_rule(rl, type):
            return {
                # 'type': type,
                'name': rl[0],
                'definition': fix_schema_name(rl[1], remove=True)
            }
    
        return {
            'type': 'entity',
            'name': decl.name,
            'supertype': decl.subtype.super_type if decl.subtype else None,
            'abstract': decl.abstract,
            'attributes': [format_attribute(a) for a in decl.attributes],
            'inverses': [format_inverse(a) for a in decl.inverse[1:]],
            'derived': [format_rule(a, 'derived_attribute') for a in (decl.derived or [])],
            'where_rules': [format_rule(a, 'where_rule') for a in decl.where],
            'unique_rules': [format_rule(a, 'unique_rule') for a in decl.unique],
            'deprecated': decl.name in depr
        }
    else:
        print(type(decl))
        
def compare(depr0, depr1, e0, e1):
    depr0, depr1 = map(lambda fn: json.load(open(fn)), (depr0, depr1))
    dd0, dd1 = map(to_dict, (e0, e1), (depr0, depr1))
    
    result = DeepDiff(dd0, dd1, ignore_order=True, cutoff_intersection_for_pairs=0.5)
    for i, (ke, lbl) in enumerate([("iterable_item_added", "additions"), ("values_changed", "modifications"), ("iterable_item_removed", "deletions")]):
        di = result.to_dict().get(ke, {})
        for k, v in di.items():
            path = list(map(ast.literal_eval, re.findall(r"\[(.+?)\]", k)))
            if lbl in ("additions", "deletions") and isinstance(path[-1], int):
                path = path[:-1]
            for pi, pp in list(enumerate(path)):
                if isinstance(pp, int):
                    path[pi] = dd0[path[pi - 1]][pp]['name']
            path = list(map(str, path))
            if lbl == "modifications" and path[0] == "where_rules" and isinstance(v['new_value'], dict) and v['new_value'].keys() == {'name', 'definition'}:
                yield (e0.name, "deletions", "where_rules", v['old_value']['name'])
                yield (e0.name, "additions", "where_rules", v['new_value']['name'])
            else:
                if isinstance(v, dict) and v.keys() == {'old_value', 'new_value'}:
                    a, b = v['old_value'], v['new_value']
                    if all(map(lambda x: isinstance(x, dict), v.values())):
                        for vk in a.keys() | b.keys():
                            if a.get(vk) != b.get(vk):
                                yield (e0.name, lbl, " ".join(path + [vk]), "Changed from %s to %s" % (a.get(vk), b.get(vk)))
                    else:
                        yield (e0.name, lbl, " ".join(path), "Changed from %s to %s" % (a, b))
                else:
                    if lbl in ("additions", "deletions"):
                        v = v['name']
                    yield (e0.name, lbl, " ".join(path), v)
    
def compare_schemas(s0, depr0, s1, depr1):
    s0e, s1e = map(lambda m: set(map(str, m.schema.entities.keys())), (s0, s1))
    for nm in s0e - s1e:
        yield (nm, "deleted", "", "")
    for nm in s1e - s0e:
        yield (nm, "added", "", "")
    for nm in s0e & s1e:
        yield from compare(depr0, depr1, s0.schema.entities[nm], s1.schema.entities[nm])

def pset_to_dict(D):
    appl = sorted(set([x.text for x in D.child_with_tag("ApplicableClasses").children]))

    props = []
    for p in (D.child_with_tag("PropertyDefs") or D.child_with_tag("QtoDefs")).children:
        pname = p.child_with_tag("Name").text
        if p.tag == "PropertyDef":
            pnode = p.child_with_tag("PropertyType").children[0]
            ptype = pnode.tag
            ptype = ptype.replace("TypeProperty", "").replace("Value", "").lower()
            try:
                if ptype in ("single", "bounded"):
                    pvalue = pnode.children[0].attributes['type']
                elif ptype == "enumerated":
                    pvalue = pnode.children[0].attributes['name']
                elif ptype == "reference":
                    pvalue = pnode.attributes['reftype']
                elif ptype == "list":
                    pvalue = pnode.children[0].children[0].attributes['type']
                elif ptype == "table":
                    pvalue = " ".join([pnode.child_with_tag(x).children[0].attributes["type"] for x in ["DefiningValue", "DefinedValue"]])
                elif ptype == "typesimpleproperty":
                    # weird 2x3 anomaly
                    ptype = "reference"
                    pvalue = pnode.children[0].attributes['type']
                elif ptype == "typecomplexproperty":
                    ptype = "complex"
                    pvalue = pnode.attributes['name']
                else:
                    raise RuntimeError(f"{ptype} not implemented")
            except:
                pvalue = "invalid"
        else:
            ptype = p.child_with_tag("QtoType").text
            pvalue = None
            if not ptype:
                ptype = "invalid"
        props.append((pname, " ".join(filter(None, (ptype, pvalue)))))
        
    return {
        'name': D.child_with_tag("Name").text,
        'applicability': appl,
        'properties': props
    }

def compare_pset(fn0, fn1):
    import xml_dict
    d0d1 = list(map(pset_to_dict, map(xml_dict.xml_node.strip_namespaces, map(xml_dict.read, (fn0, fn1)))))
    
    pset = d0d1[0]['name']
    
    appl0, appl1 = map(set, map(operator.itemgetter('applicability'), d0d1))
    for nm in appl0 - appl1:
        yield (pset, "deleted", "applicability", nm)
    for nm in appl1 - appl0:
        yield (pset, "added", "applicability", nm)
 
    prop0, prop1 = map(dict, map(operator.itemgetter('properties'), d0d1))
    for nm in prop0.keys() - prop1.keys():
        yield (pset, "deleted", "property", nm)
    for nm in prop1.keys() - prop0.keys():
        yield (pset, "added", "property", nm)
    for nm in prop0.keys() & prop1.keys():
        v0, v1 = prop0[nm], prop1[nm]
        if v0 != v1:
            yield (pset, "modifications", f"property {nm}", f"Changed from {v0} to {v1}")

def compare_psets(dir0, dir1):
    p0, p1 = map(set, map(sorted, map(lambda li: [s.lower() for s in li], map(os.listdir, (dir0, dir1)))))
    case0, case1 = ({fn.lower():fn for fn in os.listdir(d)} for d in (dir0, dir1))
    
    for nm in p0 - p1:
        yield (case0[nm][:-4], "deleted", "", "")
    for nm in p1 - p0:
        yield (case1[nm][:-4], "added", "", "")
    for nm in p0 & p1:
        yield from compare_pset(os.path.join(dir0, case0[nm]), os.path.join(dir1, case1[nm]))
            

if __name__ == "__main__":
    import os
    import sys
    import json
    import operator
    import itertools
    import functools
    
    from ifcopenshell.express import express_parser
    
    repo_dir = None
    
    if len(sys.argv) == 2:    
        repo_dir = sys.argv[1]
    elif len(sys.argv) == 3:
        files = sys.argv[1:]
    else:
        repo_dir = os.path.join(os.path.dirname(__file__), "..")

    if repo_dir:
        d = os.path.join(repo_dir, "reference_schemas")
        names = [
                "IFC2X3_TC1.exp", "deprecated_entities_Ifc2.3.0.1.json", "psd_IFC2x3",
                "IFC4_ADD2_TC1.exp", "deprecated_entities_Ifc4.0.2.2.json", "psd_IFC4_ADD2_TC1",
        ]
        
        if not is_iso:
            names += [
                # no IfcDoc branch for 4x1
                "IFC4x1.exp", "deprecated_entities_Ifc4.0.2.2.json", "psd_IFC4x1",
                "IFC4x2.exp", "deprecated_entities_Ifc4.2.0.1.json", "psd_IFC4x2"
            ]
            
        files = list(map(functools.partial(os.path.join, d), names))
        files += [
            "IFC.exp",
            "deprecated_entities.json",
            "psd",
        ]

    specs = [[express_parser.parse(files[i]), *files[i+1:i+3]] for i in range(0, len(files), 3)]
    
    for (schema_a, depr_a, psd_a), (schema_b, depr_b, psd_b) in zip(specs[:-1], specs[1:]):
        differences = sorted(compare_schemas(schema_a, depr_a, schema_b, depr_b)) \
            + sorted(compare_psets(psd_a, psd_b))
            
        schema_name = schema_b.schema.name.replace("X", ".")
        
        changes_by_schema.append((schema_name, differences))
        
        for ty, changes in itertools.groupby(differences, key=operator.itemgetter(0)):
            changes_by_type[ty][schema_name] = [x[1:] for x in changes]
    
    json.dump(changes_by_schema, open("changes_by_schema.json", "w"), indent=2)
    json.dump(changes_by_type, open("changes_by_type.json", "w"), indent=2)
