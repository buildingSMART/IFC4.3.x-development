import os
import re
import sys
import html
import json

from collections import defaultdict

import xmi

try:
    fn = sys.argv[1]
    try:
        OUTPUT = open(sys.argv[2], "w", encoding='utf-8')
    except IndexError as e:
        OUTPUT = sys.stdout
except:
    print("Usage: python to_po.py <schema.xml>", file=sys.stderr)
    exit()

xmi_doc = xmi.doc(fn)
bfn = os.path.basename(fn)

schema_name = xmi_doc.by_tag_and_type["packagedElement"]['uml:Package'][1].name.replace("exp", "").upper()
schema_name = "".join(["_", c][c.isalnum()] for c in schema_name)
schema_name = re.sub(r"_+", "_", schema_name)
schema_name = schema_name.strip('_')

def yield_parents(node):
    yield node
    if node.parentNode:
        yield from yield_parents(node.parentNode)

def get_path(xmi_node):
    nodes = list(yield_parents(xmi_node.xml))
    def get_name(n):
        if n.attributes:
            v = n.attributes.get('name')
            if v: return v.value
    node_names = [get_name(n) for n in nodes]
    return node_names[::-1]
    
included_packages = set(("IFC 4.2 schema (13.11.2019)", "Common Schema", "IFC Ports and Waterways", "IFC Road", "IFC Rail - PSM"))

def skip_by_package(element):
    return not (set(get_path(xmi_doc.by_id[element.idref])) & included_packages)
    
HTML_TAG_PATTERN = re.compile('<.*?>')
MULTIPLE_SPACE_PATTERN = re.compile(r'\s+')
def strip_html(s):
    S = html.unescape(s or '')
    i = S.find('\n')
    return re.sub(HTML_TAG_PATTERN, '', S)
    
def format(s):
    return re.sub(MULTIPLE_SPACE_PATTERN, ' ', ''.join([' ', c][c.isalnum() or c in '.,'] for c in s)).strip()

def generate_definitions():
    """
    A generator that yields tuples of <a, b> with
    a: location in file
    a: a fully qualifying key as tuple
    b: the documentation string
    """
    make_defaultdict = lambda: defaultdict(make_defaultdict)
    classifications = defaultdict(make_defaultdict)
    data = {
        'Domain': {
            'Name': 'IFC',
            'Version': schema_name,
            
            'Classifications': classifications
        }
    }
    
    class_name_to_node = {}
    
    for c in xmi_doc.by_tag_and_type["element"]["uml:Class"]:
        
        if skip_by_package(c):
            continue
    
        class_name_to_node[c.name] = c
        stereotype = (c/"properties")[0].stereotype
        if stereotype is not None: 
            stereotype = stereotype.lower()  
        if stereotype and stereotype.startswith("pset"):
            pset_name = c.name
            try:
                class_idref = (c|"links"|"Realisation").start
            except ValueError as e:
                print("WARNING:", pset_name, "has no associated class", file=sys.stderr)
                continue

            class_ = xmi_doc.by_id[class_idref]
            class_name = class_.name
            class_element = [e for e in xmi_doc.by_idref[class_idref] if e.xml.tagName == 'element'][0]
            class_stereotype = (class_element/"properties")[0].stereotype
            
            # Lookup enum value -> enum type -> associated type entity -> associated entity
            if class_stereotype == 'PredefinedType':
                assert "." in class_name
                enum, class_name = class_name.split('.')
                enum_types = [x for x in xmi_doc.by_tag_and_type["element"]["uml:Class"] if x.name == enum]
                if len(enum_types) != 1:
                    print("Warning: ", enum_types, class_)
                    continue
                enum_id = enum_types[0].idref
                type_refs = []
                for assoc in xmi_doc.by_tag_and_type["packagedElement"]["uml:Association"]:
                    try:
                        c1, c2 = assoc/'ownedEnd'
                    except ValueError as e:
                        # print("encountered exception `%s' on %s" % (e, assoc))
                        continue
                    assoc_type_refs = set(map(lambda c: (c|"type").idref, (c1, c2)))
                    if enum_id in assoc_type_refs:
                        other_idref = list(assoc_type_refs - {enum_id})[0]
                        type_refs.append(xmi_doc.by_id[other_idref].name)
                # @todo filter this based on inheritance hierarchy
                type_refs_without_type = [s for s in type_refs if 'Type' not in s][0]
                classifications[class_name]['Parent'] = type_refs_without_type
                
            classifications[class_name]['Description'] = format(strip_html((class_element/"properties")[0].documentation))
            
            def generalization(pe):
                try:
                    P = xmi_doc.by_id[(pe|"generalization").general]
                except:
                    P = None
                if P: return generalization(P)
                else: return pe
            
            
            for a in c/"attribute":
                type_name = "PEnum_" + a.name
                # @todo why is this lookup by name?
                enum_types_by_name = [c for c in xmi_doc.by_tag_and_type["packagedElement"]["uml:Class"] if c.name == type_name]
                if len(enum_types_by_name) == 1:
                    type_values = [x.name for x in enum_types_by_name[0]/"ownedLiteral"]
                else:
                    type_values = None
                    try:
                        pe_type = xmi_doc.by_id[(xmi_doc.by_id[a.idref]|"type").idref]
                        pe_type_name = pe_type.name
                        
                        root_generalization = generalization(pe_type)
                        type_name = root_generalization.name.lower()
                        
                    except ValueError as e:
                        print("WARNING:", a.name, "has no associated type", file=sys.stderr)
                        type_name = 'any'
                        continue
                        
                classifications[class_name]["Psets"][pset_name]["Properties"][a.name]['type'] = type_name
                classifications[class_name]["Psets"][pset_name]["Properties"][a.name]["Description"] = format(strip_html((a|"documentation").value))
                
                type_to_values = {
                    'boolean': ['TRUE','FALSE'],
                    'logical': ['TRUE','FALSE','UNKNOWN'],
                }
                if type_values is None:
                    type_values = type_to_values.get(type_name)
                if type_values:
                    classifications[class_name]["Psets"][pset_name]["Properties"][a.name]['values'] = type_values

    class_names = sorted(classifications.keys() | {c.get('Parent') for c in classifications.values() if c.get('Parent')})
    annotated = set()
    
    def element_by_id(id):
        return [x for x in xmi_doc.by_tag_and_type['element']['uml:Class'] if x.idref==id][0]        
    
    def annotate_parent(cn):      
        if cn in annotated: return
        annotated.add(cn)
        node = class_name_to_node.get(cn)
        if node is None:
            # probably an enumeration value handled above
            return
        try:
            for rel in (node|"links")/"Generalization":
                if rel.start == node.idref:
                    pc = xmi_doc.by_id[rel.end]
                    classifications[cn]["Parent"] = pc.name
                    classifications[cn]['Description'] = format(strip_html((element_by_id(rel.end)/"properties")[0].documentation))
                    annotate_parent(pc.name)
        except ValueError as e:
            print(e, file=sys.stderr)
                
    
    product = [c for c in xmi_doc.by_tag_and_type['element']['uml:Class'] if c.name == 'IfcProduct'][0]
    subtypes = []
    def visit_subtypes(t):
        sts = [element_by_id(g.start) for g in (t|"links")/"Generalization" if g.end == t.idref]
        subtypes.extend(x.name for x in sts)
        for t in sts:
            visit_subtypes(t)
    
    visit_subtypes(product)
    
    for cn in class_names:
        annotate_parent(cn)
        
    for cn in subtypes:
        annotate_parent(cn)
        
    return data
        

json.dump(generate_definitions(), OUTPUT, indent=2)
