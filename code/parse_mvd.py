import os
import io
import operator
import functools
import dataclasses

import pyparsing

from collections import defaultdict

from ifcopenshell import mvd
from ifcopenshell.mvd.mvdxml_expression import node as expression_node

flatten=lambda l: sum(map(flatten,l),[]) if isinstance(l,(list, pyparsing.ParseResults)) else [l]

def dump(rule, parents, file):
    print(" " * len(parents), "- ", rule.attribute, sep='', file=file)

def remove_quotes(v):
    if v[0] == "'" and v[-1] == "'":
        return v[1:-1]
    else:
        return v

@dataclasses.dataclass(order=True, frozen=True)
class concept_binding:
    entity: str
    name: str
    definition: str
    rules: object
    parameters: object
    parameter_docs: list
    

def enumerate_concepts(fn, with_rules=True):
    roots = list(mvd.concept_root.parse(fn))
    for root in roots:
        for concept in root.concepts():
            try:
                definition = concept.concept_node.getElementsByTagName('Definition')[0].getElementsByTagName("Body")[0].firstChild.wholeText
            except:
                definition = ''
                
            rules = None
            
            if with_rules:
                s = io.StringIO()
                concept.template().traverse(functools.partial(dump, file=s), with_parents=True)
                rules = s.getvalue()
            
            parameters = defaultdict(list)
            for k, v in map(operator.attrgetter('a', 'c'), filter(lambda x: isinstance(x, expression_node), flatten(concept.rules()))):
                parameters[k].append(remove_quotes(v))
                
            parameter_docs = [n.getAttribute("Description") for n in concept.concept_node.getElementsByTagName('TemplateRule')]
            if parameter_docs:
                param_len = len(next(iter(parameters.values())))
                if param_len != len(parameter_docs):
                    breakpoint()
                
            yield concept_binding(root.entity, concept.name, definition, rules, dict(parameters.items()), parameter_docs)


if __name__ == "__main__":
    import sys
    import json

    try: fn = sys.argv[1]
    except: fn = None

    output = defaultdict(dict)

    for cb in enumerate_concepts(fn):
        output[cb.entity][cb.name] = dataclasses.asdict(cb)

    json.dump(output, open("concepts.json", "w"), indent=1)
