import os
import sys
import glob
import subprocess

def relative_path(*args):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *args))

reference_dir = relative_path("..", "reference_schemas")
scripts = "to_express", "to_po", "to_bsdd"
extensions = "exp", None, "json"

# check PO file for non-unique keys with
# grep msgid ifc.pot | sort | uniq -d

for ffn in glob.glob(relative_path("..", "schemas", "*.xml")):
    fn = os.path.basename(ffn)
    print("Processing:", fn)
    
    if not os.path.exists(relative_path("..", "output")):
        os.makedirs(relative_path("..", "output"))
    
    for script, ext in zip(scripts, extensions):
        print("Running:", script)
        
        if ext is None:
            output_path = relative_path("..", "output")
        else:
            output_path = relative_path("..", "output", fn[:-4] + "." + ext)
        
        subprocess.check_call([
            sys.executable, 
            relative_path(script + ".py"), 
            ffn, 
            output_path
        ])
        if script == "to_express":
        
            subprocess.check_call([
                sys.executable, 
                "-m", "express_diff", 
                os.path.join(reference_dir, "IFC4x3_RC2.exp"),
                relative_path("..", "output", fn[:-4] + "." + ext),
                relative_path("..", "output", fn[:-4] + "." + ext + ".md")
            ], cwd=relative_path("."))
            
        elif script == "to_bsdd":
        
            subprocess.check_call([
                sys.executable, 
                relative_path("validate_bsdd.py"), 
                relative_path("..", "output", fn[:-4] + "." + ext)
            ])
            
    subprocess.check_call([sys.executable, relative_path("sanity_checker.py"), ffn])

    # subprocess.check_call([sys.executable, relative_path("process_schema.py"), ffn])
    