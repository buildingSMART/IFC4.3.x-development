import sys
import operator

import tabulate

from . import express_parser
from . import nodes

fn1, fn2, output = sys.argv[1:]

print("Running difference", *sys.argv[1:])

def eq(a, b):
    if (type(a) != type(b)):
        return False
    elif isinstance(a, (nodes.StringType, nodes.AggregationType, nodes.BinaryType, str, nodes.ExplicitAttribute, nodes.InverseAttribute)):
        return str(a) == str(b)
    elif isinstance(a, (nodes.SelectType, nodes.EnumerationType)):
        return set(a.values) == set(b.values)
    elif isinstance(a, nodes.EntityDeclaration):
        # @todo
        import pdb; pdb.set_trace()
        
        return str(a) == str(b)
    else:
        import pdb; pdb.set_trace()
        
def format(a):
    if isinstance(a, (nodes.SelectType, nodes.EnumerationType)):
        return ", ".join(sorted(a.values))
    else:
        return str(a)

def compare(fn1, fn2, s1, s2):
    for nm in set(s1.keys) - set(s2.keys):
        yield (nm, "", "not in '%s'" % fn2)
        
    for nm in set(s2.keys) - set(s1.keys):
        yield (nm, "not in '%s'" % fn1, "")
        
    for x in 'simpletypes', 'selects', 'enumerations':
        d1, d2 = map(operator.attrgetter(x), (s1, s2))
        for nm in sorted(d1.keys() & d2.keys()):
            if not eq(d1[nm], d2[nm]):
                yield (nm, d1[nm], d2[nm])
            
    for e in sorted(s1.entities.keys() & s2.entities.keys()):
        e1, e2 = s1.entities[e], s2.entities[e]
        if e1.abstract != e2.abstract:
            yield (e, ["not abstract", "abstract"][e1.abstract], ["not abstract", "abstract"][e2.abstract])
        if e1.supertypes != e2.supertypes:
            yield (e + " supertype", e1.supertypes, e2.supertypes)
            
        e1_anames = [attr.name for attr in e1.attributes]
        e2_anames = [attr.name for attr in e2.attributes]
        if e1_anames != e2_anames:
            yield (e + " attributes", e1_anames, e2_anames)
        e1_anames = {attr.name:attr for attr in e1.attributes}
        e2_anames = {attr.name:attr for attr in e2.attributes}
        for nm in e1_anames.keys() & e2_anames.keys():
            if not eq(e1_anames[nm], e2_anames[nm]):
                yield (e + "." + nm, e1_anames[nm], e2_anames[nm])
                
        e1_anames = [attr.name for attr in (e1.inverse or [])]
        e2_anames = [attr.name for attr in (e2.inverse or [])]
        if e1_anames != e2_anames:
            yield (e + "." + nm + " inverses", e1_anames, e2_anames)
        e1_anames = {attr.name:attr for attr in (e1.inverse or [])}
        e2_anames = {attr.name:attr for attr in (e2.inverse or [])}
        for nm in e1_anames.keys() & e2_anames.keys():
            if not eq(e1_anames[nm], e2_anames[nm]):
                yield (e + "." + nm, e1_anames[nm], e2_anames[nm])
                
with open(output, "w") as f:
    f.write(tabulate.tabulate(list(
        [format(x) for x in tup] for tup in compare(fn1, fn2, *map(express_parser.parse, (fn1, fn2)))
    ), headers=["Name", fn1, fn2], tablefmt="github"))
