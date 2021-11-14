import re
import io
import bisect

from xml.dom import minidom
from collections import defaultdict

class base(object):
    def __truediv__(self, other):
        return list(map(node, self.xml.getElementsByTagName(other)))
        
    def __or__(self, other):
        li = self/other
        if len(li) != 1:
            raise ValueError("%s has %d childNodes of type %s" % (self, len(li), other))
        return li[0]

class node(base):
    
    def __init__(self, xmlnode):
        self.xml = xmlnode        
        
    def tags(self):    
        return dict(map(lambda t: (t.name, t.value), self/"tag"))

    def attributes(self):
        return dict((k, getattr(self, k)) for k in self.xml.attributes.keys())
        
    def __getattr__(self, k):
        di = (self.xml.attributes or {})
        attr = di.get(k, di.get('xmi:'+k))
        if attr: return attr.value
        else:
            if '_' in k:
                return self.__getattr__(k.replace("_", ":"))
            else:
                return None

    def __repr__(self):
        out = io.StringIO()
        self.xml.writexml(out)
        return re.sub(r"^\s+", "", out.getvalue(), flags=re.MULTILINE).split("\n")[0]


def get_encoding(fn):
    from xml.parsers import expat
    p = expat.ParserCreate()
    d = []
    p.XmlDeclHandler = lambda *args: d.extend(args)
    p.Parse(next(iter(open(fn, encoding='ascii'))) + "<dummy/>")
    return d[1]


class doc(base):
    """
    A helper class for easily navigating the DOM.
    
    Examples:
    
    doc/"connector" list of elements with connector tagName
    doc|"start" same as above but single element (this is asserted)
    doc.by_tag_and_type["element"]["uml:DataType"]
    doc.by_id[...] single element by xml:id
    
    """
    
    def __init__(self, fn):
        self.xml = minidom.parse(fn)
        self.text = open(fn, encoding=get_encoding(fn)).read()
        self.linebreaks = [m.span()[0] for m in re.finditer(r'\n', self.text)]
        self.by_type = defaultdict(list)
        self.by_tag_and_type = defaultdict(lambda: defaultdict(list))
        self.by_tag = defaultdict(list)
        self.by_id = dict()
        self.by_idref = defaultdict(list)
        
        def visit(n, *fns):
            if n.nodeType == n.ELEMENT_NODE:
                for fn in fns:
                    fn(n)
            for c in n.childNodes:
                if c.nodeType == c.ELEMENT_NODE:
                    visit(c, *fns)
                
        def register_by_xmi_type(n):
            n = node(n)
            t = n.type
            if t: self.by_type[t].append(n)
            
        def register_by_tag_and_xmi_type(n):
            n = node(n)
            self.by_tag[n.xml.tagName].append(n)
            t = n.type
            if t: self.by_tag_and_type[n.xml.tagName][t].append(n)
            
        def register_by_xmi_idref(n):
            n = node(n)
            t = n.xmi_idref
            if t:
                # note that duplicate xmi:ids do exist e.g. for generalizations
                self.by_idref[t].append(n)

        def register_by_xmi_id(n):
            n = node(n)
            t = n.xmi_id
            if t and t not in self.by_id:
                # note that duplicate xmi:ids do exist e.g. for generalizations
                self.by_id[t] = n

        visit(self.xml, 
            register_by_xmi_type,
            register_by_xmi_id,
            register_by_xmi_idref,
            register_by_tag_and_xmi_type)
            
        self.tags = {}
            
        for pr in self.by_tag["uml:Profile"]:
            for pe in pr / "packagedElement":
                if pe.xmi_type != "uml:Stereotype":
                    continue

                D = {}
                tag = f"{pr.id}:{pe.id}".replace(" ", "_")
                attrs = [a.name for a in pe / "ownedAttribute"]
                base, attrs = attrs[0], attrs[1:]
                for tag_def in self.by_tag[tag]:
                    # it appears EA does not correctly export
                    # profiles with different base types but the
                    # same id / name, so we lookup attribute name
                    # based on XML node
                    base = [k for k in tag_def.attributes() if k.startswith("base_")][0]
                    
                    base_val = getattr(tag_def, base)
                    if len(attrs) == 0:
                        D[base_val] = True
                    elif len(attrs) == 1:
                        D[base_val] = getattr(tag_def, attrs[0])
                    else:
                        D[base_val] = tuple(getattr(tag_def, a) for a in attrs)
                
                # we update because there can be multiple stereotypes for
                # different kinds of elements, such as ordering info
                # for assoc, entity and enum literals
                self.tags[pe.name] = self.tags.get(pe.name, {})
                self.tags[pe.name].update(D)

    
    def locate(self, node):
        # pat = r'(?<=<)(%s[^\\/]*?xmi:idref="%s"[^\\/]*?)((?= \\/>)|(?=>))' % (node.xml.tagName, node.idref)
        # offset = next(re.finditer(pat, self.text)).span()[0]
        offset = self.text.find('id="' + (node.idref or node.id))
        line_no = bisect.bisect_left(self.linebreaks, offset)
        char = self.linebreaks[line_no] - offset
        line_no += 1
        return (line_no, char)