# imports the markdown definitions for properties from the bSI/IFC repository

import os
import sys
import glob

from collections import defaultdict

dr = sys.argv[1]
odr = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "docs", "properties")

prop_files = glob.glob(os.path.join(dr, "**", "Documentation.md"), recursive=True)
propname_from_path = lambda s: s.split(os.sep)[-2].split("_")[0]

prop_definitions = defaultdict(list)

for p in prop_files:
    # -sig is used to strip off the BOM
    prop_definitions[propname_from_path(p)].append(open(p, encoding='utf-8-sig').read().strip())

for nm, defs in prop_definitions.items():
    of = os.path.join(odr, nm[0].lower(), nm + ".md")
    # we just take the longest property definition in case of duplicates
    longest = max(defs, key=len)
    if not os.path.exists(os.path.dirname(of)):
        os.makedirs(os.path.dirname(of))
    with open(of, "w", encoding="utf-8") as f:
        print(nm, file=f)
        print("=" * len(nm), file=f)
        print(file=f)
        print(longest, file=f)
    