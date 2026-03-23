import logging

_join = lambda x: map(lambda tup: "\t%s : %s;" % tup, x)

class simple_type:
    def __init__(self, name, super, constraints):
        self.name, self.super, self.constraints = name, super, list(constraints)
    
    def to_express(self):
        cs_tuple = []
        if len(self.constraints) != 0:
            cs_tuple.append(" WHERE")
            cs_tuple.extend(_join(self.constraints))
        return "\n".join((
            "TYPE %s = %s;" % (self.name, self.super),
        ) + tuple(cs_tuple) + (
            "END_TYPE;",
        ))    
    
    def __repr__(self):
        return self.to_express()
        
        
class enum_or_select:
    def __init__(self, name, values):
        self.name = name
        self.values = values
        
    def to_express(self):
        return "\n".join((
            "TYPE %s = %s" % (self.name, self.type),
            "\n".join(map(lambda v: "\t%s%s" % (",("[v[0] == 0], v[1]), enumerate(self.values))) + ");",
            "END_TYPE;"
        ))
        
    def __repr__(self):
        return self.to_express()


class enumeration(enum_or_select):
    type = "ENUMERATION OF"
    
    
class select(enum_or_select):
    type = "SELECT"
    
    
class entity:
    
    def __init__(self, name, attributes, derived, inverses, where_clauses, unique_clauses, subtypes, supertypes, is_abstract):
        self.name, self.attributes, self.derived, self.inverses, self.where_clauses, self.unique_clauses, self.subtypes, self.supertypes, self.is_abstract = \
            name, list(attributes), list(derived), list(inverses), list(where_clauses), list(unique_clauses), list(subtypes), list(supertypes), is_abstract
            
    def _get_supertype(self):
        # @todo this is some weird naming due to ` .. of .. ' naming in express
        if len(self.subtypes) == 1:
            return self.subtypes[0]
    supertype = property(_get_supertype)
    
            
    def to_express(self):
        adic = map(list, map(_join, (self.attributes, self.derived, self.inverses, self.unique_clauses, self.where_clauses)))
        adic_labels = None, "DERIVE", "INVERSE", "UNIQUE", "WHERE"
        abstract_string = ["", " ABSTRACT"][self.is_abstract]
        
        def _():
            semi = "" if len(self.subtypes) or len(self.supertypes) else ";"
            yield ("ENTITY %s" % self.name) + semi
            if len(self.subtypes) > 1:
                logging.warning("Multiple super types for %s", self.name)
                breakpoint()
            if len(self.supertypes):
                semi = "" if len(self.subtypes) else ";"
                yield "%s SUPERTYPE OF (ONEOF\n%s))" % (abstract_string, "\n".join(map(lambda v: "\t%s%s" % (",("[v[0] == 0], v[1]), enumerate(sorted(self.supertypes))))) + semi
            if len(self.subtypes) == 1:
                yield " SUBTYPE OF (%s);" % self.subtypes[0]
            for label, li in zip(adic_labels, adic):
                if label: 
                    if len(li):
                        yield " " + label
                yield from li
            yield "END_ENTITY;"

        return "\n".join(_())

    def __repr__(self):
        return self.to_express()