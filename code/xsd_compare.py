import sys
import operator

import xml_dict

fns = sys.argv[1:]
xds = list(map(xml_dict.read, fns))

ignored_attributes = ["targetNamespace"]

def freeze(x):
    if isinstance(x, dict):
        return frozenset(x.items())
    return x
    
def ignore_attributes(x):
    return {k:v for k,v in x.items() if k not in ignored_attributes}

def compare(args):
    tags = list(map(operator.attrgetter("tag"), args))
    attrs = list(map(ignore_attributes, map(operator.attrgetter("attributes"), args)))
    texts = list(map(str.strip, map(operator.attrgetter("text"), args)))
    
    def assert_equal(aspect, vs, abort=True):
        if len(set(map(freeze, vs))) != 1:
            print(aspect, "not equal: ", *vs)
            if abort:
                for x in args:
                    x.recursive_print()
                exit(1)
        print(vs[0])
            
    assert_equal("tags", tags)
    assert_equal("attributes", attrs)
    assert_equal("text", texts)
    
    children = list(map(operator.attrgetter("children"), args))
    child_count = list(map(len, children))
    
    assert_equal("child count", child_count, abort=False)
    
    for xs in zip(*children):
        compare(xs)

compare(xds)
