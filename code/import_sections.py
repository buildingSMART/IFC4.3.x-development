# imports the markdown definitions for sections from the bSI/IFC repository

import os
import sys
import glob

from collections import defaultdict

dr = sys.argv[1]
odr = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "docs")
odirs = {p.split(os.sep)[-1]:p for p in glob.glob(odr + "\\**", recursive=True) if os.path.isdir(p)}

md_files = glob.glob(os.path.join(dr, "**", "Documentation.md"), recursive=True)

for p in sorted(md_files, key=len):
    parts = p.split(os.sep)
    section = parts[-2]
    if " " in section:
        section = section.split(" ")[0].lower()
    if section in odirs:
        of = os.path.join(odirs[section], "README.md")
        print(p, "->", of)
        contents = open(p, encoding='utf-8-sig').read().strip()
        with open(of, "w", encoding="utf-8") as f:
            print(parts[-2], file=f)
            print("=" * len(parts[-2]), file=f)
            print(file=f)
            print(contents, file=f)
        