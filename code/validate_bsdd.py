import sys
import json

d = json.load(open(sys.argv[1]))


assert d['DictionaryName'] == "IFC"

assert d['Classes'][0]['Code'] == "IfcActuator"
assert d['Classes'][0]['Definition'][0:60] == "An actuator is a mechanical device for moving or controlling"
assert d['Classes'][0]['ClassProperties'][0]['Code'] == "PositionHistory"
assert d['Classes'][0]['ClassProperties'][0]['Name'] == "Position History"
assert d['Classes'][0]['ClassProperties'][0]['PropertySet'] == "Pset_ActuatorPHistory"
assert d['Classes'][0]['ClassProperties'][3]['Code'] == "ActuatorApplication"
assert d['Classes'][0]['ClassProperties'][3]['Name'] == "Actuator Application"
assert d['Classes'][0]['ClassProperties'][3]['PropertySet'] == "Pset_ActuatorTypeCommon"
assert d['Classes'][0]['ClassProperties'][3]['AllowedValues'][0]['Value'] == "DAMPERACTUATOR"
assert d['Classes'][0]['ClassProperties'][3]['AllowedValues'][0]['Description'] == "Damper Actuator"

# OLD CHECKING:
# roots = {k for k, v in d['Dictionary']['Classes'].items() if not v.get('Parent')}
# print("Roots:", *roots)
# assert roots == {'IfcRoot', 'IfcMaterialDefinition', 'IfcProfileDef'}

# all_pset_names = set()

# for k, v in d['Classes']['Classes'].items():
#     if v.get('Parent') and v.get('Parent') not in d['Dictionary']['Classes'].keys():
#         print(k, "has missing parent:", v.get('Parent'))
#         assert False
#     for pset, props in v.get('Psets', {}).items():
#         all_pset_names.add(pset)
        
# print("Emitted", len(all_pset_names), "property sets")

# for x in sorted(all_pset_names):
#     print(x)



print("All ok!")