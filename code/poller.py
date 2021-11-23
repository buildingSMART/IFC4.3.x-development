import os
import sys
import time
import subprocess

XML_PATH = "/tmp/ifc43-xml"

try:
    os.makedirs(XML_PATH)
except: pass

REPO_DIR = os.environ.get("REPO_DIR", os.path.join(os.path.dirname(__file__), ".."))

while True:

    a = subprocess.check_output(["git", "-C", REPO_DIR, "rev-parse", "HEAD"])
    b = subprocess.check_output(["git", "-C", REPO_DIR, "pull"])
    c = subprocess.check_output(["git", "-C", REPO_DIR, "rev-parse", "HEAD"])
    
    if a != c or not os.listdir(XML_PATH):
    
        subprocess.call([sys.executable, "transform_to_xml.py", os.path.join(REPO_DIR, "docs"), XML_PATH])
        subprocess.call(["/solr-8.6.3/bin/solr", "create_core", "-force", "-c", "ifc"])
        subprocess.call(["/solr-8.6.3/bin/post", "-c", "ifc", XML_PATH])
        
        subprocess.call([sys.executable, "extract_concepts_from_xmi.py", os.path.join(REPO_DIR, "schemas/IFC.xml")])
        subprocess.call([sys.executable, "to_pset.py", os.path.join(REPO_DIR, "schemas/IFC.xml"), "psd/"])
        subprocess.call([sys.executable, "parse_xmi.py", os.path.join(REPO_DIR, "schemas/IFC.xml")])
        subprocess.call([sys.executable, "parse_mvd.py", os.path.join(REPO_DIR, "mvdXML/IFC4_ADD2.mvdxml")])
        subprocess.call([sys.executable, "change_log.py", REPO_DIR])
        
        subprocess.call([sys.executable, "process_schema.py", os.path.join(REPO_DIR, "schemas/IFC.xml")])
        
    else:
    
        time.sleep(60)
