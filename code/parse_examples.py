import functools
import re
import os
import shutil
import sys
import json
import glob
import subprocess
import markdown
import bs4

def BeautifulSoup(*args):
    return bs4.BeautifulSoup(*args, features="lxml")

class ExamplesParser:
    def __init__(self, examples_dir):
        self.examples_by_type = {}
        self.examples_dir = examples_dir

    def parse(self):
        if not os.path.isdir(self.examples_dir):
            return
        examples = map(functools.partial(os.path.relpath, start=self.examples_dir), filter(os.path.isdir, glob.glob(os.path.join(self.examples_dir, "**", "*"), recursive=True)))
        ifcre = re.compile(r"IFC\w+")
        for example in examples:

            example_dir = os.path.join(examples_dir, example)
            
            if not glob.glob(os.path.join(example_dir, "*.ifc")) and not glob.glob(os.path.join(example_dir, "*.xml")):
                continue
            
            for ifc in glob.glob(os.path.join(example_dir, "*.ifc")):
                with open(ifc, "r") as f:
                    for ifc_class in ifcre.findall(f.read()):
                        self.examples_by_type.setdefault(str(ifc_class), set()).add(example.replace("\\", "/"))
            if not os.path.isfile(os.path.join(example_dir, "thumb.png")):
                rule = re.compile(r".*\.(png|jpg|jpeg)", re.IGNORECASE)
                for name in os.listdir(example_dir):
                    if rule.match(name):
                        args = [shutil.which("convert"), "-format", "png", "-resize", "300", name, "thumb.png"]
                        subprocess.call(args, cwd=example_dir)
                        break
                else:
                    # @todo
                    try:
                        md = open(os.path.join(example_dir, "README.md")).read()
                    except:
                        continue
                    soup = BeautifulSoup(markdown.markdown(md))
                    for img in soup.find_all("img"):
                        if img["src"].startswith("../../figures/examples"):
                            name = os.path.abspath(os.path.join('../docs', img["src"][6:]))
                            args = [shutil.which("convert"), "-format", "png", "-resize", "300", name, "thumb.png"]
                            if subprocess.call(args, cwd=example_dir) == 0:
                                break

if __name__ == "__main__":
    try:
        repo_dir = sys.argv[1]
    except:
        repo_dir = os.path.join(os.path.dirname(__file__), "..")

    examples_dir = os.path.join(repo_dir, "..", "examples", "models")
    examples_parser = ExamplesParser(examples_dir)
    examples_parser.parse()

    biggest_set = max(map(len, examples_parser.examples_by_type.values()))

    json.dump({k: list(v) for k, v in examples_parser.examples_by_type.items() if len(v) < (biggest_set / 2)}, open("examples_by_type.json", "w"), indent=2)
