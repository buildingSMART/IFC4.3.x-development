import os
import sys
import glob
import subprocess

def relative_path(*args):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *args))

reference_dir = relative_path("..", "reference_schemas")
scripts = "to_express", "to_po", "to_bsdd", "to_pset"
extensions = "exp", None, "json", None

# check PO file for non-unique keys with
# grep msgid ifc.pot | sort | uniq -d

for ffn in glob.glob(relative_path("..", "schemas", "*.xml")):
    fn = os.path.basename(ffn)
    print("Processing:", fn)
    
    if not os.path.exists(relative_path("..", "output", "psd")):
        os.makedirs(relative_path("..", "output", "psd"))
    
    for script, ext in zip(scripts, extensions):
        print("Running:", script)
        
        if ext is None:
            if script == "to_pset":
                output_path = relative_path("..", "output", "psd")
            else:
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
        
            for reference in ["IFC4x3_RC4.exp", "IFC4x3_RC4_43c3555.exp"]:
        
                subprocess.check_call([
                    sys.executable, 
                    "-m", "express_diff", 
                    os.path.join(reference_dir, reference),
                    relative_path("..", "output", fn[:-4] + "." + ext),
                    relative_path("..", "output", "%s-%s-differences.md" % (fn[:-4], reference[:-4]))
                ], cwd=relative_path("."))
                
            subprocess.check_call([
                sys.executable, 
                "express_to_xsd.py",
                output_path,
                output_path.replace("exp", "xsd")
            ], cwd=relative_path("."))
            
        elif script == "to_bsdd":
        
            subprocess.check_call([
                sys.executable, 
                relative_path("validate_bsdd.py"), 
                relative_path("..", "output", fn[:-4] + "." + ext)
            ])
            
        elif script == "to_pset":
            
            subprocess.check_call([
                sys.executable, 
                relative_path(script + ".py"), 
                "--compare",
                output_path,
                os.path.join(reference_dir, "psd"),
                relative_path("..", "output", fn[:-4] + "-psets.md")
            ])
            
    subprocess.check_call([sys.executable, relative_path("sanity_checker.py"), ffn])

    subprocess.check_call([sys.executable, relative_path("parse_xmi.py"), ffn])
    
    subprocess.check_call([sys.executable, relative_path("templates_to_mvdxml.py"), relative_path("..", "output", "IFC4.3.mvdxml")])
