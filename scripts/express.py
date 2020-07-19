import logging

express_basic_types = {"REAL", "NUMBER", "BINARY", "BOOLEAN", "INTEGER", "STRING", "LOGICAL"}

def ifc_name(name):
    if "Ifc" in name: return name
    for ebt in express_basic_types: 
        if ebt in name: return name
    name = "".join([" ", c][c.isalnum()] for c in name)
    return "Ifc" + "".join((s[0:1].upper() + s[1:].lower()) for s in name.split(" "))    

def format_simple_type(name, super, contraints=[]):
    cs_tuple = []
    contraints = list(contraints)
    if len(contraints) != 0:
        cs_tuple.append(" WHERE")
        cs_tuple.extend(contraints)
    return "\n".join((
        "TYPE %s = %s;" % (ifc_name(name), ifc_name(super)),
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
    adic = map(list, (attributes, derived, inverses, where_clauses, unique_clauses))
    adic_labels = None, "DERIVE", "INVERSE", "WHERE", "UNIQUE"
    abstract_string = ["", " ABSTRACT"][is_abstract]
    
    def _():
        semi = "" if len(subtypes) or len(supertypes) else ";"
        yield ("ENTITY %s" % ifc_name(name)) + semi
        if len(subtypes) > 1:
            logging.warning("Multiple super types for %s", name)
        if len(supertypes):
            semi = "" if len(subtypes) else ";"
            yield "%s SUPERTYPE OF (ONEOF\n%s))" % (abstract_string, "\n".join(map(lambda v: "\t%s%s" % (",("[v[0] == 0], ifc_name(v[1])), enumerate(supertypes)))) + semi
        if len(subtypes) == 1:
            yield " SUBTYPE OF (%s);" % ifc_name(subtypes[0])
        for label, li in zip(adic_labels, adic):
            if label: 
                if len(li):
                    yield " " + label
            yield from li
        yield "END_ENTITY;"

    return "\n".join(_())
