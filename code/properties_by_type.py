import os
import operator

from collections import defaultdict

from compare_pset import read

properties_by_type = defaultdict(list)

def child_by_tag(node, tag):
    return [c for c in node["_children"] if c['#tag'] == tag][0]

def format_TypePropertySingleValue(prop):
    try:
        return prop["_children"][0]["@type"]
    except KeyError as e:
        return ""

def format_TypePropertyEnumeratedValue(prop):
    return " ".join(map(operator.itemgetter("#text"), prop["_children"][0]["_children"]))

def format_TypePropertyTableValue(prop):
    return "/".join((
        child_by_tag(prop, "DefinedValue")["_children"][0]["@type"],
        child_by_tag(prop, "DefiningValue")["_children"][0]["@type"]
    ))

def format_TypePropertyReferenceValue(prop):
    return prop["@reftype"]

def format_TypePropertyListValue(prop):
    return prop["_children"][0]["_children"][0]["@type"]

def format_TypeComplexProperty(prop):
    return " ".join(map(lambda n: child_by_tag(n, "Name")["#text"], prop["_children"]))

format_TypePropertyBoundedValue = format_TypePropertySingleValue

for fn in os.listdir("../reference_schemas/psd"):
    fn = os.path.join("../reference_schemas/psd", fn)
    
    xml = read(fn)

    psetname = child_by_tag(xml, "Name")["#text"]
    try:
        classes = " ".join(map(operator.itemgetter("#text"), child_by_tag(xml, "ApplicableClasses")["_children"]))
    except:
        classes = "-"

    if xml['#tag'] == 'PropertySetDef':
        for prop in child_by_tag(xml, 'PropertyDefs')["_children"]:
            propname = child_by_tag(prop, "Name")["#text"]
            proptypenode = child_by_tag(prop, 'PropertyType')["_children"][0]
            proptype = proptypenode["#tag"]
            proptypeargs = globals()[f"format_{proptype}"](proptypenode)
            proptypeifc = f"Ifc{proptype[4:]}"

            properties_by_type[proptypeifc].append((psetname, classes, propname, proptypeargs))

for k, vs in properties_by_type.items():
    with open(f"{k}.csv", 'w') as f:
        for v in vs:
            print(",".join(v), file=f)