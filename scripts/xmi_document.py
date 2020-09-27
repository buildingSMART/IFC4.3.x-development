# @todo: double encoding e.g Role &amp;lt;&amp;gt;
# @todo: schema name not really discoverable
# @todo: ControlPointsList / ColourList : LIST [2:?] OF LIST [2:?]
# @todo: IfcClassificationReference.HasReferences self referential inverse
# @todo: schema namespace different in constraint expression

# CONFIGURATION
included_packages = set((
    "IFC 4.2 schema (13.11.2019)", 
    "Common Schema", 
    "IFC Ports and Waterways", 
    "IFC Road", 
    "IFC Rail - PSM"))
    
# currently not used
express_excluded_stereotypes = set((
    "propertyset", 
    "quantityset", 
    "penumtype", 
    "virtualentity"))
    
all_excluded_stereotypes = set((
    "virtualentity"))
    
included_statuses = set((
    "implemented", 
    "proposed", 
    "proposedmodification", 
    "deprecated", 
    "approved", 
    "candidate"))

import re
import sys
import html

import operator
import functools

from collections import defaultdict, namedtuple

import xmi
import express

import logging
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

# @todo schema name is hardcoded and not derived from the XMI package name for now
SCHEMA_NAME = "IFC4X3_RC1"

def unescape(s):
    # @todo this is bizarre encoding, what happened here?
    return html.unescape(html.unescape(s.replace('xx38', '&')))

def float_international(s):
    return float(s.replace(',', '.'))
    
connector_data = namedtuple("connector_data", ("is_inverse", "inverse_order", "aggregation_type", "is_optional"))
assocation_data = namedtuple("assocation_data", ("own_end", "type", "other_end", "asssocation"))

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
    
infinity = 1e9
    
def try_get_order(a):
    try:
        return int([t for t in a/("tag") if t.name == "ExpressOrdering"][0].value)
    except IndexError as e:
        # When no ordering is found in sequences where other elements do have
        # ordering, they are pushed to the back to be consistent with IFC4X3_RC1
        return infinity
        
where_pat = re.compile(r"'\w+\.(\w+(\.\w+)?)'")
def fix_schema_name(s):
    def repl(x):
        return "'%s.%s'" % (SCHEMA_NAME, x.group(1))
    return remove_linebreak_before_semi(re.sub(where_pat, repl, s))    
    
def remove_linebreak_before_semi(s):
    lines = s.split('\n')
    if lines[-1] == ';':
        lines[-2] += ';'
        lines[-1:] = []
    return '\n'.join(lines)
    

class xmi_item:
    type = None
    name = None
    definition = None
    node = None
    children = None
    
    def __init__(self, type, name, definition, node, children = None):
        self.type, self.name, self.definition, self.node, self.children = type, name, definition, node, children or []
        self.children = [xmi_item(None, a, None, b, None) for a, b in self.children]        
        
    def __iter__(self):
        return iter(self.children)
        
    def _get_documentation(self):
        ds = (self.node/"documentation")
        if len(ds) == 1:
            return ds[0].value
        else:
            ps = (self.node/"properties")
            if ps:
                return ps[0].documentation
        
    documentation = property(_get_documentation)
    
class xmi_document:

    def __init__(self, fn):    
    
        self.xmi = xmi.doc(fn)
        self.extract_connectors()
        self.extract_associations()
        self.extract_order()
                
        # Assert that we indeed have all `included_packages` in the UML
        packagenames_from_uml = set(map(operator.attrgetter('name'), self.xmi.by_tag_and_type["packagedElement"]["uml:Package"]))
        assert len(included_packages - packagenames_from_uml) == 0
        
    def skip_by_package(self, element):
        return not (set(get_path(self.xmi.by_id[element.idref])) & included_packages)
        
    def extract_connectors(self):
        # Extract some data from the connectors for use later on
        self.connectors = defaultdict(dict)
        for c in self.xmi/"connector":
            src = c|"source"
            tgt = c|"target"
            
            # model need to be populated for both and at least one role (attribute name)
            if not ((src|"model").name and (tgt|"model").name and ((src|"role").name or (tgt|"role").name)):
                continue    
            
            marked_inverse = False
            for st, en in [(src, tgt), (tgt, src)]:
                marked_inverse |= "ExpressInverse" in st.tags()
                
            for st, en in [(src, tgt), (tgt, src)]:
                cls = (st|"model").name
                other_cls = (en|"model").name
                
                if marked_inverse:
                    is_inverse = "ExpressInverse" in st.tags()
                else:
                    # @tfk this is a guess but apparently in the cases where ExpressInverse where
                    # not marked, the inverse attribute is on the source end of the connector
                    is_inverse = st == src
                    
                inverse_order = int(st.tags().get("ExpressOrderingInverse", 0))
                is_optional = "ExpressOptional" in st.tags()
                self.connectors[c.idref][other_cls] = connector_data(is_inverse, inverse_order, st.tags().get("ExpressAggregation"), is_optional)
            
            # if not marked_inverse:
            #     if (src|"model").name and (src|"role").name and (tgt|"model").name and (tgt|"role").name:
            #         logging.warning("Inverse not marked on %s: %s.%s %s.%s", c, (src|"model").name, (src|"role").name, (tgt|"model").name, (tgt|"role").name)
            
    def extract_associations(self):
        # Extract some data from the assocations for use later on
        self.assocations = defaultdict(list)
        for assoc in self.xmi.by_tag_and_type["packagedElement"]["uml:Association"]:
            try:
                c1, c2 = assoc/'ownedEnd'
            except ValueError as e:
                logging.warning("encountered exception `%s' on %s", e, assoc)
                continue
            t1, t2 = map(lambda c: (c|"type").idref, (c1, c2))
            tv1, tv2 = map(lambda t: self.xmi.by_id[t].name, (t1, t2))
            cv1, cv2 = map(operator.attrgetter('name'), (c1, c2))
            self.assocations[tv1].append(assocation_data(c2, self.xmi.by_id[t2], c1, assoc))
            self.assocations[tv2].append(assocation_data(c1, self.xmi.by_id[t1], c2, assoc))

    def extract_order(self):
        self.order = dict()
        for o in self.xmi/"thecustomprofile:ExpressOrdering":
            d = o.attributes()
            dk = [k for k in d.keys() if k.startswith('base_')][0]
            self.order[d[dk]] = int(d['ExpressOrdering'])    
    
    def __iter__(self):
        """
        A generator that yields tuples of <a, b> with
        a: an element in EXPRESS_ORDER
        b: an type/entity/function definition string
        """
               
        for c in (self.xmi.by_tag_and_type["element"]["uml:Class"] + self.xmi.by_tag_and_type["element"]["uml:Interface"] + self.xmi.by_tag_and_type["element"]["uml:Enumeration"] + self.xmi.by_tag_and_type["element"]["uml:DataType"]):
        
            if self.skip_by_package(c):
                continue
                
            stereotype = (c/"properties")[0].stereotype if (c/"properties") else None
            if stereotype is not None: 
                stereotype = stereotype.lower()
                
            if stereotype in all_excluded_stereotypes:
                continue
                
            status = (c/"project")[0].status if (c/"project") else None
            if status is not None: 
                status = status.lower()
                
            if status not in included_statuses:
                continue
            
            if stereotype in {"express function", "express rule"}:
                
                yield xmi_item(stereotype.split(" ")[1].upper(), unescape((c|"behaviour").value).split(" ")[1], fix_schema_name(unescape((c|"behaviour").value)) + ";", c)
                
            elif stereotype == 'predefinedtype':
                
                # A predefined type enumeration value, handled as part of 'ptcontainer'
                continue
                
            elif stereotype == "propertyset" or stereotype == "quantityset" or (stereotype is not None and stereotype.startswith("pset_")):
                
                yield xmi_item("PSET", c.name, "", c, [
                    (x.name, x) for x in c/("attribute")
                ])
                
            elif c.xmi_type == "uml:DataType":
            
                dd = self.xmi.by_id[c.idref]
                try:
                    super = [t for t in c/"tag" if t.name == "ExpressDefinition"][0].value
                    super_verbatim = True
                except IndexError as e:
                    try:
                        super = self.xmi.by_id[(dd|"generalization").general].name
                        super_verbatim = False
                    except ValueError as ee:
                        # if the type does not have a generalization, let's assume it's one of EXPRESS' native types
                        logging.warning("No generalization found on %s, omitting", c)
                        continue
                
                cs = sorted(c/"constraint", key=lambda cc: float_international(cc.weight))
                constraints = map(lambda cc: "\t%s : %s;" % tuple(map(unescape, map(functools.partial(getattr, cc), ("name", "description")))), cs)            
                
                yield xmi_item("TYPE", c.name, express.format_simple_type(c.name, super, constraints, super_verbatim=super_verbatim), c)
                
            elif c.xmi_type == "uml:Enumeration":
            
                get_attribute = lambda n: [x for x in self.xmi.by_idref[n.xmi_id] if x.xml.tagName == "attribute"][0]
                values = [(x.name, get_attribute(x)) for x in self.xmi.by_id[c.xmi_idref]/"ownedLiteral"]
                yield xmi_item(
                    "PENUM" if stereotype == "penumtype" or c.name.lower().startswith("penum_") else "ENUM", # <------- nb 
                    c.name, express.format_type(c.name, "ENUMERATION OF", [a for a, b in values]), c, values)
            
            elif stereotype == "express select" or stereotype == "select" or c.xmi_type == "uml:Interface":
                
                values = sorted(filter(lambda s: s != c.name, map(lambda s: self.xmi.by_id[s.start].name, c/"Substitution")))
                yield xmi_item("SELECT", c.name, express.format_type(c.name, "SELECT", values), c)
                
            elif stereotype == "enumeration":
                                   
                if "penum_" in c.name.lower():
                    continue
                        
                values = map(operator.itemgetter(1), sorted(map(lambda a: (try_get_order(a), (a.name, a)), c/("attribute"))))
                yield xmi_item("ENUM", c.name, express.format_type(c.name, "ENUMERATION OF", [a for a, b in values]), c, values)
                
            elif stereotype == 'templatecontainer':

                nodes = [[x for x in self.xmi.by_idref[d.supplier] if x.xml.tagName == "element"][0] for d in self.xmi.by_tag_and_type["packagedElement"]["uml:Dependency"] if d.client==c.idref]
                values = [(n.name, n) for n in nodes]
                # @todo ExpressOrdering on <element>
                yield xmi_item("ENUM", c.name, express.format_type(c.name, "ENUMERATION OF", [a for a, b in values]), c, values)
                
            elif stereotype == 'ptcontainer':
                
                children = []
                ids = [d.end for d in (c/"Dependency") if d.start == c.xmi_idref]
                if not ids:
                    print("Warning, no dependency relationship for %s" % c.name)
                    nodes = [x for x in self.xmi.by_tag_and_type["element"]["uml:Class"] if x.name.startswith(c.name + ".")]
                    children = list(map(operator.itemgetter(1), sorted(map(lambda a: (try_get_order(a), (a.name.split('.')[1], a)), nodes))))
                    values = [a for a, b in children]
                else:
                    def get_element(id): return [n for n in self.xmi.by_tag_and_type['element']['uml:Class'] if n.idref==id][0]
                    elems = list(map(get_element, ids))
                    def get_stereotype(elem): return (elem/"properties")[0].stereotype if (elem/"properties") else None
                    stereotypes = list(map(get_stereotype, elems))
                    # pelems = [self.xmi.by_id[n.idref] for n in elems]
                    # [self.skip_by_package(x) for x in pelems]
                    # [(x|"project").status for x in elems]
                    filtered_elems = [e for e,s in zip(elems, stereotypes) if s.lower() != 'virtualentity']
                    children = [(e.name.split('.')[-1], e) for e in filtered_elems]
                    # make unique by name
                    children = [x for i,x in enumerate(children) if x[0] not in [y[0] for y in children[0:i]]]
                    values = [a for a, b in children]
                
                if "USERDEFINED" not in values: values.append("USERDEFINED")
                if "NOTDEFINED" not in values: values.append("NOTDEFINED")
                
                yield xmi_item("ENUM", c.name, express.format_type(c.name, "ENUMERATION OF", values), c, children)
                
            elif stereotype is not None and (stereotype.startswith("pset") or stereotype == "$"):
                # Don't serialize psets to EXPRESS
                # @todo Some psets (and only psets) have their stereotype set to $, why?
                continue
                
            elif stereotype == "virtualentity":
            
                continue
                
            else:
            
                if not c.name.startswith("Ifc"):
                    # @tfk entities need to start with IFC or otherwise 'conceptual'?
                    continue
            
                is_abstract = (c/"properties")[0].isAbstract == "true" 
            
                attribute_names = set()
                attributes_optional = {}
                for la in c / ("attribute"):
                    iref = la.idref
                    a = self.xmi.by_id[iref]
                    n = a.name
                    attribute_names.add(n)

                attributes, inverses, derived, subtypes, supertypes, children = [], [], [], [], [], []
                
                for g in c/("Generalization"):
                    start, end = g.start, g.end
                    issub = start == c.idref
                    other = [start, end][issub]
                    other_name = self.xmi.by_id[other].name
                    [supertypes, subtypes][issub].append(other_name)
                    
                for end_node, end_node_type, other_end, assoc_node in self.assocations[c.name]:
                    try:
                        nm = end_node.name
                        assert nm
                    except:
                        continue
                        
                    try:
                        attr_name = other_end.name
                    except:
                        attr_name = None
                        
                    try:
                        is_inverse, inverse_order, express_aggr, is_optional = self.connectors[assoc_node.xmi_id][c.name]
                    except:
                        is_inverse, is_optional, express_aggr = False, False, None
                        
                    is_inverse |= assoc_node.xmi_id not in self.order
                        
                    if not is_inverse and end_node.isOrdered is not None:
                        ####
                        express_aggr = "LIST" if end_node.isOrdered == "true" else "SET"
                        
                    if end_node/"lowerValue" and not express_aggr:
                        is_optional |= (end_node|"lowerValue").value == '0'
                        
                    bound = "[0:1]" if is_inverse else "[0:?]"
                    try:
                        lv = int((end_node|"lowerValue").value)
                        uv_s = (end_node|"upperValue").value
                        if uv_s == "*":
                            uv = "?"
                        else:
                            uv = int(uv_s)
                            if uv == -1: uv = "?"
                        bound = "[%s:%s]" % (lv, uv)
                    except: pass
                    attr_entity = end_node_type.name                
                        
                    # bound != "[0:?]" and 
                    # inverse attributes always aggregates?
                    if is_inverse and end_node.isOrdered is None and bound != "[1:1]":
                        express_aggr = "SET"
                        
                    is_optional_string = "OPTIONAL " if is_optional else ""                    
                    
                    if express_aggr:
                        attr_entity = "%s %s OF %s" % (express_aggr, bound, attr_entity)

                    if nm not in attribute_names:
                        if (is_inverse and attr_name is not None): # or assoc_node.xmi_id not in order:
                            inverses.append((inverse_order, "\t%s : %s FOR %s;" % (nm, attr_entity, attr_name)))
                        else:
                            attribute_order = self.order.get(assoc_node.xmi_id, None)
                            if attribute_order is None:
                                logging.warning("No attribute order on %s.%s" % (c.name, nm))
                                attribute_order = 1000
                            attributes.append((attribute_order, "\t%s : %s%s;" % (nm, is_optional_string, attr_entity)))
                            
                        children.append((nm, assoc_node))
                    else:
                        # mark as optional for when emitted as an UML attribute below
                        attributes_optional[nm] = is_optional
                        
                    # @tfk workaround for associations with the same name
                    attribute_names.add(nm)
                        
                for la in c/("attribute"):
                
                    iref = la.idref
                    a = self.xmi.by_id[iref]
                    is_optional = "ExpressOptional" in map(operator.attrgetter('name'), la/("tag"))
                    bnds = la/"bounds"
                    express_aggr = la.tags().get("ExpressAggregation") or (bnds and bnds[0].upper and bnds[0].upper != '1')
                    if not express_aggr:
                        if bnds:
                            is_optional |= bnds[0].lower == '0'
                        is_optional |= attributes_optional.get(a.name, False)
                            
                    is_derived = a.isDerived == "true"
                    
                    if express_aggr is True and (la/"coords"):
                        express_aggr = "LIST" if (la/"coords")[0].ordered == "1" else "SET"
                    
                    if express_aggr:
                        bound = ""
                        try:
                            lv = int((a|"lowerValue").value)
                            uv_s = (a|"upperValue").value
                            if uv_s == "*":
                                uv = "?"
                            else:
                                uv = int(uv_s)
                                if uv == -1: uv = "?"
                            bound = "[%s:%s]" % (lv, uv)
                        except: continue
                    # or use order[iref]?
                    try:
                        ordering = int(la.tags()["ExpressOrdering"])
                    except KeyError as e:
                        ordering = 0
                    is_optional_string = "OPTIONAL " if is_optional else ""
                    n = a.name
                    try:
                        t = (a|"type").idref
                    except:
                        is_derived = len(la/"Constraint") == 1
                        if not is_derived:
                            logging.warning("Unable to find type of %s on %s", a, c)
                            continue
                        
                    if is_derived:
                        derived.append("\t%s : %s;" % (n, unescape((la|"Constraint").notes)))
                        children.append((n, la))
                        continue
                    attribute_names.add(n)
                    
                    tv = express.ifc_name(self.xmi.by_id[t].name)
                    if express_aggr:
                        tv = "%s %s OF %s" % (express_aggr, bound, tv)
                    
                    override = la.tags().get("ExpressDefinition")
                    if override:
                        tv = override
                        is_optional_string = ""
                        
                    attributes.append((ordering, "\t%s : %s%s;" % (n, is_optional_string, tv)))
                    
                    children.append((n, la))
                
                cs = sorted(c/("constraint"), key=lambda cc: float_international(cc.weight))
                constraints = map(lambda cc: (cc.type, "\t%s : %s;" % tuple(map(unescape, map(functools.partial(getattr, cc), ("name", "description"))))), cs)
                constraints_by_type = defaultdict(list)
                for ct, cc in constraints:
                    constraints_by_type[ct].append(fix_schema_name(cc))

                attributes = map(operator.itemgetter(1), sorted(attributes))
                inverses = map(operator.itemgetter(1), sorted(inverses))
                
                yield xmi_item("ENTITY", c.name, express.format_entity(c.name, attributes, derived, inverses, constraints_by_type["EXPRESS_WHERE"], constraints_by_type["EXPRESS_UNIQUE"], subtypes, supertypes, is_abstract), c, children)
