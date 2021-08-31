import re
import os
import glob
import json
import hashlib
import operator
import itertools
import subprocess

from collections import defaultdict

import tabulate
import pydot
import pysolr
import markdown

from bs4 import BeautifulSoup

from flask import Flask, send_file, render_template, abort, url_for, request, send_from_directory, jsonify

import md as mdp

app = Flask(__name__)

base = '/IFC/RELEASE/IFC4x3/HTML'

def make_url(fragment): return base + '/' + fragment

entity_attributes = json.load(open("entity_attributes.json", encoding="utf-8"))
entity_definitions = json.load(open("entity_definitions.json", encoding="utf-8"))
entity_to_package = json.load(open("entity_to_package.json", encoding="utf-8"))
entity_supertype = json.load(open("entity_supertype.json", encoding="utf-8"))
changes_by_type = json.load(open("changes_by_type.json", encoding="utf-8"))
concepts = json.load(open("concepts.json", encoding="utf-8"))

navigation_entries = [
    ("Cover", "Contents", "Foreword", "Introduction"),
    ("Scope", "Normative references", "Terms, definitions, and abbreviated terms", "Fundamental concepts and assumptions"),
    ("Core data schemas", "Shared element data schemas", "Domain specific data schemas", "Resource definition data schemas"),
    ("Computer interpretable listings", "Alphabetical listings", "Inheritance listings", "Diagrams"),
    ("Examples", "Change logs", "Bibliography", "Index")
]

content_names = ['scope','normative_references','terms_and_definitions','concepts']
content_names_2 = ['cover','foreword','introduction','bibliography']

def to_dict(x):
    if isinstance(x, (list, tuple)):
        return type(x)(map(to_dict, x))
    else:
        return {"title": x}

def make_entries(x):
    md_root = "../docs/schemas"
    categories = [d for d in os.listdir(md_root) if os.path.isdir(os.path.join(md_root, d))]
        
    if isinstance(x, (list, tuple)):
        return type(x)(map(make_entries, x))
    
    elif x['title'] == 'Alphabetical listings':
        url = make_url('listing')
    elif x['title'] == 'Contents':
        url = make_url('toc.html')
    elif x['number'] == 4:
        url = make_url('concepts/content.html')
    elif type(x['number']) == int:
        if  x['number'] >= 5:
            url = make_url('chapter-%d/' % x['number'])
        else:
            url = make_url('content/' + content_names[x['number'] - 1] + '.htm')
    elif x['number'] in {'A', 'C', 'D', 'E', 'F'}:
        url = make_url('annex-%s.html' % x['number'].lower())
    elif x['title'].lower() in content_names_2:
        url = make_url('content/' + x['title'].lower() + '.htm')
    else:
        url = '#'
    
    return dict(**x, url=url)

def make_counter(start=0):
    n = start
    def counter():
        nonlocal n
        n += 1
        if n > 14:
            return None
        if n > 8:
            return chr(ord('A') + n - 9)
        elif n >= 1:
            return n
    return counter
    
section_counter = make_counter(-4)
        
def number_entries(x):
    if isinstance(x, (list, tuple)) and set(map(type, x)) == {dict}:
        return type(x)(dict(**di, number=section_counter()) for i, di in enumerate(x))
    else:
        return type(x)(map(number_entries, x))
        
navigation_entries = make_entries(number_entries(to_dict(navigation_entries)))

def chapter_lookup(number=None, cat=None):

    def do_chapter_lookup(x):
        if isinstance(x, (list, tuple)):
            return next((v for v in map(do_chapter_lookup, x) if v is not None), None)
        if number is not None and x['number'] == number:
            return x
        if cat is not None and x['title'].split(" ")[0].lower() == cat:
            return x
            
    return do_chapter_lookup(navigation_entries)

hierarchy = json.load(open("hierarchy.json"))

entity_names = sorted(sum([schema.get('Entities', []) for _, cat in hierarchy for __, schema in cat], []))
type_names = sorted(sum([schema.get('Types', []) for _, cat in hierarchy for __, schema in cat], []))

name_to_number = {}

for i, (cat, schemas) in enumerate(hierarchy, start=5):
    for j, (schema_name, members) in enumerate(schemas, start=1):
        for k, ke in enumerate(["Types", "Entities"], start=2):
            for l, name in enumerate(members.get(ke, ()), start=1):
                name_to_number[name] = ".".join(map(str, (i,j,k,l)))

def generate_inheritance_graph(current_entity):
    i = current_entity
    g = pydot.Graph('dot_inheritance', directed=True)
    di = {
        'rankdir': 'BT',
        'ranksep': 0.2
    }
    for kv in di.items():
        g.set(*kv)

    previous = None
    while i:
        n = pydot.Node(i)
        di = {
            'color':'black',
            'fillcolor':'grey43',
            'fontcolor':'white',
            'fontsize': '10',
            'height':'0.2',
            'shape':'rectangle',
            'style':'filled',
            'width':'3',
        }
        for kv in di.items():
            n.set(*kv)
        g.add_node(n)
    
        if previous:
            g.add_edge(pydot.Edge(previous, n, arrowhead="onormal"))
            
        previous = n
        
        i = entity_supertype.get(i)
        
    return g.to_string()
    

def get_node_colour(n):
    if entity_supertype.get(n) is None:
        return 'gray'

    def is_relationship(ty=n):
        if ty == "IfcRelationship":
            return True
        ty = entity_supertype.get(ty)
        if ty:
            return is_relationship(ty)
        return False
    
    return 'yellow' if is_relationship() else 'dodgerblue'


def transform_graph(current_entity, graph_data, only_urls=False):
    graphs = pydot.graph_from_dot_data(graph_data)
    
    # collect all node names to see if we need to insert args in cluster
    
    all_nodes = set()
    
    def collect_nodes(g):
        all_nodes.update(n.get_name() for n in g.get_nodes())
        for sg in g.get_subgraphs():
            collect_nodes(sg)
    
    for graph in graphs:
        collect_nodes(graph)
        
    # now visit graph and decorate nodes
    
    def visit_graph(g):
        names_seen = {}
        
        edge_nodes_in_cluster = set()
        
        for e in g.get_edges():
            edge_nodes_in_cluster.add(e.get_source())
            edge_nodes_in_cluster.add(e.get_destination())
            
        # add nodes to cluster that aren't explicitly declared
        # in the graph
        for n in (edge_nodes_in_cluster - all_nodes):
            g.add_node(pydot.Node(n))
        
        for n in g.get_nodes():
            nm = n.get_label() or n.get_name()
            
            if nm in {'graph', 'edge', 'node'}: continue
                
            if not only_urls:            
                
                if n.get_name() in names_seen:
                    # rank=same groupings otherwise cause
                    # node names to be listed twice
                    args = names_seen[n.get_name()]
                
                else:
                    args = {
                        'fillcolor': get_node_colour(nm),
                        'shape': 'box',
                        'style': 'filled'
                    }
                    
                    if n.get_name() == current_entity:
                        args['color'] = 'red'
                    
                    names_seen[n.get_name()] = args
                    
                for kv in args.items():
                    print(nm, *kv)
                    n.set(*kv)
                
            n.set('URL',  url_for('resource', resource=nm, _external=True))
            
        for sg in g.get_subgraphs():
            visit_graph(sg)
            
    for graph in graphs:
        visit_graph(graph)
        
    return graph.to_string()


def process_graphviz(current_entity, md):
    def is_figure(s):
        if 'dot_figure' in s:
            return 1
        elif 'dot_inheritance' in s:
            return 2
        else:
            return 0
        
    graphviz_code = filter(is_figure, re.findall('```(.*?)```', md, re.S))
    
    for c in graphviz_code:
        hash = hashlib.sha256(c.encode('utf-8')).hexdigest()
        fn = os.path.join('svgs', current_entity + "_" + hash+'.dot')
        c2 = transform_graph(current_entity, c, only_urls=is_figure(c) == 2)
        with open(fn, "w") as f:
            f.write(c2)
        md = md.replace("```%s```" % c, '![](/svgs/%s_%s.svg)' % (current_entity, hash))
        subprocess.call(["dot", "-O", "-Tsvg", fn])
    
    return md    


def create_entity_definition(e):
    table = [(e, "")]
    while e:
        keys = [x for x in entity_attributes.keys() if x.startswith(e + '.')]
        for k, (is_fwd, ty) in zip(keys, map(entity_attributes.__getitem__, keys)):
            nm = k.split('.')[1]
            
            if is_fwd:
                card = "[0:1]" if "OPTIONAL" in ty else "[1:1]"
            else:
                # nm = "<i>%s</i>" % nm
                inv_card = re.findall(r'(\[.+?\])', ty)
                if inv_card:
                    card = inv_card[0]
                else:
                    card = ""
            
            table.append((nm, card))
        e = entity_supertype.get(e)
        
    table = "<<table border=\"1\" cellborder=\"0\" cellspacing=\"0\">%s</table>>" % \
        "".join("<tr>%s</tr>" % "".join("<td width=\"%d\" height=\"24\" fixedsize=\"true\" bgcolor=\"%s\" align=\"left\" port=\"%s%d\">%s</td>" % ([20,250][i==0],["white", "gray"][ri==0],r[0],i,c) for i,c in enumerate(r)) for ri, r in enumerate(table))
    
    return table


def process_graphviz_concept(name, md):
    graphviz_code = filter(lambda s: s.strip().startswith("concept"), re.findall('```(.*?)```', md, re.S))
    
    for c in graphviz_code:
        
        hash = hashlib.sha256(c.encode('utf-8')).hexdigest()
        fn = os.path.join('svgs', name + "_" + hash + '.dot')
        c2 = c.replace("concept", "digraph")  # transform_graph(current_entity, c, only_urls=is_figure(c) == 2)
        
        nodes = set(n.split(':')[0] for n in (re.findall('([\:\w]+)\s*\->', c2) + re.findall('\->\s*([\:\w]+)', c2)))
        
        c2 = re.sub(r'(\w+)\:(\w+)\s*\->\s*([\:\w]+)', lambda m: f"{m.group(1)}:{m.group(2)}1 -> {m.group(3)}", c2)
        c2 = re.sub(r'([\w\:]+)\s*\->\s*(\w+)\:(\w+)', lambda m: f"{m.group(1)} -> {m.group(2)}:{m.group(3)}0", c2)
        
        G = pydot.graph_from_dot_data(c2)[0]
        
        G.set_node_defaults(shape='plaintext', width='3')
        G.set_nodesep('0.1')
        G.set_splines('polyline')
        G.set_rankdir('LR')
                        
        for n in nodes:
            G.add_node(pydot.Node(n, label=create_entity_definition(n)))
            
        # this is ugly, but the node defaults need to come before the edges
        G.obj_dict["nodes"]['node'][0]['sequence'] = -1
            
        c3 = G.to_string()
        
        with open(fn, "w") as f:
            f.write(c3)
        md = md.replace("```%s```" % c, '![](/svgs/%s_%s.svg)' % (name, hash))
        
        print("dot", "-O", "-Tsvg", fn)
        print("svg", subprocess.call(["dot", "-O", "-Tsvg", fn]))
    
    return md 

    
"""
@app.route('/svgs/<entity>/<hash>.svg')
def get_svg(entity, hash):
    return send_from_directory('svgs', entity + "_" + hash + '.dot.svg');
"""

@app.route(make_url('figures/<fig>'))
def get_figure(fig):
    return send_from_directory('../docs/figures', fig)


DOC_ANNOTATION_PATTERN = re.compile(r'\{\s*\..+?\}')
    
class builder:
    
    def __init__(self, resource, md_root=None):
    
        """
        package = entity_to_package.get(resource)
        if not package:
            abort(404)
        """
            
        md = None    
        self.md_root = md_root or "../docs/schemas"
        
        # @todo eliminate this glob pattern approach
        
        # for category in os.listdir(md_root):
        #     for module in os.listdir(os.path.join(md_root, category)):
        #         if module == package:
        
        self.md = os.path.join("../docs/schemas", "*", "*", "*", resource + ".md")
        self.resource = resource
    
        
    @property
    def markdown(self):
        fns = glob.glob(self.md)
        if not fns: return ''
        with open(fns[0], 'r', encoding='utf-8') as f:
            return re.sub(DOC_ANNOTATION_PATTERN, '', "\n".join(f.readlines()[2:]))
            
    @property
    def attributes(self):
        attrs = []
        supertype_counts = []
        fwd_attrs = []
        
        ty = self.resource
        while ty:
            md_ty_fn = glob.glob(os.path.join("../docs/schemas", "*", "*", "*", ty + ".md"))[0]
            md_ty = re.sub(DOC_ANNOTATION_PATTERN, '', open(md_ty_fn, encoding='utf-8').read())
            ty_attrs = list(mdp.markdown_attribute_parser(md_ty))
            supertype_counts.append((ty, len(ty_attrs)))
            for a, b in ty_attrs[::-1]:
                is_fwd, attr_ty = entity_attributes.get(".".join((ty, a)), (False, "INVALID"))
                attrs.append((
                    a, attr_ty, re.sub(
                        "\\n+", 
                        "<br><br>",
                        # remove underscored words:
                        re.sub("_(\\w+?)_", lambda m: m.group(1), b.strip()) 
                        # keep underscored words:
                        # b.strip()             
                        # convert to links (todo attributes):                   
                        # re.sub("_(\\w+?)_", lambda m: "<a href='%s'>%s</a>" % (url_for('resource', resource=m.group(1)), m.group(1)), b.strip())
                )))
                if is_fwd:
                    fwd_attrs.append(a)
            ty = entity_supertype.get(ty)
            
        attr_index = {b:a for a,b in enumerate(fwd_attrs[::-1], 1)}
        attrs = [(attr_index.get(b,''),b,c,d) for b,c,d in attrs[::-1]]
        
        return attrs
            
    
@app.route('/api/v0/resource/<resource>')
def api_resource(resource):
    b = builder(resource)
    definition = b.markdown
    if "\n\n" in definition:
        definition = definition[0:definition.index("\n\n")]
    definition = markdown.markdown(definition)
    return jsonify({
        'resource': resource,
        'definition': definition,
        'attributes': b.attributes
    });
      

@app.route(make_url('lexical/<resource>.htm'))
def resource(resource):
    try:
        idx = name_to_number[resource]
    except:
        abort(404)
        
    doc_annotation_pattern = re.compile(r'\{\s*\..+?\}')

    """
    package = entity_to_package.get(resource)
    if not package:
        abort(404)
    """
        
    md = None    
    md_root = "../docs/schemas"
    # for category in os.listdir(md_root):
    #     for module in os.listdir(os.path.join(md_root, category)):
    #         if module == package:
    
    md = os.path.join("../docs/schemas", "*", "*", "*", resource + ".md")
    
    html = ''
    
    paragraph = 1
                
    if glob.glob(md):
        
        md = glob.glob(md)[0]
        
        attribute_table = ''
        
        with open(md, 'r', encoding='utf-8') as f:
    
            mdc = re.sub(doc_annotation_pattern, '', f.read())
            
            if "Entities" in md:
            
                if "## Attributes" in mdc:
                    mdc = mdc[0:mdc.index("## Attributes")]
                    mdc += '\n\n' + idx + '.%d Attributes\n===========\n\n' % paragraph
                    paragraph += 1
                
                attrs = []
                supertype_counts = []
                fwd_attrs = []
                
                ty = resource
                while ty:
                    md_ty_fn = glob.glob(os.path.join("../docs/schemas", "*", "*", "*", ty + ".md"))[0]
                    md_ty = re.sub(doc_annotation_pattern, '', open(md_ty_fn, encoding='utf-8').read())
                    ty_attrs = list(mdp.markdown_attribute_parser(md_ty))
                    supertype_counts.append((ty, len(ty_attrs)))
                    for a, b in ty_attrs[::-1]:
                        is_fwd, attr_ty = entity_attributes.get(".".join((ty, a)), (False, "INVALID"))
                        attrs.append((
                            a, attr_ty, re.sub(
                                "\\n+", 
                                "<br><br>",
                                # remove underscored words:
                                re.sub("_(\\w+?)_", lambda m: m.group(1), b.strip()) 
                                # keep underscored words:
                                # b.strip()             
                                # convert to links (todo attributes):                   
                                # re.sub("_(\\w+?)_", lambda m: "<a href='%s'>%s</a>" % (url_for('resource', resource=m.group(1)), m.group(1)), b.strip())
                        )))
                        if is_fwd:
                            fwd_attrs.append(a)
                    ty = entity_supertype.get(ty)
                    
                attr_index = {b:a for a,b in enumerate(fwd_attrs[::-1], 1)}
                attrs = [(attr_index.get(b,''),b,c,d) for b,c,d in attrs[::-1]]
            
                attribute_table = tabulate.tabulate(attrs, headers=("#", "Attribute", "Type", "Description"), tablefmt='unsafehtml')
                soup = BeautifulSoup(attribute_table)
                insertion_points = [0] + list(itertools.accumulate(map(operator.itemgetter(1), supertype_counts[::-1])))[:-1]
                trs = list(soup.findAll('tr'))
                for tridx, (ty, _) in zip(insertion_points, supertype_counts[::-1]):
                    tr = soup.new_tag('tr')
                    td = soup.new_tag('td', colspan=4)
                    a = soup.new_tag('a', href=url_for('resource', resource=ty))
                    a.string = ty
                    td.append(a)
                    tr.append(td)
                    trs[tridx+1].insert_before(tr)
                attribute_table = str(soup)
                    
                mdc += "\n\nattribute_table\n\n"
                
                try:
                    mdc += '\n\n' + idx + '.%d Entity inheritance\n===========\n\n```' % paragraph + generate_inheritance_graph(resource) + '```'
                    paragraph += 1
                except:
                    pass
    
            html = markdown.markdown(
                process_graphviz(resource, mdc),
                extensions=['tables', 'fenced_code'])
                
            html = html.replace("attribute_table", attribute_table)
        
            soup = BeautifulSoup(html)
        
            # First h1 is handled by the template
            try:
                soup.find('h1').decompose()
            except:
                # only entities have H1?
                pass
        
            hs = []
            # Renumber the headings
            for i in list(range(7))[::-1]:
                for h in soup.findAll('h%d' % i):
                    h.name = 'h%d' % (i + 2)
                    hs.append(h)
                
            # Change svg img references to embedded svg
            # because otherwise URLS are not interactive
            for img in soup.findAll("img"):
                if img['src'].endswith('.svg'):
                    print(img['src'].split('/')[-1].split('.')[0])
                    entity, hash = img['src'].split('/')[-1].split('.')[0].split('_')
                    svg = BeautifulSoup(open(os.path.join('svgs', entity + "_" + hash + '.dot.svg')))
                    img.replaceWith(svg.find('svg'))
                else:
                    img['src'] = img['src'][9:]
        
            scs = changes_by_type.get(resource, [])
            change_log = ''
            if scs:
                change_log += "<h3>Change log</h3><div>"
                for s, cs in scs.items():
                    change_log += "<h4>%s</h4>" % s
                    change_log += tabulate.tabulate(cs, tablefmt='unsafehtml')
                change_log += "</div>"
        
            html = str(soup)
            
            if "Entities" in md:
            
                ty = resource
                dicts = []
                while ty is not None:
                    dicts.append(concepts.get(ty, {}))
                    ty = entity_supertype.get(ty)
                    
                usage = {}
                # in reverse so that the most-specialized are retained
                for d in reversed(dicts):
                    usage.update(d)                
                
                if usage:
                    paragraph += 1
                    html += "<h3>" + idx + ".%d Definitions applying to General Usage</h3>" % (paragraph-1)
            
                    for n, (concept, data) in enumerate(sorted(usage.items()), start=1):
                        html += "<h4>" + idx + ".%d.%d " % (paragraph - 1, n) + concept + "</h4>"
                        html += "<div>" + data['definition'].replace("../../", "")
                        
                        keys = set()
                        for d in dicts:
                            keys |= d.get(concept, {}).get('parameters', {}).keys()
                            
                        params = defaultdict(list)
                        for d in dicts:
                            for k in keys:
                                params[k] += d.get(concept, {}).get('parameters', {}).get(k, [])
                                
                        print(params)
                            
                        # transpose
                        vals = list(map(list, itertools.zip_longest(*params.values())))
                        html += tabulate.tabulate(vals, headers=params.keys(), tablefmt='html') + "</div>"
                        # html += "<pre>" + data['rules'] + "</pre>"
                        
            if entity_definitions.get(resource):
                html += "<h3>" + idx + ".%d Formal representations</h3>" % paragraph
                html += "<pre>" + entity_definitions.get(resource) + "</pre>"
                paragraph += 1
            
            
                
    return render_template('entity.html', navigation=navigation_entries, content=html, number=idx, entity=resource, path=md[3:], preface=change_log)

@app.route(make_url('listing'))
def listing():
    items = [{'number': name_to_number[n], 'url': url_for('resource', resource=n), 'title': n} for n in sorted(entity_names + type_names)]
    return render_template('list.html', navigation=navigation_entries, items=items)

@app.route(make_url('concepts/content.html'))
@app.route(make_url('concepts/<path:s>/content.html'))
def concept(s=''):
    md_root = "../docs/templates"
    
    s = s.replace("_", " ")
    
    n = "4"
    if s:
        ps = s.split("/")
        t = ps[-1]
        for pt in itertools.accumulate([[p] for p in ps]):
            n += '.%d' % (sorted(os.listdir(os.path.join(md_root, *pt[:-1]))).index(pt[-1]) + 1)
    else:
        t = chapter_lookup(number=4).get('title')
    
    fn = os.path.join(md_root, s, "README.md")
    
    if os.path.exists(fn):
        html = markdown.markdown(
            process_graphviz_concept(
                "".join(c for c in s if c.isalnum()),
                open(fn).read()
            ))
        soup = BeautifulSoup(html)
        # First h1 is handled by the template
        soup.find('h1').decompose()
        
        # Change svg img references to embedded svg
        # because otherwise URLS are not interactive
        for img in soup.findAll("img"):
            if img['src'].endswith('.svg'):
                entity, hash = img['src'].split('/')[-1].split('.')[0].split('_')
                svg = BeautifulSoup(open(os.path.join('svgs', entity + "_" + hash + '.dot.svg')))
                svg_node = svg.find('svg')
                svg_node.attrs['width'] = "%dpx" % (int(svg_node.attrs['width'][0:-2]) // 3 * 2)
                svg_node.attrs['height'] = "%dpx" % (int(svg_node.attrs['height'][0:-2]) // 3 * 2)
                img.replaceWith(svg_node)
            else:
                img['src'] = img['src'][9:]

        html = str(soup)
    else:
    	html = fn
    	
    def make_path(p):
        return p.split(os.sep)[3:-1]
        
    def make_link(c):
        c = list(c)
        return link(
            make_url("concepts/" + "/".join(c).replace(" ", "_") + "/content.html"),
            " ".join(c[(0 if len(c) == 1 else 1):]))
        
    subs = sorted(filter(lambda pt: "/".join(pt) != s, filter(None, map(make_path, glob.glob(os.path.join(md_root, s, "**", "README.md"), recursive=True)))))
    subs = list((make_link(next(b)),[make_link(c) for c in list(b)[1:]]) for a, b in itertools.groupby(subs, key=operator.itemgetter(0)))

    return render_template('chapter.html', navigation=navigation_entries, content=html, path=fn[3:], title=t, number=n, subs=subs)

from dataclasses import dataclass
@dataclass
class link:
    href : str
    text : str
    
    
@app.route(make_url('chapter-<n>/'))
def chapter(n):
    try: n = int(n)
    except: abort(404)
    
    chp = chapter_lookup(number=n)
    t = chp.get('title')
    md_root = "../docs/schemas"
    cat = t.split(" ")[0].lower()
    
    fn = os.path.join(md_root, cat, "README.md")
    
    if os.path.exists(fn):
        html = markdown.markdown(open(fn).read())
        soup = BeautifulSoup(html)
        # First h1 is handled by the template
        soup.find('h1').decompose()
        html = str(soup)
    else:
    	html = ''
    
    subs = [itms for t, itms in hierarchy if t == chp.get('title')][0]
    subs = list(map(operator.itemgetter(0), subs))
    
    return render_template('chapter.html', navigation=navigation_entries, content=html, path=fn[3:], title=t, number=n, subs=subs)
    

@app.route('/')
@app.route(make_url('content/<s>.htm'))
def content(s='cover'):
    fn = "../content"
    fn = os.path.join(fn, s + ".md")
    
    if not os.path.exists(fn):
        abort(404)
    
    try:
        i = content_names.index(s)
        number = i + 1
        title = navigation_entries[1][i]['title']
    except:
        
        try:
            i = content_names_2.index(s)
            number = ""
            title = s[0].upper() + s[1:]
        except:
            abort(404)
    
    html = markdown.markdown(open(fn).read())
    return render_template('chapter.html', navigation=navigation_entries, content=html, path=fn[3:], title=title, number=number, subs=[])

    
@app.route(make_url('annex-a.html'))
def annex_a():
    url = "https://github.com/buildingSMART/IFC4.3.x-output/blob/master/IFC.exp"
    html = "<h2>Computer interpretable listings</h2>" + \
        "<p>This annex contains a listing of the complete schema combining all definitions of clauses 5, 6, 7, and 8 without comments " + \
        "or other explanatory text. These listings are available in computer-interpretable form that may be parsed by computer.</p>" + \
        "<p>Official schema publications for this release are at the following URLs:</p>" + \
        (tabulate.tabulate([["IFC EXPRESS long form schema", '%s']], headers=["Format", "URL"], tablefmt='html') % \
            ("<a href='%(url)s'>%(url)s</a>" % locals()))
    return render_template('chapter.html', navigation=navigation_entries, content=html, path=None, title="Annex A", number="", subs=[])

    
@app.route(make_url('toc.html'))
def toc():
    subs = [(x['title'], []) for x in navigation_entries[1]] + hierarchy
    return render_template('chapter.html', navigation=navigation_entries, content='', path=None, title="Contents", number="", subs=subs, toc=True)


@app.route(make_url('annex-c.html'))
def annex_c():
    html = "<h2>Inheritance listings</h2>" + \
        "<p>This annex contains listings of entity definitions organized by inheritance.</p>"
    
    def transform(s):
        s = s.strip('\n')
        padding = s.count(' ')
        entity = "".join([c for c in s if c != ' '])
        return '<tr><td>' + '&nbsp;' * padding * 4 + "<a href='" + url_for('resource', resource=entity) + "'>" + entity + "</a> </td><td>" + name_to_number[entity] + "</td>"
    
    html += "<table style='width:fit-content'>" +  "".join(map(transform, open("inheritance_listing.txt"))) + "</table>"
        
    return render_template('chapter.html', navigation=navigation_entries, content=html, path=None, title="Annex C", number="", subs=[])
    
@app.route(make_url('annex-d.html'))
def annex_d():
    subs = map(os.path.basename, glob.glob("../output/IFC.xml/*.png"))
    subs = sorted(s[:-4] + ":" + url_for('annex_d_diagram_page', s=s[:-4]) for s in subs)
    return render_template('chapter.html', navigation=navigation_entries, content='<h2>Diagrams</h2>', path=None, title="Annex D", number="", subs=subs)
    
@app.route(make_url('annex_d/<s>.html'))
def annex_d_diagram_page(s):
    img = "<h2>" + s + " diagram</h2><img src='"+s+".png'/>"
    return render_template('chapter.html', navigation=navigation_entries, content=img, path=None, title="Annex D", number="", subs=[])

@app.route(make_url('annex_d/<s>.png'))
def annex_d_diagram(s):
    return send_from_directory("../output/IFC.xml", s + ".png")


@app.route(make_url('annex-e.html'))
def annex_e():
    subs = map(os.path.basename, filter(os.path.isdir, glob.glob("../../examples/IFC 4.3/*")))
    subs = sorted(s + ":" + url_for('annex_e_example_page', s=s) for s in subs)
    return render_template('chapter.html', navigation=navigation_entries, content='<h2>Examples</h2>', path=None, title="Annex E", number="", subs=subs)

    
@app.route(make_url('annex-f.html'))
def annex_f():
    with open("changes_by_schema.json") as f:
        li = json.load(f)
        pairs = [('<h3>%s</h3>' % s, '<div>%s</div>' % tabulate.tabulate(cs, tablefmt='unsafehtml')) for s, cs in li]
        flat = sum(pairs, ())
        content = "".join(('<h2>Change logs</h2>',) + flat)
    return render_template('chapter.html', navigation=navigation_entries, content=content, path=None, title="Annex F", number="")
    
    
@app.route(make_url('annex_e/<s>.html'))
def annex_e_example_page(s):
    subs = map(os.path.basename, filter(os.path.isdir, glob.glob("../../examples/IFC 4.3/*")))
    if s not in subs:
        abort(404)
    
    fn = glob.glob(os.path.join("../../examples/IFC 4.3", s, "*.md"))[0]
    html = '<p></p>' + markdown.markdown(open(fn).read(), extensions=['tables', 'fenced_code'])
    code = open(glob.glob(os.path.join("../../examples/IFC 4.3", s, "*.ifc"))[0]).read()
    html += "<h2>Source</h2>"
    html += "<pre>" + code + "</pre>"
    path_repo = 'buildingSMART/Sample-Test-Files'
    path = fn[15:]
    return render_template('chapter.html', navigation=navigation_entries, content=html, path=path, title="Annex E", number="", subs=[], repo=path_repo)

@app.route(make_url('<name>/content.html'))
def schema(name):
    md_root = "../docs/schemas"
    
    cat_full, schemas = [(t, itms) for t, itms in hierarchy if name in [i[0].lower() for i in itms]][0]
    cat = cat_full.split(" ")[0].lower()
    t, subs = [x for x in schemas if x[0].lower() == name][0]
    chp = chapter_lookup(cat=cat)
    
    n1 = chp.get('number')
    n2 = [s[0] for s in schemas].index(t) + 1
    n = "%d.%d" % (n1, n2)
    fn = os.path.join(md_root, cat, t, "README.md")
    
    if os.path.exists(fn):
        html = markdown.markdown(open(fn).read(), extensions=['sane_lists'])
        soup = BeautifulSoup(html)
        # First h1 is handled by the template
        soup.find('h1').decompose()
        html = "<h2>" + n + ".1 Schema Definition</h2>" + str(soup)
    else:
        html = ''

    order = ["Types", "Entities"]
    subs = sorted(subs.items(), key=lambda tup: order.index(tup[0]))

    return render_template('chapter.html', navigation=navigation_entries, content=html, path=fn[5:], title=t, number=n, subs=subs)

@app.route('/search', methods=['GET', 'POST'])
def search():
    matches = []
    query = ''
    if request.method == 'POST' and request.form['query']:
        solr = pysolr.Solr('http://localhost:8983/solr/ifc')
        query = request.form['query']
        results = solr.search('body:(%s)' % query, **{'hl':'on', 'hl.fl':'body'})
        h = results.highlighting
        def format(s):
            return re.sub(r'[^\w\s<>/]', '', s)
        matches = [{
            'url': url_for('resource', resource=r['title'][0]), 
            'match': format(h[r['id']]['body'][0]),
            'title': r['title'][0]
        } for r in list(results)[0:10]]
    return render_template('search.html', navigation=navigation_entries, matches=matches, query=query)


@app.route('/sandcastle', methods=['GET', 'POST'])
def sandcastle():
    
    md = ''
    html = ''
    
    if request.method == 'POST' and request.form['md']:
        
        md = request.form['md']

        html = markdown.markdown(
            process_graphviz('sandcastle', md),
            extensions=['tables', 'fenced_code'])
            
        soup = BeautifulSoup(html)
        
        # Change svg img references to embedded svg
        # because otherwise URLS are not interactive
        for img in soup.findAll("img"):
            if img['src'].endswith('.svg'):
                print(img['src'].split('/')[-1].split('.')[0])
                entity, hash = img['src'].split('/')[-1].split('.')[0].split('_')
                svg = BeautifulSoup(open(os.path.join('svgs', entity + "_" + hash + '.dot.svg')))
                img.replaceWith(svg.find('svg'))
                
        html = str(soup)
    
    return render_template('sandcastle.html', html=html, md=md)
        
    