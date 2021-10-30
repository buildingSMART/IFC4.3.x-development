import io
import sys
import json
import operator
import itertools
import functools

import pyparsing

from collections import defaultdict

from ifcopenshell import mvd
from ifcopenshell.mvd.mvdxml_expression import node as expression_node

import xlsxwriter

flatten=lambda l: sum(map(flatten,l),[]) if isinstance(l,(list, pyparsing.ParseResults)) else [l]

class capturer:
    """
    Captures template rule identification    
    """
    def __init__(self, root=None):
        self.mapping = {}
        self.root = root
        
    def __call__(self, rule, parent):
        if rule.bind:
            self.mapping[rule.bind] = ((parent.attribute if parent else self.root), rule.attribute)

try:
    fn = sys.argv[1]
except:
    fn = "../mvdXML/IFC4_ADD2.mvdxml"

def dump(rule, parents, file=sys.stdout): print(" " * len(parents), "- ", rule.attribute, sep='', file=file)

roots = list(mvd.concept_root.parse(fn))
grouping = defaultdict(list)
bindings = {}

for root in roots:
    for concept in root.concepts():
        tmpl = concept.template()
        uuid = tmpl.root.getAttribute("uuid")
        if uuid in bindings:
            ks = bindings[uuid]
        else:
            capture_binding = capturer(tmpl.entity)
            tmpl.traverse(capture_binding)
            ks = tuple(sorted(capture_binding.mapping.items()))
            bindings[uuid] = ks
            
        if concept.name == "Property Sets for Objects" and root.entity == "IfcDiscreteAccessory":
            import pdb; pdb.set_trace()
    
        parameters = defaultdict(list)
        param_keys = dict(ks).keys()
        for rl in concept.rules():
            if rl == "and": continue
            prms = dict(map(operator.attrgetter('a', 'c'), filter(lambda x: isinstance(x, expression_node), flatten(rl))))
            for kk in param_keys:
                parameters[kk].append(prms.get(kk))
        
        key = (concept.name,) + ks
        
        for vals in itertools.zip_longest(*[parameters.get(k[0], []) for k in ks]):
            grouping[key].append((root.entity,) + tuple(vals))
            
        if len(parameters) == 0:
            grouping[key].append((root.entity,) + tuple(None for k in ks))
            
def format(v):
    if isinstance(v, str) and v[0] == "'" and v[-1] == "'":
        return v[1:-1]
    return v
    
workbook = xlsxwriter.Workbook('concepts.xlsx')
header_format = workbook.add_format({'bg_color': 'black', 'font_color': 'white'})
postfixes = defaultdict(int)
for k, vss in grouping.items():
    sheet_name_orig = sheet_name = k[0].replace(" ", "")[0:25]
    
    if postfixes[sheet_name_orig.lower()]:
        sheet_name += " %02d" % postfixes[sheet_name_orig.lower()]
    postfixes[sheet_name_orig.lower()] += 1
    
    columns_in_use = [i for i, xs in enumerate(zip(*vss)) if any(x is not None for x in xs)]
    
    worksheet = workbook.add_worksheet(sheet_name)
    worksheet.write(0, 0, "ApplicableEntity", header_format)
    worksheet.write(1, 0, " ", header_format)
    for j, h in enumerate([k[col] for col in columns_in_use][1:]):
        worksheet.write(0, j + 1, h[0], header_format)
        worksheet.write(1, j + 1, ".".join(h[1]), header_format)
        
    for i, vs in enumerate(vss):
        for j, v in enumerate([vs[col] for col in columns_in_use]):
            worksheet.write(i + 2, j, format(v))
            
for h in sorted(postfixes.keys()):
    print(h)
            
workbook.close()
