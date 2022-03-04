import re
import os
import sys
import glob
import operator
import itertools

from markdownify import markdownify as md
from bs4 import BeautifulSoup

import parse_mvd

concepts = sorted(parse_mvd.enumerate_concepts(sys.argv[1], with_rules=False))

for ent, ent_concepts in itertools.groupby(concepts, operator.attrgetter('entity')):

    print(ent)

    filenames = glob.glob(os.path.join("../docs/schemas", "*", "*", "*", ent + ".md"))     
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
        
        # MVD documentation is also markdown now so this segment
        # is obsolete
        # 
        # # Unwrap tables because images inside tables
        # # are not supported in Markdown.
        # #
        # # Also unwrap <a> as we post process that
        # # to links on the doc server
        # # 
        # # Also unwrap other styles such as <em> <b>
        # soup = BeautifulSoup(cp.definition, features="lxml")
        # for x in ("table", "thead", "tbody", "th", "tr", "td", "a", "em", "b"):
        #     for ref in list(soup.find_all(x)):
        #         ref.unwrap()
        # 
        # # Correct relative image paths
        # for img in soup.find_all("img"):
        #     img['src'] = re.sub("(../)+figures/", "../../../../figures/", img['src'])
        #
        # doc_content = md(str(soup))
        
        # Correct relative image paths
        doc_content = re.sub("(../)+figures/", "../../../../figures/", cp.definition)
        
        # remove underscored words:
        doc_content = re.sub("\\b_(\\w+?)_\\b", lambda m: m.group(1), doc_content) 
        
        data.append(doc_content)
        data.append("\n")
        data.append("\n")
        
        for doc_args in zip(cp.parameter_docs, *map(operator.itemgetter(1), sorted(cp.parameters.items()))):
            doc, args = doc_args[0], doc_args[1:]
            assert args
            if not doc:
                continue
                
            # remove underscored words:
            doc = re.sub("\\b_(\\w+?)_\\b", lambda m: m.group(1), doc) 
            
            data.append(f"#### {''.join(c for c in '_'.join(args) if c.isalnum() or c == '_')}\n\n")
            data.append(f"{doc}\n\n")
            
        
    with open(filename, "w", encoding="utf-8") as f:
        f.write("".join(data))
