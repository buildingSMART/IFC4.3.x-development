import os
import re
import sys
import html
import json

from collections import defaultdict

from xmi_document import xmi_document
from nltk.corpus import words
from nltk import PorterStemmer

try:
    fn = sys.argv[1]
    try:
        OUTPUT = open(sys.argv[2], "w", encoding='utf-8')
    except IndexError as e:
        OUTPUT = sys.stdout
except:
    print("Usage: python to_bsdd.py <schema.xml>", file=sys.stderr)
    exit()

xmi_doc = xmi_document(fn)
xmi_doc.should_translate_pset_types = False
bfn = os.path.basename(fn)

ps = PorterStemmer()
words_to_catch = sorted(['current','switch','order','recovery','loading','barrier','reel','basin','fountain','packaged','nozzle','tube','plant','injection','assisted','element','vertical','turbine','heating','disassembly','button','exchange','component','security','deflector','chair','cabinet','assembly','actuator','meter','sensor','object','detection','station','depth','controller','terminal','center','frame','electric','exchangers','outlet','server','plate','expansion','exhaust','damper','shell','pump','filter','conveyor','rail','solar','surcharge','excavation','combustion','draft','mechanical','constant','coil','cooled','cooler','evaporative','pavement','top','column','traffic','crossing','side','road','vehicle','island','gear','super','event','adiabatic','segment','marker','structure','ground','channel','pressure','shift','prevention','tray','provision','soil','preloaded','water','cold','hot','cable','domestic','power','generation','solid','waste','unit','carrier','duct','protection','disconnector','surfacing','breaker','wall','flow','curve','limiter','board','chamber','panel','acoustic','fire','inspection','work','marking','transverse','rumble','strip','surface','maintenance','of','system','fixed','transmission','network','machine','device','equipment','sound','stud','connector','section','inventory','bill','quantities','compacted','drained','tower','indirect','direct','media','rigid','random','gravity','relief','air'], key=len)[::-1]

schema_name = xmi_doc.xmi.by_tag_and_type["packagedElement"]['uml:Package'][1].name.replace("exp", "").upper()
schema_name = "".join(["_", c][c.isalnum()] for c in schema_name)
schema_name = re.sub(r"_+", "_", schema_name)
schema_name = schema_name.strip('_')

structure = {
        'Dictionary': {
            'Name': 'IFC',
            'Version': schema_name,            
            'Classes': None
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
# CHANGE_LOG_PATTERN = re.compile(r'\{\s*\.change\-\w+\s*\}.+', flags=re.DOTALL)
CURLY_BRACKET_PATTERN = re.compile('{.*?}')

def strip_html(s):
    try:
        s1 = html.unescape(s)
    except TypeError:
        # error when name contains link, for example: "https://github.com/buildingSMART/IFC4.3.x-development/edit/master/docs/schemas/core/IfcProductExtension/Types/IfcAlignmentTypeEnum.md#L0 has no content"
        s1 = ''
    i = s1.find('\\n')
    if i != -1:
        s1 = s1[:i]
    s2 = re.sub(HTML_TAG_PATTERN, ' ', s1)
    s3 = re.sub(CURLY_BRACKET_PATTERN, ' ', s2)
    s4 = re.sub('   ', ' ', s3)
    s5 = re.sub('  ', ' ', s4)
    return s5

def split_at_word(w, s):
    if w in s.lower():
        if not ps.stem(w) in s.lower():
            s = re.sub(w, " "+w+" ", s.lower())
    if isinstance(s, list):
        s = " ".join(s)
    return s

def split_words(s):
    # hard-coded list of words found in enumerations to split the ALLCAPS phrases into indivudual words. List might not be complete

    for w in words_to_catch[::-1]:
        s = split_at_word(w, s)
    s = re.sub("  ", " ", s)
    return s.strip()

def format(s):
    # remove all redundant characters:
    clean = ''.join(['', c][c.isalnum() or c in '.,()- —'] for c in s)
    # s = re.sub(CHANGE_LOG_PATTERN, '', str(s)).strip()
    # s = s.replace("\\X\\0D", "")
    return re.sub(MULTIPLE_SPACE_PATTERN, ' ', clean).strip()
    
def generalization(pe):
    try:
        P = xmi_doc.xmi.by_id[(pe|"generalization").general]
    except:
        P = None
    if P: return generalization(P)
    else: return pe


type_to_values = {
    'boolean': ['TRUE','FALSE'],
    'logical': ['TRUE','FALSE','UNKNOWN'],
}

def generate_definitions():
    """
    A generator that yields tuples of <a, b> with
    a: location in file
    a: a fully qualifying key as tuple
    b: the documentation string
    """
    make_defaultdict = lambda: defaultdict(make_defaultdict)
    classes = defaultdict(make_defaultdict)
    
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
    item_by_id = {}
    
    # psets are deferred to the end so that all ids are resolved
    psets = []
    
    # same for entity attributes:
    entities = []
    
    # predefined types are just normal enumerations
    enumerations = {}
    
    pset_counts_by_stereo = defaultdict(int)
    
    for item in xmi_doc:
    
        item_by_id[item.id] = item

        if item.type == "ENUM":
            enumerations[item.name] = item
        
        elif item.type == "PSET":
            psets.append(item)
            
            stereo = (item.node/"properties")[0].stereotype
            pset_counts_by_stereo[stereo] += 1
            # add human-readable name
            di['Name'] = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', re.sub("Pset_", "", item.name)).title()

        elif item.type == "ENTITY":
            by_id[item.id] = di = classes[item.name]
           
            st = item.meta.get('supertypes', [])
            if st:
                di['Parent'] = st[0]
            di['Definition'] = format(strip_html(item.markdown))
            # add human-readable name
            di['Name'] = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', (item.name[3:] if item.name.lower().startswith('ifc') else item.name)).title()
            
            entities.append(item)

    for item in entities:
    
        if "IfcTypeObject" in xmi_doc.supertypes(item.id):
            continue
    
        predefined_type_attribute = [c for c in item.children if c.name == "PredefinedType"]
        if predefined_type_attribute:
            # NB this points to the EA extension node and not the packagedElement
            ptype = (predefined_type_attribute[0].node|"properties").type
            for c in enumerations[ptype].children:
                if c.name not in ("USERDEFINED","NOTDEFINED"):
                    by_id[c.id] = di = classes[item.name + "." + c.name]
                    di["Parent"] = item.name
                    di['Definition'] = format(strip_html(c.markdown))
                    # add human-readable name, by identifying words in all-caps phrase (right now the words are hardcoded)
                    di['Name'] = re.sub("_", " ", split_words(c.name)).title()

    for item in psets:
        refs = set(item.meta.get('refs') or [])
            
        for id in refs:
        
            if isinstance(id, tuple):
                # In case of TypeObject+PredefinedType appl
                # id = id[0]
                # what to do with typedrivenonly?
                # this option is disabled now
                assert False
                continue

            di = by_id.get(id)
            if di is None:
                try:
                    log_attr_2 = xmi_doc.xmi.by_id[id].name
                except KeyError as e:
                    log_attr_2 = id
                    print("WARNING: id %s not found" % id)
                    pass
                print("WARNING: for %s entity %s not emitted" % (item.name, log_attr_2))
                continue
            
            for a, (nm, (ty_ty_arg)) in zip(item.children, item.definition):
                
                if item.stereotype == "QSET":
                    type_name = "real"
                    type_values = None
                    kind_name = 'Single'
                else:
                    ty, ty_arg = ty_ty_arg
                    if ty == "PropertyEnumeratedValue":
                        type_name = list(ty_arg.values())[0]
                        enum_types_by_name = [c for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Class"] if c.name == type_name]
                        enum_types_by_name += [c for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Enumeration"] if c.name == type_name]
                        type_values = [x.name for x in enum_types_by_name[0]/"ownedLiteral"]
                        kind_name = 'Single'
                    else:
                        type_name = list(ty_arg.values())[0]
                        pe_types = [c for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Class"] if c.name == type_name]
                        pe_types += [c for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:DataType"] if c.name == type_name]                    
                        pe_type = pe_types[0]
                        root_generalization = generalization(pe_type)
                        type_name = root_generalization.name.lower()
                        type_values = None
                        if ty == "PropertySingleValue":
                            kind_name = 'Single'
                        elif ty == "PropertyBoundedValue":
                            di["Psets"][item.name]["Properties"][a.name]["Description"] = "This property in IFC stores a bounded value, meaning it has a maximum of two (numeric or descriptive) values assigned, the first value specifying the upper bound and the second value specifying the lower bound. Read the IFC documentation for more information."
                            kind_name = 'Range'
                        elif ty == "PropertyReferenceValue":
                            di["Psets"][item.name]["Properties"][a.name]["Description"] = "This property in IFC takes as its value a reference to one of: IfcAddress, IfcAppliedValue, IfcExternalReference, IfcMaterialDefinition, IfcOrganization, IfcPerson, IfcPersonAndOrganization, IfcTable, IfcTimeSeries. Read the IFC documentation for more information."
                            kind_name = 'Complex'
                        elif ty == "PropertyListValue":
                            di["Psets"][item.name]["Properties"][a.name]["Description"] = "This property in IFC takes list as its value. Read the IFC documentation for more information."
                            kind_name = 'List'
                        elif ty == "PropertyTableValue":
                            di["Psets"][item.name]["Properties"][a.name]["Description"] = "This property in IFC takes a table as its value. That table has two columns (two lists), one for defining and other for defined values. Read the IFC documentation for more information."
                            kind_name = 'Complex'
                    # else:
                    #     print("Warning: %s.%s of type %s <%s> not mapped" % (item.name, nm, ty, ",".join(map(lambda kv: "=".join(kv), ty_arg.items()))))
                    #     continue
                        
                di["Psets"][item.name]["Properties"][a.name]["type"] = type_name
                di["Psets"][item.name]["Properties"][a.name]["Definition"] = format(strip_html(a.markdown))
                di["Psets"][item.name]["Properties"][a.name]["kind"] = kind_name

                if type_values is None:
                    type_values = type_to_values.get(type_name)
                if type_values:
                    di["Psets"][item.name]["Properties"][a.name]["values"] = type_values

    for item in entities:
    
        item_name = item.name
        if item_name.endswith("Type"):
            item_name = item_name[:-4]
        di = classes[item_name]        
               
        for c in item.children:
        
            try:
                node = c.node
                if node.xml.tagName == "attribute":
                    node = xmi_doc.xmi.by_id[c.node.idref]
                    type_type = node|"type"
                    type_id = type_type.idref
                else:
                    type_id = ([t for t in (node/"ownedEnd") if t.name == c.name][0]|"type").idref
                    type_type = xmi_doc.xmi.by_id[type_id]
                type_item = item_by_id[type_id]
            except:
                print("Not emitting %s.%s because of an error" % (item.name, c.name))
                continue
            
            if c.name == "PredefinedType":
                print("Not emitting %s.%s because it's the PredefinedType attribute" % (item.name, c.name))
            elif type_item.type == "ENTITY":
                print("Not emitting %s.%s attribute because it's taking an ENTITY: %s" % (item.name, c.name, type_item.name))
            elif type_item.type == "SELECT":
                print("Not emitting %s.%s attribute because it's taking a SELECT: %s" % (item.name, c.name, type_item.name))
            elif type_item.type == "TYPE":
                
                type_values = None
                
                if type_item.definition.super_verbatim:
                
                    if not type_item.definition.super.lower().startswith("string"):                    
                        print("Not emitting %s.%s because it has a hardcoded express definition %s" % (item.name, c.name, type_item.definition.super))
                        continue
                    else:
                        type_name = "string"
                        
                else:
                
                    pattr = xmi_doc.xmi.by_id[c.node.idref]
                    ty_id = (pattr|"type").idref
                    ty_pe = xmi_doc.xmi.by_id[ty_id]
                    ty_gen = generalization(ty_pe)
                    type_name = ty_gen.name.lower()
                
                di["Psets"]["Attributes"]["Properties"][c.name]['type'] = type_name
                di["Psets"]["Attributes"]["Properties"][c.name]["Definition"] = format(strip_html(c.markdown))
                
                if type_values is None:
                    type_values = type_to_values.get(type_name)
                if type_values:
                    di["Psets"]["Attributes"]["Properties"][c.name]['values'] = type_values
            
            elif type_item.type == "ENUM":
            
                type_name = type_item.name
                type_values = type_item.definition.values
                
                di["Psets"]["Attributes"]["Properties"][c.name]['values'] = type_values
                di["Psets"]["Attributes"]["Properties"][c.name]['type'] = type_name
                di["Psets"]["Attributes"]["Properties"][c.name]["Definition"] = format(strip_html(c.markdown))
                
            else:
                print("Not emitting %s.%s because it's a %s %s" % (item.name, c.name, type_item.name, type_item.type))
            
    # for x in sorted([item.name for item in psets]):
    #     print(x)
            
    for k, v in pset_counts_by_stereo.items():
        print(k + ":", v)
        
    print("TOTAL:", sum(pset_counts_by_stereo.values()))
            
    return classes

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
        ps = di.get(k, {}).get("Psets")
        if ps:
            if set(ps.keys()) - {"Attributes"}:
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
        #PREVIOUSLY return ("IfcProduct" in parents(k)) or has_child("IfcProduct")(k) or child_or_self_has_psets(k) 
        #TODO right now 'has_pset' is broadening to include non-products that have psets.
        return ("IfcRoot" in parents(k)) or child_or_self_has_psets(k)
        
    return {k: v for k, v in di.items() if should_include(k, v)}
    
def embed_in_structure(di):
    d = {}
    d.update(structure)
    d["Dictionary"]['Classes'] = di
    return d

json.dump(embed_in_structure(filter_definition(generate_definitions())), OUTPUT, indent=2, default=lambda x: (getattr(x, 'to_json', None) or (lambda: vars(x)))())
