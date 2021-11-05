import re
import itertools
import functools

from dataclasses import dataclass, field

@dataclass
class xml_node:
    tag : str
    attributes : dict
    text : str = ""
    namespaces : dict = None
    children : list = field(default_factory=list, repr=False)
    parent : object = None

import lxml.etree as ET

IGNORED_ATTRS = ()
IGNORED_TAGS = ()
   
def flatmap(func, *iterable):
    return itertools.chain.from_iterable(map(func, *iterable))
    

def to_data(t, parent=None):
    if t.tag in IGNORED_TAGS:
        return

    children = list(flatmap(to_data, t))
    attributes = {k: v for k, v in (t.attrib or {}).items() if k not in IGNORED_ATTRS}
    
    text = ""
    if t.text and t.text.strip():
        text = t.text.strip()
        
    nd = xml_node(t.tag, attributes, text, t.nsmap, children)
    for ch in children:
        ch.parent = nd

    yield nd

    
def read(fn):
    parser = ET.XMLParser(encoding="utf-8")
    return next(to_data(ET.parse(fn, parser=parser).getroot()))


def serialize(di, ofn):
    def inner(d, parent=None):
        if parent is None:
            node = ET.Element(d.tag, nsmap=d.namespaces)
        else:
            node = ET.SubElement(parent, d.tag)

        if d.text:
            node.text = d.text
            
        for k, v in d.attributes.items():
            node.set(k, v)
            
        for child in d.children:
            inner(child, node)
                
        return node

    ET.ElementTree(inner(di[0])).write(ofn, pretty_print=True, xml_declaration=True)
