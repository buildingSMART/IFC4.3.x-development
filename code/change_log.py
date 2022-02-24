
import re
import ast
from deepdiff import DeepDiff

from collections import defaultdict

from xmi_document import fix_schema_name

changes_by_schema = []
changes_by_type = defaultdict(dict)

def to_dict(decl):
    if type(decl).__name__ == "EntityDeclaration":
        def format_attribute(attr):
            return {
                # 'type': 'attribute',
                'name': attr.name,
                'is_optional': attr.optional,
                'definition': str(attr.type)
            }
            
        def format_inverse(attr):
            name, definition = list(map(str.strip, str(decl.inverse[1]).split(":", 1)))
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
            'unique_rules': [format_rule(a, 'unique_rule') for a in decl.unique]
        }
    else:
        print(type(decl))
        
def compare(e0, e1):
    dd0, dd1 = map(to_dict, (e0, e1))
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
    
def compare_schemas(s0, s1):
    s0e, s1e = map(lambda m: set(map(str, m.schema.entities.keys())), (s0, s1))
    for nm in s0e - s1e:
        yield (nm, "deleted", "", "")
    for nm in s1e - s0e:
        yield (nm, "added", "", "")
    for nm in s0e & s1e:
        yield from compare(s0.schema.entities[nm], s1.schema.entities[nm])

if __name__ == "__main__":
    import os
    import sys
    import json
    import operator
    import itertools
    import functools
    
    from ifcopenshell.express import express_parser
    
    try:
        repo_dir = sys.argv[1]
    except:
        repo_dir = os.path.join(os.path.dirname(__file__), "..")

    d = os.path.join(repo_dir, "reference_schemas")
    names = [
        "IFC2X3_TC1.exp",
        "IFC4_ADD2_TC1.exp",
        "IFC4x1.exp",
        "IFC4x2.exp",
        "IFC4x3_RC3.exp"
    ]
    files = map(functools.partial(os.path.join, d), names)
    schemas = list(map(express_parser.parse, files))
    
    for a, b in zip(schemas[:-1], schemas[1:]):
        differences = sorted(compare_schemas(a, b))
        changes_by_schema.append((b.schema.name, differences))
        
        for ty, changes in itertools.groupby(differences, key=operator.itemgetter(0)):
            changes_by_type[ty][b.schema.name] = [x[1:] for x in changes]
    
    json.dump(changes_by_schema, open("changes_by_schema.json", "w"), indent=2)
    json.dump(changes_by_type, open("changes_by_type.json", "w"), indent=2)
 
