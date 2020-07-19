import os
import sys
import glob
import subprocess

def relative_path(*args):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *args))

reference_dir = os.path.join(os.path.dirname(__file__), "..", "reference_schemas")
scripts = "to_express", "to_po", "to_bsdd"
extensions = "exp", "po", "json"


for ffn in glob.glob(relative_path("..", "schemas", "*.xml")):
    fn = os.path.basename(ffn)
    print("Processing:", fn)
    if not os.path.exists(relative_path("..", "output")): os.makedirs(relative_path("..", "output"))
    for script, ext in zip(scripts, extensions):
        print("Running:", script)
        subprocess.call([sys.executable, relative_path(script + ".py"), ffn, relative_path("..", "output", fn[:-4] + "." + ext)])
    # subprocess.call([sys.executable, relative_path("process_schema.py"), ffn])
    