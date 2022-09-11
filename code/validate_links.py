import os
import re

from urllib.parse import unquote

pat = re.compile(r'(href|src)="([^"]+)"')
hash = re.compile(r'#.+?$')
ignore_exts = ".py", ".png", ".jpg", ".jpeg", ".gif", ".zip", ".ico", ".js"

external = set()
non_existing = set()

for root, dirs, files in os.walk('.'):
    for nm in files:
        if "/.git" in root:
            continue

        if any(nm.lower().endswith(ext) or (ext+"?") in nm.lower() for ext in ignore_exts):
            continue

        fn = os.path.join(root, nm)
        base = os.path.dirname(fn)

        for _, pth in pat.findall(open(fn).read()):
            pth = unquote(pth)
            pth = hash.sub('', pth)
            if pth.startswith('mailto:'):
                continue
            elif pth.startswith('http://') or pth.startswith('https://'):
                external.add(pth)
                continue
            elif pth.startswith('/'):
                absolute = pth[1:]
            else:
                absolute = os.path.join(base, pth)

            if not os.path.exists(absolute):
                if '#' in absolute:
                    breakpoint()
                non_existing.add(absolute)

print("External")
for l in sorted(external):
    print(l)

print("404")
for l in sorted(non_existing):
    print(l)
