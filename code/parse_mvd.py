import io
import sys
import json
import operator
import functools

import pyparsing

from collections import defaultdict

from ifcopenshell import mvd
from ifcopenshell.mvd.mvdxml_expression import node as expression_node

flatten=lambda l: sum(map(flatten,l),[]) if isinstance(l,(list, pyparsing.ParseResults)) else [l]

try:
    fn = sys.argv[1]
except:
    # fn = "data/mvdXML/ReferenceView_V1-2.mvdxml"
    fn = "../mvdXML/IFC4_ADD2.mvdxml"

def dump(rule, parents, file=sys.stdout): print(" " * len(parents), "- ", rule.attribute, sep='', file=file)

roots = list(mvd.concept_root.parse(fn))

output = defaultdict(dict)

for root in roots:
    for concept in root.concepts():
    
        try:
            definition = concept.concept_node.getElementsByTagName('Definition')[0].getElementsByTagName("Body")[0].firstChild.wholeText
        except:
            definition = ''
        s = io.StringIO()
        concept.template().traverse(functools.partial(dump, file=s), with_parents=True)
        rules = s.getvalue()
        
        parameters = defaultdict(list)
        for k, v in map(operator.attrgetter('a', 'c'), filter(lambda x: isinstance(x, expression_node), flatten(concept.rules()))):
            parameters[k].append(v)

        output[root.entity][concept.name] = {
            'definition': definition,
            'rules': rules,
            'parameters': parameters
        }

json.dump(output, open("concepts.json", "w"), indent=1)
