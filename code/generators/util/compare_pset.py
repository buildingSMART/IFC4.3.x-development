import glob
import os
import sys
import re
import itertools

from collections import defaultdict
from xml.etree import ElementTree as ET

from deepdiff import DeepDiff

# from pprint import pprint as print
    
IGNORED_TAGS = {'PsetDefinitionAliases', 'NameAliases', 'DefinitionAliases', 'ConstantList', 'QtoDefinitionAliases', 'Definition'}
IGNORED_ATTRS = {'ifdguid', 'version'}


    
def flatmap(func, *iterable):
    return itertools.chain.from_iterable(map(func, *iterable))
    

def to_dict(t):
    # strip out namespace reported by etree as
    # "{http://www.buildingsmart-tech.org/xml/qto/QTO_IFC4.xsd}QtoSetDef"
    items = {'#tag': re.sub(r'\{.+?\}', '', t.tag)}

    if items['#tag'] in IGNORED_TAGS:
        return
    
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

    f1, f2 = sys.argv[1:]
    assert os.path.isfile(f1) == os.path.isfile(f2)
    assert os.path.isdir(f1) == os.path.isdir(f2)
    assert os.path.isdir(f1) or os.path.isfile(f1)
    
    if os.path.isfile(f1):
        fs1 = [f1]
        fs2 = [f2]
    else:
        fs1 = set(map(os.path.basename, glob.glob(os.path.join(f1, '*.xml'))))
        fs2 = set(map(os.path.basename, glob.glob(os.path.join(f2, '*.xml'))))
        shared = fs1 & fs2
        if fs1 - shared:
            print('# Only in left:\n')
            for fn in sorted(fs1 - shared):
                print('-', fn)
            print()
        if fs2 - shared:
            print('# Only in right:\n')
            for fn in sorted(fs2 - shared):
                print('-', fn)
            print()
        fs1 = sorted(os.path.join(f1, fn) for fn in shared)
        fs2 = sorted(os.path.join(f2, fn) for fn in shared)

    for f1, f2 in zip(fs1, fs2):
        emitted_header = False

        t1, t2 = map(read, (f1, f2))
        result = DeepDiff(t1, t2, ignore_order=True, cutoff_intersection_for_pairs=0.5)

        for i, (ke, lbl) in enumerate([("iterable_item_added", "additions"), ("values_changed", "modifications"), ("iterable_item_removed", "deletions")]):
            di = result.to_dict().get(ke, {})
            
            if len(di):
                if not emitted_header:
                    print('#', os.path.basename(f1))
                    emitted_header = True

                print()
                print('##', lbl)
                print()
                
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
                    def escape(s):
                        return str(s).encode('ascii', 'xmlcharrefreplace').decode('ascii')\
                            .replace('<', '&lt;').replace('>', '&gt;')

                    if isinstance(value, str):
                        return escape(value)
                    elif isinstance(value, dict) and value.get('#tag'):
                        tag = escape(value.get('#tag'))
                        attrs = "".join(
                            ' %s="%s"' % (k[1:], escape(v).replace('"', '&quot;'))
                            for k, v in value.items()
                            if k.startswith('@')
                        )
                        text = escape(value.get('#text', '')) if value.get('#text') else ''
                        children = "".join(map(format, value.get('_children') or []))
                        return "&lt;%s%s&gt;%s%s&lt;/%s&gt;" % (tag, attrs, text, children, tag)
                    return str(value)

                print("*", " > ".join(flatmap(desc, evaled)))
                
                if i == 1:
                    old_new = v['old_value'], v['new_value']            
                    print(" ", "~~%s~~ %s" % tuple(map(format, old_new)))
                
            if di: print()
            