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

try:
    fn = sys.argv[1]
except:
    fn = "../mvdXML/IFC4_ADD2.mvdxml"

def dump(rule, parents, file=sys.stdout): print(" " * len(parents), "- ", rule.attribute, sep='', file=file)

roots = list(mvd.concept_root.parse(fn))

grouping = defaultdict(list)

for root in roots:
    for concept in root.concepts():
        parameters = defaultdict(list)
        for k, v in map(operator.attrgetter('a', 'c'), filter(lambda x: isinstance(x, expression_node), flatten(concept.rules()))):
            parameters[k].append(v)
            
        key = (concept.name,) + tuple(sorted(parameters.keys()))
        
        for vals in itertools.zip_longest(*parameters.values()):
            grouping[key].append((root.entity,) + tuple(vals))
            
        if len(parameters) == 0:
            grouping[key].append((root.entity,))
            
def format(v):
    if isinstance(v, str) and v[0] == "'" and v[-1] == "'":
        return v[1:-1]
    return v
    
workbook = xlsxwriter.Workbook('concepts.xlsx')
header_format = workbook.add_format({'bg_color': 'black', 'font_color': 'white'})
postfixes = defaultdict(int)
for k, vss in grouping.items():
    sheet_name = k[0].replace(" ", "")[0:25]
    if postfixes[k[0]]:
        sheet_name += " %02d" % postfixes[k[0]]
    postfixes[k[0]] += 1
    
    worksheet = workbook.add_worksheet(sheet_name)
    worksheet.write(0, 0, "ApplicableEntity", header_format)
    for j, h in enumerate(k[1:]):
        worksheet.write(0, j + 1, h, header_format)
        
    for i, vs in enumerate(vss):
        for j, v in enumerate(vs):
            worksheet.write(i + 1, j, format(v))
            
for h in sorted(postfixes.keys()):
    print(h)
            
workbook.close()
