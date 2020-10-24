import os
import re
import sys
import html
import json

from collections import defaultdict

from xmi_document import xmi_document

try:
    fn = sys.argv[1]
    try:
        OUTPUT = open(sys.argv[2], "w", encoding='utf-8')
    except IndexError as e:
        OUTPUT = sys.stdout
except:
    print("Usage: python to_po.py <schema.xml>", file=sys.stderr)
    exit()

xmi_doc = xmi_document(fn)
bfn = os.path.basename(fn)

schema_name = xmi_doc.xmi.by_tag_and_type["packagedElement"]['uml:Package'][1].name.replace("exp", "").upper()
schema_name = "".join(["_", c][c.isalnum()] for c in schema_name)
schema_name = re.sub(r"_+", "_", schema_name)
schema_name = schema_name.strip('_')

structure = {
        'Domain': {
            'Name': 'IFC',
            'Version': schema_name,
            
            'Classifications': None
        }
    }

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
    
def generalization(pe):
    try:
        P = xmi_doc.xmi.by_id[(pe|"generalization").general]
    except:
        P = None
    if P: return generalization(P)
    else: return pe


def generate_definitions():
    """
    A generator that yields tuples of <a, b> with
    a: location in file
    a: a fully qualifying key as tuple
    b: the documentation string
    """
    make_defaultdict = lambda: defaultdict(make_defaultdict)
    classifications = defaultdict(make_defaultdict)
    
    def get_parent_of_pt(enum_type):
        enum_id = enum_type.idref
        type_refs = []
        for assoc in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Association"]:
            try:
                c1, c2 = assoc/'ownedEnd'
            except ValueError as e:
                # print("encountered exception `%s' on %s" % (e, assoc))
                continue
            assoc_type_refs = set(map(lambda c: (c|"type").idref, (c1, c2)))
            if enum_id in assoc_type_refs:
                other_idref = list(assoc_type_refs - {enum_id})[0]
                type_refs.append(xmi_doc.xmi.by_id[other_idref].name)
                
        # @todo filter this based on inheritance hierarchy
        type_refs_without_type = [s for s in type_refs if 'Type' not in s]
        if len(type_refs_without_type) != 1:
            print("WARNING:", len(type_refs_without_type), "type associations on", enum_type.name, file=sys.stderr)
        
        return type_refs_without_type[0] if type_refs_without_type else None
    
    class_name_to_node = {}
    
    by_id = {}
    
    # psets are deferred to the end so that all ids are resolved
    psets = []
    
    for item in xmi_doc:
        
        if item.type == "ENUM" and item.stereotype == "PREDEFINED_TYPE":
        
            p = get_parent_of_pt(item.node)
            
            if p:
                         
                for c in item.children:            
                    by_id[c.id] = di = classifications[p + "_" + c.name]
                    di["Parent"] = p
                    di['Description'] = format(strip_html(c.documentation))
                
        elif item.type == "PSET":
            psets.append(item)        
                    
        elif item.type == "ENTITY":
            by_id[item.id] = di = classifications[item.name]
           
            st = item.meta.get('supertypes', [])
            if st:
                di['Parent'] = st[0]
            di['Description'] = format(strip_html(item.documentation))
            
    for item in psets:
        refs = item.meta.get('refs', [])
            
        for id in refs:
        
            di = by_id.get(id)
            if di is None:
                print("WARNING: for %s entity %s not emitted" % (item.name, xmi_doc.xmi.by_id[id].name))
                continue
            
            for a in item.children:                
            
                type_name = "PEnum_" + a.name
                # @todo why is this lookup by name?
                enum_types_by_name = [c for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Class"] if c.name == type_name]
                if len(enum_types_by_name) == 1:
                    type_values = [x.name for x in enum_types_by_name[0]/"ownedLiteral"]
                else:
                    type_values = None
                    try:
                        pe_type = xmi_doc.xmi.by_id[(xmi_doc.xmi.by_id[a.node.idref]|"type").idref]
                        pe_type_name = pe_type.name
                        
                        root_generalization = generalization(pe_type)
                        type_name = root_generalization.name.lower()
                        
                    except ValueError as e:
                        print("WARNING:", a.name, "has no associated type", file=sys.stderr)
                        type_name = 'any'
                        continue
                        
                di["Psets"][item.name]["Properties"][a.name]['type'] = type_name
                di["Psets"][item.name]["Properties"][a.name]["Description"] = format(strip_html(a.documentation))
                
                type_to_values = {
                    'boolean': ['TRUE','FALSE'],
                    'logical': ['TRUE','FALSE','UNKNOWN'],
                }
                if type_values is None:
                    type_values = type_to_values.get(type_name)
                if type_values:
                    di["Psets"][item.name]["Properties"][a.name]['values'] = type_values
                        
                
    return classifications

def filter_definition(di):

    children = defaultdict(list)    
    for k, v in di.items():
        if v.get("Parent"):
            children[v.get("Parent")].append(k)

    def parents(k):
        yield k
        v = di.get(k)
        if v and v.get('Parent'):
            yield from parents(v.get('Parent'))
            
    def child_or_self_has_psets(k):
        if di.get(k, {}).get("Psets"):
            return True
        for c in children[k]:
            if child_or_self_has_psets(c):
                return True
        return False
        
    def has_child(k):
        def has_child_(k2):
            if k2 == k: return True
            if not children[k2]: return False
            return any(has_child_(c) for c in children[k2])
        return has_child_

    def should_include(k, v):
        if k == "IfcControl":
            import pdb; pdb.set_trace()
        return ("IfcProduct" in parents(k)) or has_child("IfcProduct")(k) or child_or_self_has_psets(k)
        
    return {k: v for k, v in di.items() if should_include(k, v)}
    
def embed_in_structure(di):
    d = {}
    d.update(structure)
    d["Domain"]['Classifications'] = di
    return d

json.dump(embed_in_structure(filter_definition(generate_definitions())), OUTPUT, indent=2)
