import os
import re
import glob
import uuid
import datetime
import operator
import traceback

from collections import defaultdict
from xml.etree import ElementTree as ET

import bs4
import markdown
import networkx
import xmlschema

from xmi_document import SCHEMA_NAME

def BeautifulSoup(*args):
    return bs4.BeautifulSoup(*args, features='lxml')

schema_name = SCHEMA_NAME.split('_')[0]
try:
    schema_name_postfix = SCHEMA_NAME.split('_')[1]
except:
    schema_name_postfix = ''

mvd_s = xmlschema.XMLSchema(os.path.join(os.path.dirname(__file__), 'mvdXML_V1.1_add1.xsd'))

def generate_uuid():
    return str(uuid.uuid4())

def read_scope():
    return "bladibla"

roots = []

concept_mapping = {}
root_level_concepts = {}

fns = glob.glob(os.path.join(os.path.dirname(__file__), "../docs/templates/**/README.md"), recursive=True)
for fn in sorted(fns, key=len):
    path = os.path.normpath(fn).split(os.sep)[:-1]
    
    parent = path[-2]
    name = path[-1]
        
    txt = open(fn, encoding='utf-8').read()
    soup = BeautifulSoup(markdown.markdown(txt))
    
    try:
        soup.h1.decompose()
    except:
        print(fn)
        traceback.print_exc()
        
    try:
        soup.code.decompose()
    except:
        print(fn)
        traceback.print_exc()
    
    concept_blocks = re.findall(r"concept\s*\{.+?\}", txt, flags=re.S)
    rules = None
    root = None
    
    if concept_blocks:
        block = concept_blocks[0]

        edges = re.findall("([\:\w]+)\s*\->\s*([\:\w]+)", block)
        rule_bindings = dict(re.findall(r'(\w+:\w+)\[binding="(.+?)"\]', block))
                
        rules = {}
        G = networkx.DiGraph()

        for a,b in edges:
            rb = rule_bindings.get(a)
            attr = a.split(':')[1] if ':' in a else None
            a,b = map(lambda x: x.split(':')[0], (a,b))
            if attr:
                G.add_edge(a, f'{attr}_{a}')
                G.add_edge(f'{attr}_{a}', b)
                G.nodes[f'{attr}_{a}']['type'] = 'AttributeRule'
                G.nodes[f'{attr}_{a}']['binding'] = rb
            else:
                G.add_edge(a, b)

        if len(G):
            root = min(G.in_degree(), key=operator.itemgetter(1))[0]                 

            Gadj = networkx.to_dict_of_lists(G)

            def build(x, at=rules):
                ty = G.nodes[x].get('type', 'EntityRule')
                ruleid = G.nodes[x].get('binding')
                other_ty = next(iter({'EntityRule', 'AttributeRule'} - {ty}))

                if not ty in at:
                    at[ty] = []
                    
                at[ty].append({
                    '@' + ty.replace('Rule', 'Name'): x.split("_")[0] if "_" in x else x,
                })
                
                if Gadj[x]:
                    # only initiate next level if we have out edges
                    child = {}
                    at[ty][-1][f'{other_ty}s'] = child
                    
                if ruleid:
                    at[ty][-1]['@RuleID'] = ruleid
                    
                for k in Gadj[x]:
                    build(k, child)

            build(root)

            rules = list(rules.values())[0][0]['AttributeRules']

    di = {
        '@applicableEntity': [root],
        '@applicableSchema': [schema_name],
        '@name': name,
        '@status': 'sample',
        '@uuid': generate_uuid(),
        'Definitions': {
            'Definition': {
                'Body': {
                    '$': soup.body.encode_contents().decode('utf-8'),
                    '@lang': 'en'
                }
            }
        },
        'Rules': rules
    }
        
    concept_mapping[name] = di
    
    if parent == 'docs':
        continue
    elif parent == 'templates':
        root_level_concepts[name] = di
    else:
        sub = concept_mapping[parent]['SubTemplates'] = concept_mapping[parent].get('SubTemplates', {'ConceptTemplate': []}) 
        li = sub['ConceptTemplate']
        li.append(di)
        
templates = [a[1] for a in sorted(root_level_concepts.items())]

dict = {
    '@name': '',
    '@status': 'sample',
    '@uuid': generate_uuid(),
    '@xmlns': 'http://buildingsmart-tech.org/mvd/XML/1.1',
    '@xmlns:xsd': 'http://www.w3.org/2001/XMLSchema',
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    '@xsi:schemaLocation': 'http://www.buildingsmart-tech.org/mvd/XML/1.1 http://www.buildingsmart-tech.org/mvd/XML/1.1/mvdXML_V1.1_add1.xsd',
    'Templates': {
        'ConceptTemplate': templates
    },
    'Views': {
        'ModelView': [{
            '@applicableSchema': schema_name, 
            '@code': schema_name,
            '@copyright': f'&copy; {datetime.datetime.now().year} buildingSMART International Ltd.',
            '@name': 'General Usage',
            '@owner': 'bSI',
            '@status': 'sample',
            '@uuid': generate_uuid(),
            '@version': schema_name_postfix,
            'Definitions': {
                'Definition': [{
                    'Body': {
                        '$': read_scope(),
                        '@lang': 'en'
                    },
                }]
            },
            'Roots': {
                'ConceptRoot': roots
            }
        }]
    }
}

elem, errors = mvd_s.encode(dict, validation='lax')

ET.register_namespace("", dict['@xmlns'])
ET.ElementTree(elem).write(f'{schema_name}.mvdxml', encoding="utf-8", xml_declaration=True)

if errors:
    for e in []: # errors:
        print(e)
    exit(1)