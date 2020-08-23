import sys
import json

d = json.load(open(sys.argv[1]))
keys = d['Domain']['Classifications'].keys()
children = {c.get('Parent') for c in d['Domain']['Classifications'].values() if c.get('Parent')}
orphans = children - keys
print(*orphans)
assert orphans == {'IfcRoot', 'IfcMaterialDefinition'}
