import re
import os
import glob
import operator
import itertools

from markdownify import markdownify as md
from bs4 import BeautifulSoup

import parse_mvd

concepts = sorted(parse_mvd.enumerate_concepts(with_rules=False))

for ent, ent_concepts in itertools.groupby(concepts, operator.attrgetter('entity')):

    print(ent)
    
    # if ent == "IfcBuildingElement":
    #     ent == "IfcBuiltElement"

    filenames = glob.glob(os.path.join("../docs/schemas", "*", "*", "*", ent + ".md"))
    
    if not filenames:
        continue
        
    filename = filenames[0]
    
    with open(filename, "r", encoding="utf-8") as f:
        data = list(f)
        
        if "## Concepts" in (l.rstrip() for l in data):
           
            # Cut away existing concepts header
            data = data[0:[d.startswith("## Concepts") for d in data].index(True)]
            
            # Cut away trailing blank lines
            data = data[::-1]
            for l in list(data):
                if not l.strip():
                    data = data[1:]
                else:
                    break
            data = data[::-1]
            
        data.append("\n")
        data.append("## Concepts\n")
        data.append("\n")

    for cp in ent_concepts:
        print(cp.name)
    
        data.append("### %s\n" % cp.name)
        data.append("\n")
        
        # Unwrap tables because images inside tables
        # are not supported in Markdown.
        #
        # Also unwrap <a> as we post process that
        # to links on the doc server
        # 
        # Also unwrap other styles such as <em> <b>
        soup = BeautifulSoup(cp.definition, features="lxml")
        for x in ("table", "thead", "tbody", "th", "tr", "td", "a", "em", "b"):
            for ref in list(soup.find_all(x)):
                ref.unwrap()
        
        # Correct relative image paths
        for img in soup.find_all("img"):
            img['src'] = re.sub("(../)+figures/", "../../../../figures/", img['src'])
        
        data.append(md(str(soup)))
        data.append("\n")
        
    with open(filename, "w", encoding="utf-8") as f:
        f.write("".join(data))
