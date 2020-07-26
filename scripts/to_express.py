# @todo: double encoding e.g Role &amp;lt;&amp;gt;
# @todo: schema name not really discoverable
# @todo: ControlPointsList / ColourList : LIST [2:?] OF LIST [2:?]
# @todo: IfcClassificationReference.HasReferences self referential inverse
# @todo: schema namespace different in constraint expression

import re
import sys
import html

import operator
import functools

from collections import defaultdict, namedtuple

import xmi
import express

import logging
logging.basicConfig(level=logging.DEBUG)

# The order in which definitions are to appear in the Express schema
EXPRESS_ORDER=("TYPE", "ENUM", "SELECT", "ENTITY", "FUNCTION", "RULE")

def unescape(s):
    # @todo this is bizarre encoding, what happened here?
    return html.unescape(html.unescape(s.replace('xx38', '&')))

def float_international(s):
    return float(s.replace(',', '.'))

try:
    fn = sys.argv[1]
    try:
        OUTPUT = open(sys.argv[2], "w", encoding='utf-8')
    except IndexError as e:
        OUTPUT = sys.stdout
except:
    print("Usage: python to_express.py <schema.xml>", file=sys.stderr)
    exit()
    
xmi = xmi.doc(fn)

connector_data = namedtuple("connector_data", ("is_inverse", "inverse_order", "aggregation_type", "is_optional"))
assocation_data = namedtuple("assocation_data", ("own_end", "type", "other_end", "asssocation"))

# Extract some data from the connectors for use later on
connectors = defaultdict(dict)
for c in xmi/"connector":
    src = c|"source"
    tgt = c|"target"
    for st, en in [(src, tgt), (tgt, src)]:
        cls = (st|"model").name
        other_cls = (en|"model").name
        is_inverse = "ExpressInverse" in st.tags()
        inverse_order = int(st.tags().get("ExpressOrderingInverse", 0))
        is_optional = "ExpressOptional" in st.tags()
        connectors[c.idref][other_cls] = connector_data(is_inverse, inverse_order, st.tags().get("ExpressAggregation"), is_optional)
    
# Extract some data from the assocations for use later on
assocations = defaultdict(list)
for assoc in xmi.by_tag_and_type["packagedElement"]["uml:Association"]:
    try:
        c1, c2 = assoc/'ownedEnd'
    except ValueError as e:
        logging.warning("encountered exception `%s' on %s", e, assoc)
        continue
    t1, t2 = map(lambda c: (c|"type").idref, (c1, c2))
    tv1, tv2 = map(lambda t: xmi.by_id[t].name, (t1, t2))
    cv1, cv2 = map(operator.attrgetter('name'), (c1, c2))
    assocations[tv1].append(assocation_data(c2, xmi.by_id[t2], c1, assoc))
    assocations[tv2].append(assocation_data(c1, xmi.by_id[t1], c2, assoc))

order = dict()
for o in xmi/"thecustomprofile:ExpressOrdering":
    d = o.attributes()
    dk = [k for k in d.keys() if k.startswith('base_')][0]
    order[d[dk]] = int(d['ExpressOrdering'])
    
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

def generate_definitions():
    """
    A generator that yields tuples of <a, b> with
    a: an element in EXPRESS_ORDER
    b: an type/entity/function definition string
    """
    
    for d in xmi.by_tag_and_type["element"]["uml:DataType"]:
       
        P = " ".join(map(str, get_path(xmi.by_id[d.idref])))
        print(P)
        if "to be replaced" in P:
            continue
       
        dd = xmi.by_id[d.idref]
        try:
            super = [t for t in d/"tag" if t.name == "ExpressDefinition"][0].value
            super_verbatim = True
        except IndexError as e:
            try:
                super = xmi.by_id[(dd|"generalization").general].name
                super_verbatim = False
            except ValueError as ee:
                # if the type does not have a generalization, let's assume it's one of EXPRESS' native types
                logging.warning("No generalization found on %s, omitting", d)
                continue
        
        cs = sorted(d/"constraint", key=lambda cc: float_international(cc.weight))
        constraints = map(lambda cc: "\t%s : %s;" % tuple(map(unescape, map(functools.partial(getattr, cc), ("name", "description")))), cs)            
        
        yield "TYPE", d.name, express.format_simple_type(d.name, super, constraints, super_verbatim=super_verbatim)
        
    for c in xmi.by_tag_and_type["element"]["uml:Class"]:
    
        P = " ".join(map(str, get_path(xmi.by_id[c.idref])))
        print(P)
        if "to be replaced" in P:
            continue
            
        stereotype = (c/"properties")[0].stereotype
        if stereotype is not None: 
            stereotype = stereotype.lower()
        
        if stereotype in {"express function", "express rule"}:
            
            yield stereotype.split(" ")[1].upper(), unescape((c|"behaviour").value).split(" ")[1], unescape((c|"behaviour").value) + ";"
            
        elif stereotype == 'predefinedtype':
            
            # A predefined type enumeration value, handled as part of 'ptcontainer'
            continue
        
        elif stereotype == "express select":
            
            values = filter(lambda s: s != c.name, map(lambda s: xmi.by_id[s.start].name, c/"Substitution"))
            yield "SELECT", c.name, express.format_type(c.name, "SELECT", values)
            
        elif stereotype == "enumeration":
            
            def try_get_order(a):
                try:
                    return int([t for t in a/("tag") if t.name == "ExpressOrdering"][0].value)
                except IndexError as e:
                    return 0
                    
            if "penum_" in c.name.lower():
                continue
                    
            values = map(operator.itemgetter(1), sorted(map(lambda a: (try_get_order(a), a.name), c/("attribute"))))
            yield "ENUM", c.name, express.format_type(c.name, "ENUMERATION OF", values)
            
        elif stereotype == 'templatecontainer':
            
            values = [xmi.by_id[d.supplier].name for d in xmi.by_tag_and_type["packagedElement"]["uml:Dependency"] if d.client==c.idref]
            # @todo ExpressOrdering on <element>
            yield "ENUM", c.name, express.format_type(c.name, "ENUMERATION OF", values)
            
        elif stereotype == 'ptcontainer':
            
            values = [x.name.split('.')[1] for x in xmi.by_tag_and_type["element"]["uml:Class"] if x.name.startswith(c.name + ".")]
            
            if "USERDEFINED" not in values: values.append("USERDEFINED")
            if "NOTDEFINED" not in values: values.append("NOTDEFINED")
            
            yield "ENUM", c.name, express.format_type(c.name, "ENUMERATION OF", values)
            
        elif stereotype is not None and (stereotype.startswith("pset") or stereotype == "$"):
            # Don't serialize psets to EXPRESS
            # @todo Some psets (and only psets) have their stereotype set to $, why?
            continue
            
        else:
        
            is_abstract = (c/"properties")[0].isAbstract == "true" 
        
            attribute_names = set()
            for la in c / ("attribute"):
                iref = la.idref
                a = xmi.by_id[iref]
                n = a.name
                attribute_names.add(n)

            attributes, inverses, derived, subtypes, supertypes = [], [], [], [], []
            
            for g in c/("Generalization"):
                start, end = g.start, g.end
                issub = start == c.idref
                other = [start, end][issub]
                other_name = xmi.by_id[other].name
                [supertypes, subtypes][issub].append(other_name)
            
            for end_node, end_node_type, other_end, assoc_node in assocations[c.name]:
                try:
                    nm = end_node.name
                    assert nm
                except:
                    continue
                    
                try:
                    attr_name = other_end.name
                except:
                    attr_name = None
                    
                bound = ""
                try:
                    lv = int((end_node|"lowerValue").value)
                    uv = int((end_node|"upperValue").value)
                    if uv == -1: uv = "?"
                    bound = "[%s:%s]" % (lv, uv)
                except: pass
                attr_entity = end_node_type.name

                is_inverse, inverse_order, express_aggr, is_optional = connectors[assoc_node.xmi_id][c.name]
                is_optional_string = "OPTIONAL " if is_optional else ""

                if express_aggr:
                    attr_entity = "%s %s OF %s" % (express_aggr, bound, attr_entity)

                if nm not in attribute_names:
                    if (is_inverse and attr_name is not None) or assoc_node.xmi_id not in order:
                        inverses.append((inverse_order, "\t%s : %s FOR %s;" % (nm, attr_entity, attr_name)))
                    else:
                        attribute_order = order[assoc_node.xmi_id]
                        attributes.append((attribute_order, "\t%s : %s%s;" % (nm, is_optional_string, attr_entity)))
                    
            for la in c/("attribute"):
                iref = la.idref
                a = xmi.by_id[iref]
                is_optional = "ExpressOptional" in map(operator.attrgetter('name'), la/("tag"))
                is_derived = a.isDerived == "true"
                express_aggr = la.tags().get("ExpressAggregation")
                if express_aggr:
                    bound = ""
                    try:
                        lv = int((a|"lowerValue").value)
                        uv = int((a|"upperValue").value)
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
                    continue
                attribute_names.add(n)
                tv = express.ifc_name(xmi.by_id[t].name)
                if express_aggr:
                    tv = "%s %s OF %s" % (express_aggr, bound, tv)
                attributes.append((ordering, "\t%s : %s%s;" % (n, is_optional_string, tv)))
            
            cs = sorted(c/("constraint"), key=lambda cc: float_international(cc.weight))
            constraints = map(lambda cc: (cc.type, "\t%s : %s;" % tuple(map(unescape, map(functools.partial(getattr, cc), ("name", "description"))))), cs)
            constraints_by_type = defaultdict(list)
            for ct, cc in constraints:
                constraints_by_type[ct].append(cc)

            attributes = map(operator.itemgetter(1), sorted(attributes))
            inverses = map(operator.itemgetter(1), sorted(inverses))
            
            yield "ENTITY", c.name, express.format_entity(c.name, attributes, derived, inverses, constraints_by_type["EXPRESS_WHERE"], constraints_by_type["EXPRESS_UNIQUE"], subtypes, supertypes, is_abstract)
            
def sort_key(tup):
    return (EXPRESS_ORDER.index(tup[0]), express.ifc_name(tup[1]))


schema_name = xmi.by_tag_and_type["packagedElement"]['uml:Package'][1].name.replace("exp", "").upper()
schema_name = "".join(["_", c][c.isalnum()] for c in schema_name)
schema_name = re.sub(r"_+", "_", schema_name)

print("SCHEMA %s;" % schema_name, file=OUTPUT)
print(file=OUTPUT)

emitted = set()

for exp_type, name, definition in sorted(generate_definitions(), key=sort_key):
    if (exp_type, name) in emitted:
        logging.warning("duplicate definition for %s %s", exp_type, name)
        continue
    emitted.add((exp_type, name))
    print(definition, file=OUTPUT)
    print(file=OUTPUT)

print("END_SCHEMA;", file=OUTPUT)
