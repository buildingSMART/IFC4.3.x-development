import os
import platform
import tempfile
import operator
import itertools
import subprocess

import rdflib

import append_xmi

from rdflib.namespace import RDF
from rdflib import Namespace

def relative_path(*args):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *args))

SHACL = Namespace("http://www.w3.org/ns/shacl#")

if not os.path.exists(os.path.join(tempfile.gettempdir(), "schema.ttl")):

    d = append_xmi.context(relative_path("../schemas/IFC.xml"))

    counter = {'c': 1}
    node_mapping = {}
    g = rdflib.Graph()

    def fqdn(s):
        if s.startswith("{"):
            return rdflib.URIRef("/".join(s[1:].split("}")))
        else:
            return rdflib.URIRef(f"http://example.org/{s}")

    def v(nd, stack):
        if nd.tag == "{http://schema.omg.org/spec/XMI/2.1}Extension":
            return False

        s = rdflib.URIRef(f"node_{counter['c']}")
        counter['c'] += 1
        node_mapping[nd] = s

        g.add((s, RDF.type, fqdn(nd.tag)))
            
        for k, v in nd.attributes.items():
            g.add((s, fqdn(k), rdflib.Literal(v)))
            
        if stack:
            g.add((s, fqdn("containedIn"), node_mapping[stack[-1]]))        

    d._recurse(v)

    g.serialize(os.path.join(tempfile.gettempdir(), "schema.ttl"), format="turtle")

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

with open("shacl-result.md", "w") as f:

    for s,_,__ in g.triples((None, RDF.type, SHACL.ValidationResult)):
        for _,__, rM in g.triples((s, SHACL.resultMessage, None)):
            for _,__,sS in g.triples((s, SHACL.sourceShape, None)):
                results.append((sS, rM))
                
    for k, vs in itertools.groupby(sorted(results), key=operator.itemgetter(0)):
        f.write(f"## {k.split('#')[-1]}\n\n")
        for _, v in vs:
            f.write(f"* {v}\n")
        
