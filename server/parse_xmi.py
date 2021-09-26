import os
import sys
import json
import glob
import operator

from collections import defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from xmi_document import xmi_document
from compare_pset import read as read_psd

fn = os.path.join(os.path.dirname(__file__), '..', 'schemas', 'IFC.xml')
xmi_doc = xmi_document(fn)

entity_to_package = {}

#@todo this may need to get revised
hierarchy = [
    ("Core data schemas", [
        ("IfcKernel", defaultdict(list)),
        ("IfcControlExtension", defaultdict(list)),
        ("IfcProcessExtension", defaultdict(list)),
        ("IfcProductExtension", defaultdict(list)), 
    ]),
    ("Shared element data schemas", [
        ("IfcSharedBldgElements", defaultdict(list)),
        ("IfcSharedBldgServiceElements", defaultdict(list)),
        ("IfcSharedComponentElements", defaultdict(list)),
        ("IfcSharedFacilitiesElements", defaultdict(list)),
        ("IfcSharedMgmtElements", defaultdict(list)),
    ]),
    ("Domain specific data schemas", [
        ("IfcArchitectureDomain", defaultdict(list)),
        ("IfcBuildingControlsDomain", defaultdict(list)),
        ("IfcConstructionMgmtDomain", defaultdict(list)),
        ("IfcElectricalDomain", defaultdict(list)),
        ("IfcHvacDomain", defaultdict(list)),
        ("IfcPlumbingFireProtectionDomain", defaultdict(list)),
        ("IfcPortsAndWaterways", defaultdict(list)),
        ("IfcRail", defaultdict(list)),
        ("IfcRoad", defaultdict(list)),
        # @NB this one is XMI but not in the published HTML
        ("IfcSharedInfrastructureElements", defaultdict(list)),
        ("IfcStructuralAnalysisDomain", defaultdict(list)),
        ("IfcStructuralElementsDomain", defaultdict(list)),
    ]),
    ("Resource definition data schemas", [
        ("IfcActorResource", defaultdict(list)),
        ("IfcApprovalResource", defaultdict(list)),
        ("IfcConstraintResource", defaultdict(list)),
        ("IfcCostResource", defaultdict(list)),
        ("IfcDateTimeResource", defaultdict(list)),
        ("IfcExternalReferenceResource", defaultdict(list)),
        ("IfcGeometricConstraintResource", defaultdict(list)),
        ("IfcGeometricModelResource", defaultdict(list)),
        ("IfcGeometryResource", defaultdict(list)),
        ("IfcMaterialResource", defaultdict(list)),
        ("IfcMeasureResource", defaultdict(list)),
        ("IfcPresentationAppearanceResource", defaultdict(list)),
        ("IfcPresentationDefinitionResource", defaultdict(list)),
        ("IfcPresentationOrganizationResource", defaultdict(list)),
        ("IfcProfileResource", defaultdict(list)),
        ("IfcPropertyResource", defaultdict(list)),
        ("IfcQuantityResource", defaultdict(list)),
        ("IfcRepresentationResource", defaultdict(list)),
        ("IfcStructuralLoadResource", defaultdict(list)),
        ("IfcTopologyResource", defaultdict(list)),
        ("IfcUtilityResource", defaultdict(list)),
    ]),
]

supertype = {}
subtypes = defaultdict(list)
roots = []
attributes = {}
definitions = {}
resource_to_package = {}
psets = {}

def get_schema(name):
    for cat, schemas in hierarchy:
        for schema_name, members in schemas:
            if schema_name == name: return members

for item in xmi_doc:
    if item.type == "ENTITY":
        entity_to_package[item.name] = item.package
        resource_to_package[item.name] = get_schema(item.package)
        get_schema(item.package)['Entities'].append(item.name)
        if item.definition.supertype:
            supertype[item.name] = item.definition.supertype
            subtypes[item.definition.supertype].append(item.name)
        else:
            roots.append(item.name)
            
        for a in item.definition.attributes:
            attributes[".".join((item.name, a[0]))] = (True, a[1])
        for a in item.definition.inverses:
            parts = a.split(' ')
            nm = parts[0].strip()
            ty = ' '.join(parts[2:])[:-1]
            attributes[".".join((item.name, nm))] = (False, ty)
        
    elif item.type in ("TYPE", "SELECT", "ENUM"):
        resource_to_package[item.name] = get_schema(item.package)
        get_schema(item.package)['Types'].append(item.name)
        
    if item.type in ("ENTITY", "TYPE", "SELECT", "ENUM"):
        definitions[item.name] = str(item.definition)
        
def child_by_tag(node, tag):
    return [c for c in node["_children"] if c['#tag'] == tag][0]
    
for fn in glob.glob("./psd/*.xml"):
    xml = read_psd(fn)
    
    psetname = child_by_tag(xml, "Name")["#text"]
    try:
        classes = list(map(operator.itemgetter("#text"), child_by_tag(xml, "ApplicableClasses")["_children"]))
    except:
        classes = []

    props = []
    definition = {
        'name': psetname,
        'applicability': classes,
        'properties': props
    }

    if xml['#tag'] == 'PropertySetDef':
        for prop in child_by_tag(xml, 'PropertyDefs').get("_children", []):
            propname = child_by_tag(prop, "Name")["#text"]
            try:
                proptypenode = child_by_tag(prop, 'PropertyType')["_children"][0]
                proptype = proptypenode["#tag"]
                # proptypeargs = globals()[f"format_{proptype}"](proptypenode)
                proptypeifc = f"Ifc{proptype[4:]}"
            except IndexError as e:
                proptypeifc = "INVALID"
            
            props.append({
                'name': propname,
                'type': proptypeifc
            })
            
    if classes:
        cls = classes[0].split("/")[0]
        try:
            resource_to_package[cls]['Property Sets'].append(psetname)
        except KeyError as e:
            pass
            
    psets[psetname] = definition
        
for cat, schemas in hierarchy:
    for schema_name, members in schemas:
        for member_names in members.values():
            member_names.sort()

with open("inheritance_listing.txt", "w") as f:
    def do_print(k, indent=0):
        print(" " * indent + k, file=f)
        for l in sorted(subtypes[k]):
             do_print(l, indent+1)
         
    for x in sorted(roots):
        do_print(x)


json.dump(supertype, open("entity_supertype.json", "w", encoding="utf-8"))
json.dump(entity_to_package, open("entity_to_package.json", "w", encoding="utf-8"))
json.dump(hierarchy, open("hierarchy.json", "w", encoding="utf-8"))
json.dump(attributes, open("entity_attributes.json", "w", encoding="utf-8"))
json.dump(definitions, open("entity_definitions.json", "w", encoding="utf-8"))
json.dump(psets, open("pset_definitions.json", "w", encoding="utf-8"))
