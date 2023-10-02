import itertools
import operator
import re
import subprocess
import markdown
from bs4 import BeautifulSoup

soup = BeautifulSoup(markdown.markdown(open('../content/terms_and_definitions.md', encoding='utf-8').read()))
terms = [x.text for x in soup.find_all('h3')]

for term in terms:
    print(term)
    print('-' * len(term))
    proc = subprocess.run(['grep', '-wiR', term, 'docs', 'content'], cwd='..', capture_output=True)
    docs = itertools.groupby(sorted(y for y in [x.split(':', 1) for x in proc.stdout.decode('utf-8').split('\n')] if len(y[0])), key=operator.itemgetter(0))
    has_any = False
    for d, ls in docs:
        ls = list(l[1] for l in ls)
        if not d.lower().endswith('.md'):
            continue
        if all(l.startswith('#') for l in ls):
            continue
        print('*', d)
        for l in ls:
            if l.startswith('#'):
                continue
            print('    *', re.sub(r'([^\w\.\,\s])', r'\\\1' , l))
            has_any = True
    
    if not has_any:
        print('*NONE*')

    print('\n\n')