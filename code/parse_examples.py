import re
import os
import sys
import json
import glob
import subprocess


class ExamplesParser:
    def __init__(self, examples_dir):
        self.examples_by_type = {}
        self.examples_dir = examples_dir

    def parse(self):
        if not os.path.isdir(self.examples_dir):
            return
        examples = map(os.path.basename, filter(os.path.isdir, glob.glob(os.path.join(self.examples_dir, "*"))))
        ifcre = re.compile(r"IFC\w+")
        for example in examples:
            example_dir = os.path.join(examples_dir, example)
            for ifc in glob.glob(os.path.join(example_dir, "*.ifc")):
                with open(ifc, "r") as f:
                    for ifc_class in ifcre.findall(f.read()):
                        self.examples_by_type.setdefault(str(ifc_class), set()).add(example)
            if not os.path.isfile(os.path.join(example_dir, "thumb.png")):
                rule = re.compile(r".*\.(png|jpg|jpeg)", re.IGNORECASE)
                for name in os.listdir(example_dir):
                    if rule.match(name):
                        args = ["convert", "-format", "png", "-resize", "300", name, "thumb.png"]
                        subprocess.call(args, cwd=example_dir)
                        break


if __name__ == "__main__":
    try:
        repo_dir = sys.argv[1]
    except:
        repo_dir = os.path.join(os.path.dirname(__file__), "..")

    examples_dir = os.path.join(repo_dir, "..", "examples", "IFC 4.3")
    examples_parser = ExamplesParser(examples_dir)
    examples_parser.parse()

    json.dump({k: list(v) for k, v in examples_parser.examples_by_type.items()}, open("examples_by_type.json", "w"), indent=2)
