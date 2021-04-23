import os
import sys
import json

from collections import defaultdict

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from xmi_document import xmi_document

fn = os.path.join(os.path.dirname(__file__), '..', 'schemas', 'IFC.xml')
xmi_doc = xmi_document(fn)

entity_to_package = {}

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

def get_schema(name):
    for cat, schemas in hierarchy:
        for schema_name, members in schemas:
            if schema_name == name: return members
    import pdb; pdb.set_trace()

for item in xmi_doc:
    if item.type == "ENTITY":
        entity_to_package[item.name] = item.package
        get_schema(item.package)['Entities'].append(item.name)
        if item.definition.supertype:
            supertype[item.name] = item.definition.supertype
            subtypes[item.definition.supertype].append(item.name)
        else:
            roots.append(item.name)
    elif item.type in ("TYPE", "SELECT", "ENUM"):
        get_schema(item.package)['Types'].append(item.name)
        
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
