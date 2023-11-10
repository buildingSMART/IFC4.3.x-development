import sys
import json

d = json.load(open(sys.argv[1]))
roots = {k for k, v in d['Dictionary']['Classes'].items() if not v.get('Parent')}
print("Roots:", *roots)
assert roots == {'IfcRoot', 'IfcMaterialDefinition', 'IfcProfileDef'}

all_pset_names = set()

for k, v in d['Dictionary']['Classes'].items():
    if v.get('Parent') and v.get('Parent') not in d['Dictionary']['Classes'].keys():
        print(k, "has missing parent:", v.get('Parent'))
        assert False
    for pset, props in v.get('Psets', {}).items():
        all_pset_names.add(pset)
        
print("Emitted", len(all_pset_names), "property sets")

# for x in sorted(all_pset_names):
#     print(x)

print("All ok!")