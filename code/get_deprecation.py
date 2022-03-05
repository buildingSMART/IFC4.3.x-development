import json
import glob
import subprocess
from xml.dom import minidom as xml

branches = ["Ifc2.3.0.1", "Ifc4.0.2.2", "Ifc4.2.0.1"]

def make_get_attribute(nm):
    def inner(node):
        a = node.attributes.get(nm)
        if a:
            return a.value
    return inner
    
get_name = make_get_attribute('Name')
get_status = make_get_attribute('Status')

for branch in branches:
    subprocess.run(["git", "checkout", branch])
    
    def collect():
        for fn in glob.glob("**/Doc*.xml", recursive=True):
            doc = xml.parse(fn)
            if get_status(doc.childNodes[0]) == "Deprecated":
                yield get_name(doc.childNodes[0])

    with open(f"deprecated_entities_{branch}.json", "w") as f:
        json.dump(list(collect()), f)