import sys
import logging

import express
from xmi_document import xmi_document

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

# The order in which definitions are to appear in the Express schema
EXPRESS_ORDER=("TYPE", "ENUM", "SELECT", "ENTITY", "FUNCTION", "RULE")

# @todo schema name is hardcoded and not derived from the XMI package name for now
SCHEMA_NAME = "IFC4X3_RC1"

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

for itm in sorted((x for x in xdoc if x.type in EXPRESS_ORDER), key=sort_key):
    if (itm.type, itm.name) in emitted:
        logging.warning("duplicate definition for %s %s", itm.type, itm.name)
        continue
    emitted.add((itm.type, itm.name))
    print(itm.definition, file=OUTPUT)
    print(file=OUTPUT)

print("END_SCHEMA;", file=OUTPUT)
