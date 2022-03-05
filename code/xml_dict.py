import re
import sys
import itertools
import functools

from dataclasses import dataclass, field

@dataclass
class xml_node:
    tag : str
    attributes : dict = field(default_factory=dict)
    text : str = ""
    namespaces : dict = field(default=None, repr=False)
    children : list = field(default_factory=list, repr=False)
    parent : object = field(default=None, repr=False)
    
    def __hash__(self):
        return id(self)
        
    def child_with_tag(self, tag):
        cs = list(self.children_with_tag(tag))
        if cs:
            return cs[0]
                
    def children_with_tag(self, tag):
        for ch in self.children:
            if ch.tag == tag:
                yield ch
                
    def recursive_print(self, file=sys.stdout, level=0):
        attr_pairs = "".join(f' {k}="{v}"' for k, v in self.attributes.items())
        close = " /" if not (self.text or self.children) else ""
        indent = " " * (level*2)
        
        print(f"{indent}<{self.tag}{attr_pairs}{close}>", file=file)
        
        if self.text or self.children:
            if self.text:
                print(f"{indent}  {self.text}", file=file)
            for c in self.children:
                c.recursive_print(file=file, level=level+1)
                pass
                
            print(f"{indent}</{self.tag}>", file=file)
            

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
            node = ET.SubElement(parent, d.tag, nsmap=d.namespaces)

        if d.text:
            node.text = d.text
            
        for k, v in d.attributes.items():
            node.set(k, v)
            
        for child in d.children:
            inner(child, node)
                
        return node

    etree = ET.ElementTree(inner(di[0]))
    ET.indent(etree, "\t")
    etree.write(ofn, pretty_print=True, xml_declaration=True)
