import os
import re
import glob
import platform
import tempfile
import operator
import itertools
import subprocess

from dataclasses import dataclass, field

import rdflib
import markdown

import append_xmi

from rdflib import Namespace
from rdflib.namespace import RDF
from rdflib.collection import Collection

import bs4
def BeautifulSoup(*args):
    return bs4.BeautifulSoup(*args, features='lxml')

def relative_path(*args):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *args))

SHACL = Namespace("http://www.w3.org/ns/shacl#")

@dataclass
class markdown_section:
    level : int
    heading : str
    content : str
    children : list = field(default_factory=list)
    
def parse_document(fn):
    soup = BeautifulSoup(
        markdown.markdown(open(fn, encoding="utf-8").read(),
        extensions=['tables', 'fenced_code', 'sane_lists'])
    )
    
    headings = soup.find_all(re.compile("h\d"))
    next_heading = headings[1:] + [None]
    
    root = None
    stack = [None]

    for h, next in zip(headings, next_heading):
        nodes = (n for n in h.nextSiblingGenerator())
        selected = itertools.takewhile(lambda n: next is None or n != next, nodes)
        strings = filter(None, map(lambda n: getattr(n, 'text', '').strip(), selected))
        concat = "".join(strings)
        
        section = markdown_section(int(h.name[1:]), h.text, concat)
        if section.level == len(stack):
            stack.append(None)
        elif section.level == len(stack) - 1:
            pass
        else:
            stack[section.level:] = [None]
            
        stack[-1] = section
        try:
            if stack[-2] is not None:
                stack[-2].children.append(section)
        except:
            print(fn)
            return None
        
        if root is None:
            root = section
            
    return root

def process_document(g, fn, subj, cls):
    g.add((subj, RDF.type, cls))
        
    fn_parts = list(map(rdflib.Literal, fn.replace("\\", "/")[len(base_path)+1:].split("/")))[::-1]
    c = Collection(g, fqdn(f"doc_{i}_filename"), fn_parts)
    g.add((subj, fqdn("hasFilename"), c.uri))
    
    def write(s, ct):
        g.add((s, fqdn("hasHeading"), rdflib.Literal(ct.heading)))
        if ct.content.strip():
            g.add((s, fqdn("hasText"), rdflib.Literal(ct.content)))
        
        for i, ch in enumerate(ct.children):
            s2 = s + f"_{i}"
            g.add((s2, fqdn("containedIn"), s))
            write(s2, ch)
        
    contents = parse_document(fn)
    if contents:
        write(subj, contents)
    

if not os.path.exists(os.path.join(tempfile.gettempdir(), "schema.ttl")):

    d = append_xmi.context(relative_path("../schemas/IFC.xml"))
    
    id_to_node = {}
    counter = {'c': 1}
    node_mapping = {}
    g = rdflib.Graph()

    def fqdn(s):
        if s.startswith("{"):
            return rdflib.URIRef("/".join(s[1:].split("}")))
        else:
            return rdflib.URIRef(f"http://example.org/ifc43Shapes/{s}")
    
    def v(nd, stack):
        if nd.tag == "{http://schema.omg.org/spec/XMI/2.1}Extension":
            return False

        nid = nd.attributes.get("{http://schema.omg.org/spec/XMI/2.1}id")
        if nid:
            id_to_node[nid] = nd
            
        s = fqdn(f"node_{counter['c']}")
        counter['c'] += 1
        node_mapping[nd] = s

    d._recurse(v)
    
    def v(nd, stack):
        if nd.tag == "{http://schema.omg.org/spec/XMI/2.1}Extension":
            return False
            
        s = node_mapping[nd]
        
        g.add((s, RDF.type, fqdn(nd.tag)))
            
        for k, v in nd.attributes.items():
            if v in id_to_node:
                g.add((s, fqdn(k), node_mapping[id_to_node[v]]))
            else:
                g.add((s, fqdn(k), rdflib.Literal(v)))
            
        if stack:
            g.add((s, fqdn("containedIn"), node_mapping[stack[-1]]))

    d._recurse(v)
    
    base_path = relative_path("..")
    
    for i,fn in enumerate(glob.glob(os.path.join(base_path, "docs/properties/**/*.md"), recursive=True)):
        process_document(g, fn, fqdn(f"doc_{i}"), fqdn("MarkdownPropertyDefinition"))

    for i,fn in enumerate(glob.glob(os.path.join(base_path, "docs/schemas/**/*.md"), recursive=True), start=i):
        process_document(g, fn, fqdn(f"doc_{i}"), fqdn("MarkdownResourceDefinition"))

    g.serialize(os.path.join(tempfile.gettempdir(), "schema.ttl"), format="turtle", encoding="utf-8")

VALIDATE_PATH = "shaclvalidate.sh"
if platform.system() == 'Windows':
    SHACL_PATH = os.environ.get("SHACL_HOME", os.path.join(os.path.abspath(os.path.dirname(__file__)), 'shacl-1.3.2'))
    VALIDATE_PATH = os.path.join(SHACL_PATH, 'bin', 'shaclvalidate.bat')
    
    if not os.path.exists(VALIDATE_PATH):
        raise RuntimeError(
            "Unable to find shaclvalidate \n"
            "Download shacl from https://repo1.maven.org/maven2/org/topbraid/shacl/1.3.2/shacl-1.3.2-bin.zip\n"
            "Extract and place in the this folder: \n" + 
            os.path.abspath(os.path.dirname(__file__))            
        )
        
    os.environ['SHACL_HOME'] = SHACL_PATH

proc = subprocess.Popen(
    [VALIDATE_PATH, "-datafile", os.path.join(tempfile.gettempdir(), "schema.ttl"), "-shapesfile", relative_path('shapes.ttl')],
    stdout=subprocess.PIPE)
stdout, stderr = proc.communicate()
stdout = stdout.decode('ascii')

g = rdflib.Graph()
g.parse(data=stdout, format="ttl")

results = []

with open(relative_path('../output/shacl-result.md'), "w") as f:

    for s,_,__ in g.triples((None, RDF.type, SHACL.ValidationResult)):
        for _,__, rM in g.triples((s, SHACL.resultMessage, None)):
            for _,__,sS in g.triples((s, SHACL.sourceShape, None)):
                results.append((sS, rM))
                
    for k, vs in itertools.groupby(sorted(results), key=operator.itemgetter(0)):
        f.write(f"## {k.split('#')[-1]}\n\n")
        for _, v in vs:
            f.write(f"* {v}\n")
        

# set PATH=C:\Program Files\Eclipse Adoptium\jdk-17.0.2.8-hotspot\bin;%PATH%
# set JAVA_HOME=C:\Program Files\Eclipse Adoptium\jdk-17.0.2.8-hotspot
# set JENA_HOME=C:\Apps\apache-jena-4.3.2
# C:\Apps\apache-jena-4.3.2\bat\shacl.bat validate -v --shapes shapes.ttl --data %TEMP%\schema.ttl
