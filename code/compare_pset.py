import sys
import re
import itertools

from collections import defaultdict
from xml.etree import ElementTree as ET

from deepdiff import DeepDiff

# from pprint import pprint as print
    
IGNORED_TAGS = {'PsetDefinitionAliases', 'NameAliases', 'DefinitionAliases', 'ConstantList', 'QtoDefinitionAliases'}
IGNORED_ATTRS = {'ifdguid', 'version'}


    
def flatmap(func, *iterable):
    return itertools.chain.from_iterable(map(func, *iterable))
    

def to_dict(t):
    if t.tag in IGNORED_TAGS:
        return

    # strip out namespace reported by etree as
    # "{http://www.buildingsmart-tech.org/xml/qto/QTO_IFC4.xsd}QtoSetDef"
    items = {'#tag': re.sub(r'\{.+?\}', '', t.tag)}
    
    if list(t):
        items['_children'] = list(flatmap(to_dict, t))
    
    items.update({'@' + k: v for k, v in (t.attrib or {}).items() if k not in IGNORED_ATTRS})
        
    if t.text and t.text.strip():
        items['#text'] = t.text.strip()
        
    yield items
    
def read(fn):
    parser = ET.XMLParser(encoding="utf-8")
    return next(to_dict(ET.parse(fn, parser=parser).getroot()))

if __name__ == "__main__":

    t1, t2 = map(read, sys.argv[1:])
    result = DeepDiff(t1, t2,ignore_order=True)

    for i, (ke, lbl) in enumerate([("iterable_item_added", "additions"), ("values_changed", "modifications"), ("iterable_item_removed", "deletions")]):
        di = result.to_dict().get(ke, {})
        
        if len(di):
            print()
            print(lbl)
            print('-'*len(lbl))
            
        for k, v in di.items():
            # when added we need to look at t2
            root = t2 if i == 0 else t1
            
            parts = re.split(r"(?<=\])(?=\[)", k)
            parts = list(itertools.accumulate(parts))
            while parts:
                try:
                    evaled = list(map(eval, parts))
                    break
                except:
                    parts = parts[:-1]
                
            def desc(part):
                if isinstance(part, dict):
                    s = [] 
                    if part.get('#tag'):
                        s.append(part.get('#tag'))
                    if [c for c in (part.get('_children') or []) if c.get('#tag') == 'Name']:
                        t = [c for c in part.get('_children') if c.get('#tag') == 'Name'][0]["#text"]
                        s.append('[Name="%s"]' % t)
                    elif part.get('#text', '').strip():
                        s.append('"%s"' % part.get('#text', '').strip())
                    if s:
                        yield " ".join(s)\
                            .encode('ascii', 'xmlcharrefreplace').decode('ascii')
                            
            def format(value):
                if isinstance(value, str):
                    return value.encode('ascii', 'xmlcharrefreplace').decode('ascii')
                elif isinstance(value, dict) and value.get('#tag'):
                    return "&lt;%s&gt;" % value.get('#tag')
                return str(value)

            print("*", " > ".join(flatmap(desc, evaled)))
            
            if i == 1:
                old_new = v['old_value'], v['new_value']            
                print(" ", "~~%s~~ %s" % tuple(map(format, old_new)))
