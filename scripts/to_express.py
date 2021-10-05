import sys
import logging

from collections import defaultdict

import express
from xmi_document import xmi_document, SCHEMA_NAME

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

# The order in which definitions are to appear in the Express schema
EXPRESS_ORDER=("TYPE", "ENUM", "SELECT", "ENTITY", "FUNCTION", "RULE")

try:
    fn = sys.argv[1]
    try:
        OUTPUT = open(sys.argv[2], "w", encoding='utf-8')
    except IndexError as e:
        OUTPUT = sys.stdout
except:
    print("Usage: python to_express.py <schema.xml>", file=sys.stderr)
    exit()

            
def sort_key(tup):
    return (EXPRESS_ORDER.index(tup.type), express.ifc_name(tup.name))


"""
schema_name = self.xmi.by_tag_and_type["packagedElement"]['uml:Package'][1].name.replace("exp", "").upper()
schema_name = "".join(["_", c][c.isalnum()] for c in schema_name)
schema_name = re.sub(r"_+", "_", schema_name)
"""

print("SCHEMA %s;" % SCHEMA_NAME, file=OUTPUT)
print(file=OUTPUT)

emitted = set()

xdoc = xmi_document(fn)

definitions = sorted((x for x in xdoc if x.type in EXPRESS_ORDER), key=sort_key)
definitions_by_name = {x.name: x for x in definitions}

supertypes = {}
for x in definitions:
    if x.type == "ENTITY":
        supertypes[x.name] = x.definition.supertype
        
        
def is_subclass_of(nm, supert):
    return nm == supert or (supertypes.get(nm) and is_subclass_of(supertypes.get(nm), supert))


def has_where_rule(nm, wr, inherited=True):
    itm = definitions_by_name[nm]
    clauses = dict(itm.definition.where_clauses)
    return wr in clauses or (inherited and (supertypes.get(nm) and has_where_rule(supertypes.get(nm), wr)))


for itm in definitions:
    if (itm.type, itm.name) in emitted:
        logging.warning("duplicate definition for %s %s", itm.type, itm.name)
        continue
        
    # add two where rules
    # @todo we should probably move this to xmi_document
    
    
    is_occurence=is_subclass_of(itm.name, "IfcElement") or is_subclass_of(itm.name, "IfcSystem") or is_subclass_of(itm.name, "IfcSpatialStructureElement")
    is_type = is_subclass_of(itm.name, "IfcElementType")
    if is_type or is_occurence:
        if "PredefinedType" in dict(itm.definition.attributes):
            type_attr = dict(itm.definition.attributes)["PredefinedType"]
            type_name = type_attr.split(" ")[-1]
            type_def = definitions_by_name[type_name].definition
            type_optional = "OPTIONAL" in type_attr
            attr = "IfcElementType.ElementType" if is_type else "IfcObject.ObjectType"
            if not has_where_rule(itm.name, "CorrectPredefinedType"):
                if isinstance(type_def, express.select):
                    clause_1 = "NOT(EXISTS(PredefinedType))"
                    clause_2 = "(%s)" % " AND ".join("(PredefinedType <> %s.USERDEFINED)" % v for v in type_def.values)
                    clause_3 = " OR ".join("(PredefinedType = %s.USERDEFINED)" % v for v in type_def.values)
                    clause_3 = "((%(clause_3)s) AND EXISTS(SELF\\%(attr)s))" % locals()
                    clauses = (clause_1, clause_2, clause_3)
                    if not type_optional:
                        clauses = clauses[1:]
                    rule = " OR ".join(clauses)
                else:
                    clause_1 = "NOT(EXISTS(PredefinedType)) OR\n " if type_optional else ''
                    rule = clause_1 + "(PredefinedType <> %(type_name)s.USERDEFINED) OR\n ((PredefinedType = %(type_name)s.USERDEFINED) AND EXISTS (SELF\\%(attr)s))" % locals()
                itm.definition.where_clauses += [("CorrectPredefinedType", rule)]
        if itm.name + "Type" in definitions_by_name:
            itm_type=definitions_by_name[itm.name+"Type"]
            if "PredefinedType" in dict(itm_type.definition.attributes):
                if not has_where_rule(itm.name, "CorrectTypeAssigned", inherited=False):
                    itm.definition.where_clauses += [("CorrectTypeAssigned", "(SIZEOF(IsTypedBy) = 0) OR\n  ('%(schema_name)s.%(entity_name_upper)sTYPE' IN TYPEOF(SELF\\IfcObject.IsTypedBy[1].RelatingType))" % {'schema_name': SCHEMA_NAME, 'entity_name_upper': itm.name.upper()})]
            
    emitted.add((itm.type, itm.name))
    print(itm.definition, file=OUTPUT)
    print(file=OUTPUT)

print("END_SCHEMA;", file=OUTPUT)
