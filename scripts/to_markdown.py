import os
import re
import sys
import html
import shutil
import operator

from collections import namedtuple, defaultdict

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

# @todo also in to_express.py

##########################################################################

assocation_data = namedtuple("assocation_data", ("own_end", "type", "other_end", "asssocation"))
    
# Extract some data from the assocations for use later on
assocations = defaultdict(list)
for assoc in xmi_doc.by_tag_and_type["packagedElement"]["uml:Association"]:
    try:
        c1, c2 = assoc/'ownedEnd'
    except ValueError as e:
        print("encountered exception `%s' on %s" % (e, assoc))
        continue
    t1, t2 = map(lambda c: (c|"type").idref, (c1, c2))
    tv1, tv2 = map(lambda t: xmi_doc.by_id[t].name, (t1, t2))
    cv1, cv2 = map(operator.attrgetter('name'), (c1, c2))
    assocations[tv1].append(assocation_data(c2, xmi_doc.by_id[t2], c1, assoc))
    assocations[tv2].append(assocation_data(c1, xmi_doc.by_id[t1], c2, assoc))
    
##########################################################################

def float_international(s):
    return float(s.replace(',', '.'))

def format(s, cell=False):
    h2t = html2text.HTML2Text()
    S = s.replace('\n', '<br>').replace("$inet://", "").replace("../../../../../../", "../")
    if cell:
        h2t.body_width = 0
        S = S.replace('<br>', '')
    return h2t.handle(S)

def process(node):
    node_name = express.ifc_name(node.name)
    docs = (node/"properties")[0].documentation
    mdfn = os.path.join(output, node_name[3], node_name + ".md")
    if not os.path.exists(os.path.dirname(mdfn)):
        os.makedirs(os.path.dirname(mdfn))
        
    stereotype = (node/"properties")[0].stereotype
    if stereotype is not None: 
        stereotype = stereotype.lower()
        
    if stereotype in {'predefinedtype', 'ptcontainer', '$', 'enumeration', 'propertyset', 'complexproperty'}:
        # @todo handle enumerations and 'ptcontainers'
        return
    if stereotype is not None and (stereotype.startswith('pset') or stereotype.startswith('qto_')):
        return

    with open(mdfn, 'w', encoding='utf-8') as f:
    
        print(node_name, file=f)
        print('=' * len(node_name), file=f)
        if docs is not None:
            print(format(docs), file=f)
            
        if node.xmi_type == "uml:Class":
                
            attrs = [(
                la.name, 
                format((la|"documentation").value or '', cell=True)
            ) for la in node/("attribute")]

            if len(attrs):
                print("Attribute definitions", file=f)
                print("---------------------", file=f)
                print(tabulate.tabulate(attrs, headers=['Attribute', 'Description'], tablefmt="github"), file=f)
                print(file=f)
                
            cs = sorted(node/"constraint", key=lambda cc: float_international(cc.weight))
            cs_names = map(operator.attrgetter('name'), cs)
            cs_names_cells = [[n, ''] for n in cs_names]
            
            if len(cs_names_cells):
                print("Formal Propositions", file=f)
                print("-------------------", file=f)
                print(tabulate.tabulate(cs_names_cells, headers=['Rule', 'Description'], tablefmt="github"), file=f)
                print(file=f)
                
            assoc_names = [tup.own_end.name for tup in assocations[c.name]]
            assoc_names_cells = [[n, ''] for n in assoc_names]
            
            if len(assoc_names_cells):
                print("Associations", file=f)
                print("------------", file=f)
                print(tabulate.tabulate(assoc_names_cells, headers=['Attribute', 'Description'], tablefmt="github"), file=f)
                print(file=f)
            
                    
#xmi_doc.by_tag_and_type["element"]["uml:DataType"] + 
for c in \
    xmi_doc.by_tag_and_type["element"]["uml:Class"]:
    
    process(c)
