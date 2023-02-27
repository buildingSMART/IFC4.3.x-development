import os
import sys
import time
import requests
import subprocess

XML_PATH = "/tmp/ifc43-xml"

try:
    os.makedirs(XML_PATH)
except: pass

REPO_DIR = os.environ.get("REPO_DIR", os.path.join(os.path.dirname(__file__), ".."))

while True:

    a = subprocess.check_output(["git", "-C", REPO_DIR, "rev-parse", "HEAD"])
    # do not require credentials for auto merge on pull
    # subprocess.check_output(["git", "-C", REPO_DIR, "pull"])
    subprocess.check_output(["git", "-C", REPO_DIR, "fetch"])
    subprocess.check_output(["git", "-C", REPO_DIR, "reset", "--hard", "origin/master"])
    c = subprocess.check_output(["git", "-C", REPO_DIR, "rev-parse", "HEAD"])
    
    first_time = not os.listdir(XML_PATH)
    
    if a != c or first_time:
    
        subprocess.call([sys.executable, "transform_to_xml.py", os.path.join(REPO_DIR, "docs"), XML_PATH])
        subprocess.call(["/solr-8.6.3/bin/solr", "create_core", "-force", "-c", "ifc"])
        subprocess.call(["/solr-8.6.3/bin/post", "-c", "ifc", XML_PATH])
        
        subprocess.call([sys.executable, "extract_concepts_from_xmi.py", os.path.join(REPO_DIR, "schemas/IFC.xml")])
        subprocess.call([sys.executable, "to_pset.py", os.path.join(REPO_DIR, "schemas/IFC.xml"), "psd/"])
        subprocess.call("zip ../psd.zip *", cwd="psd", shell=True)
        subprocess.call([sys.executable, "parse_xmi.py", os.path.join(REPO_DIR, "schemas/IFC.xml")])
        subprocess.call([sys.executable, "to_express.py", os.path.join(REPO_DIR, "schemas/IFC.xml"), "IFC.exp"])
        subprocess.call([sys.executable, "express_to_xsd.py", "IFC.exp", "IFC.xsd"])
        subprocess.call([sys.executable, "change_log.py", REPO_DIR])
        subprocess.call([sys.executable, "parse_examples.py", REPO_DIR])

        subprocess.call([sys.executable, "templates_to_mvdxml.py", 'IFC4.3.mvdxml', REPO_DIR])
        subprocess.call([sys.executable, "determine_mvd_scope.py", 'IFC.exp', 'IFC4.3.mvdxml'])
        
        subprocess.call([sys.executable, "process_schema.py", os.path.join(REPO_DIR, "schemas/IFC.xml")])
        
        if first_time:
            # First time. Spider the site to build indices in Redis. Then terminate.
            subprocess.call("wget -q --recursive --spider -S localhost:5000".split(" "))
            requests.post("http://localhost:5000/build_index")
            subprocess.call("redis-cli shutdown".split(" "))
    else:
        time.sleep(60)
