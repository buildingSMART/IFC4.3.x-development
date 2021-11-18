import os
import sys
import time
import subprocess

XML_PATH = "/tmp/ifc43-xml"

try:
    os.makedirs(XML_PATH)
except: pass

while True:

    a = subprocess.check_output(["git", "rev-parse", "HEAD"])
    b = subprocess.check_output(["git", "pull"])
    c = subprocess.check_output(["git", "rev-parse", "HEAD"])
    
    if a != c or not os.listdir(XML_PATH):
    
        subprocess.call([sys.executable, "transform_to_xml.py", "../docs", XML_PATH])
        subprocess.call(["/solr-8.6.3/bin/solr", "create_core", "-force", "-c", "ifc"])
        subprocess.call(["/solr-8.6.3/bin/post", "-c", "ifc", XML_PATH])
        
        subprocess.call([sys.executable, "process_schema.py", "../schemas/IFC.xml" ])
        
    else:
    
        time.sleep(60)
