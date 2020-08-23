import logging

express_basic_types = {"REAL", "NUMBER", "BINARY", "BOOLEAN", "INTEGER", "STRING", "LOGICAL"}

def ifc_name(name):
    if name.startswith("ENUMERATION"): return name
    if name.startswith("SELECT"): return name
    if name.startswith("Ifc"): return name
    for ebt in express_basic_types: 
        if ebt in name: return name
    name = "".join([" ", c][c.isalnum()] for c in name)
    s = "".join((s[0:1].upper() + s[1:].lower()) for s in name.split(" "))    
    if not s.lower().startswith("ifc"):
        s = "Ifc" + s
    return s

def format_simple_type(name, super, contraints=[], super_verbatim=False):
    cs_tuple = []
    contraints = list(contraints)
    if len(contraints) != 0:
        cs_tuple.append(" WHERE")
        cs_tuple.extend(contraints)
    return "\n".join((
        "TYPE %s = %s;" % (ifc_name(name), super if super_verbatim else ifc_name(super)),
    ) + tuple(cs_tuple) + (
        "END_TYPE;",
    ))

def format_type(name, type, values):
    return "\n".join((
        "TYPE %s = %s" % (ifc_name(name), ifc_name(type)),
        "\n".join(map(lambda v: "\t%s%s" % (",("[v[0] == 0], v[1]), enumerate(values))) + ");",
        "END_TYPE;"
    ))
    
def format_entity(name, attributes, derived, inverses, where_clauses, unique_clauses, subtypes, supertypes, is_abstract):
    adic = map(list, (attributes, derived, inverses, unique_clauses, where_clauses))
    adic_labels = None, "DERIVE", "INVERSE", "UNIQUE", "WHERE"
    abstract_string = ["", " ABSTRACT"][is_abstract]
    
    def _():
        semi = "" if len(subtypes) or len(supertypes) else ";"
        yield ("ENTITY %s" % ifc_name(name)) + semi
        if len(subtypes) > 1:
            logging.warning("Multiple super types for %s", name)
        if len(supertypes):
            semi = "" if len(subtypes) else ";"
            yield "%s SUPERTYPE OF (ONEOF\n%s))" % (abstract_string, "\n".join(map(lambda v: "\t%s%s" % (",("[v[0] == 0], ifc_name(v[1])), enumerate(sorted(supertypes))))) + semi
        if len(subtypes) == 1:
            yield " SUBTYPE OF (%s);" % ifc_name(subtypes[0])
        for label, li in zip(adic_labels, adic):
            if label: 
                if len(li):
                    yield " " + label
            yield from li
        yield "END_ENTITY;"

    return "\n".join(_())
