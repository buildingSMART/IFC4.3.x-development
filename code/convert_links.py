import os
import re

pat = re.compile(r'''(?P<attr>href|src)=("|')(https?://(localhost|app:5000))?/(?P<path>[^"']+)("|')''')
ignore_exts = ".py", ".png", ".jpg", ".jpeg", ".gif", ".zip", ".ico", ".woff"

for root, dirs, files in os.walk('.'):
    for nm in files:
        if "/.git" in root:
            continue
        
        if any(nm.lower().endswith(ext) for ext in ignore_exts):
            continue
        
        fn = os.path.join(root, nm)
        base = os.path.dirname(fn)
        
        def repl(href):            
            repl = '%s="%s"' % (href.group('attr'), os.path.relpath(href.group('path'), base))
            print('in', root)
            print('-', href.group(0))
            print('+', repl)
            print()
            return repl

        print(fn)            
        with open(fn, encoding='utf-8') as f:
            S0 = f.read()
        
        S1 = pat.sub(repl, S0)
        
        if S0 != S1:
            with open(fn, 'w', encoding='utf-8') as f:
                f.write(S1)
