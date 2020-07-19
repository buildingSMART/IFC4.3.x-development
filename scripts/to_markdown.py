import os
import re
import sys
import html
import shutil

import html2text
import tabulate

import xmi
import express

try:
    fn = sys.argv[1]
    output = sys.argv[2]
except:
    print("Usage: python to_markdown.py <schema.xml> <output_dir>", file=sys.stderr)
    exit()

xmi_doc = xmi.doc(fn)
bfn = os.path.basename(fn)

if os.path.exists(output):
    shutil.rmtree(output)
    
os.makedirs(output)

schema_name = xmi_doc.by_tag_and_type["packagedElement"]['uml:Package'][1].name.replace("exp", "").upper()
schema_name = "".join(["_", c][c.isalnum()] for c in schema_name)
schema_name = re.sub(r"_+", "_", schema_name)
schema_name = schema_name.strip('_')

def format(s):
    return html2text.html2text(s.replace('\n', '<br>').replace("$inet://", "").replace("../../../../../../", ""))

def process(node):
    node_name = express.ifc_name(node.name)
    if "(" in node_name:
        import pdb; pdb.set_trace()
    docs = (node/"properties")[0].documentation
    mdfn = os.path.join(output, node_name + ".md")
    with open(mdfn, 'w', encoding='utf-8') as f:
        print(node_name, file=f)
        print('=' * len(node_name), file=f)
        if docs is not None:
            # import pdb; pdb.set_trace()
            print(format(docs), file=f)
        
        if node.xmi_type == "uml:Class":
            stereotype = (node/"properties")[0].stereotype
            if stereotype is not None: 
                stereotype = stereotype.lower()
            if stereotype not in {"predefinedtype", '$', None} and not stereotype.startswith('pset'):
                attrs = [(
                    la.name, 
                    format((la|"properties").documentation or '')
                ) for la in node/("attribute")]

                if len(attrs):
                    print("Attributes", file=f)
                    print("----------", file=f)
                    print(tabulate.tabulate(attrs, headers=['Attribute', 'Definition'], tablefmt="github"), file=f)
#xmi_doc.by_tag_and_type["element"]["uml:DataType"] + 
for c in \
    xmi_doc.by_tag_and_type["element"]["uml:Class"]:
    
    process(c)
