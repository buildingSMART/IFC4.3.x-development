import os
import sys
import itertools

import lark

from github import Github

g = Github(os.environ["USER_AUTH"])
r = g.get_repo("buildingSMART/IFC4.3.x-output")

def alnum(s):
    return "".join(c for c in s if c.isalnum())

class issue:  
    def __init__(self, *args):
        self.len = self.format.count("%s")
        assert(len(args) == (self.len + 1) or len(args) == 0)
        
        self.data = (type(self).__name__,) + tuple(map(alnum, args[:-1]))
        self.body = args[-1] if len(args) else None
        
        parts = self.format.split("%s")
        parts = [p.strip() for p in parts]
        parts = list(itertools.chain(*zip(parts, ["WORD"] * len(parts))))[:-1]
        parts = [p for p in parts if p]
        parts = [(x if x == "WORD" else ('"%s"' % x)) for x in parts]
        
        self.grammar = lark.Lark("start: %s\n%%import common.WORD\n" % " ".join(parts))
        
    def __hash__(self):
        return hash(self.data)
        
    def __eq__(self, other):
        return self.data == other.data
        
    def construct(self):
        print("Creating issue:")
        print(self.format % self.data[1:])
        print("="*len(self.format % self.data[1:]))
        print(self.body)
        return g.create_issue(self.format % self.data[1:], body=self.body)
    
    def parse(self, issue):
        self.data = (type(self).__name__,) + tuple(map(str, self.grammar.parse(issue.title).children))
        

class missing_documentation_for_attribute(issue):
    format = "Entity %s has no documentation for attribute %s"

class missing_documentation_for_entity(issue):
    format = "Entity %s has no documentation"
    
issue_templates = [missing_documentation_for_entity, missing_documentation_for_attribute]

def parse_issue(i):
    for t in issue_templates:
        try:
            x = t()
            x.parse(i)
            return x
        except lark.exceptions.LarkError as e:
            return None


issues = list(r.get_issues(state='all'))
parsed_issues = map(parse_issue, issues)
parsable_issues = filter(lambda ab: ab[0] is not None, zip(parsed_issues, issues))
issue_mapping = dict(parsable_issues)

from xmi_document import xmi_document

try:
    fn = sys.argv[1]
except:
    print("Usage: python sanity_checker.py <schema.xml>", file=sys.stderr)
    exit()

def generate_issues():
    xmi_doc = xmi_document(fn)

    for item in xmi_doc:
        
        if item.type == "ENTITY":
            
            md = item.markdown_definition_html
            if not md:
                yield missing_documentation_for_entity(item.name, str(md))
                
            for child in item.children:
                
                md = child.markdown_definition_html
                if not md:
                    yield missing_documentation_for_attribute(item.name, child.name, str(md))
            
discovered_issues = set(generate_issues())

for old_issue, gh_handle in issue_mapping.items():
    open_on_gh = gh_handle.state == 'open'
    issue_exists = old_issue in discovered_issues
    if open_on_gh != issue_exists:
        gh_handle.edit(state='open' if issue_exists else 'closed')
    
for new_issue in discovered_issues - issue_mapping.keys():
    new_issue.construct()
