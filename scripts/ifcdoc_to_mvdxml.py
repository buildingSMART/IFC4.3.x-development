import os
import re
import glob
import functools
import itertools

import lxml.etree as ET

import ifcopenshell
from ifcopenshell.mvd.mvdxml_expression import parse as parse_mvd_expr

IGNORED_ATTRS = ()
IGNORED_TAGS = ()
   
def flatmap(func, *iterable):
    return itertools.chain.from_iterable(map(func, *iterable))
    

def to_dict(t):
    if t.tag in IGNORED_TAGS:
        return

    # strip out namespace reported by etree as
    # "{http://www.buildingsmart-tech.org/xml/qto/QTO_IFC4.xsd}QtoSetDef"
    items = {'#tag': re.sub(r'\{.+?\}', '', t.tag)}
    
    if list(t):
        items['_children'] = list(flatmap(to_dict, t))
    
    items.update({'@' + k: v for k, v in (t.attrib or {}).items() if k not in IGNORED_ATTRS})
        
    if t.text and t.text.strip():
        items['#text'] = t.text.strip()
        
    yield items

    
def read(fn):
    parser = ET.XMLParser(encoding="utf-8")
    return next(to_dict(ET.parse(fn, parser=parser).getroot()))
    
    
def make_transform_tag_renamer(target, attribute_mapping={}):
    def inner(di, parent):
        return {
            '#tag': target,
            **{attribute_mapping.get(k, k): v for k, v in di.items() if k[0] == '@'}
        }
    return inner

def make_transform_identity():
    def inner(di, parent):
        return make_transform_tag_renamer(di["#tag"])(di, parent)
    return inner
    
def do_transform_skip(di, parent):
    return None
    
def child_by_tag(node, tag):
    return [c for c in node["_children"] if c['#tag'] == tag][0]
    
def transform_uuid(v):
    if len(v) == 36:
        return v
    return ifcopenshell.guid.split(ifcopenshell.guid.expand(v))[1:-1]
    
transform_DocModelView = make_transform_tag_renamer("ModelView")
transform_ConceptRoots = make_transform_tag_renamer("Roots")
transform_Concepts = make_transform_identity()
transform_DocModelRuleAttribute = make_transform_tag_renamer("AttributeRule", attribute_mapping={"Name": "AttributeName"})
transform_DocModelRuleEntity = make_transform_tag_renamer("EntityRule", attribute_mapping={"Name": "EntityName"})
transform_DocTemplateDefinition = make_transform_tag_renamer("ConceptTemplate")

templates = {}
used_template_ids = {}

def parse_templates(pt):
    for fn in glob.glob(os.path.join(pt, "**", "DocTemplateDefinition.xml"), recursive=True):
        tmpl_def = transform(read(fn))[0]
        if "@id" in tmpl_def:
            href = tmpl_def["@id"]
            templates[href] = tmpl_def

def transform_DocConceptRoot(di, parent):
    return {
        '#tag': "ConceptRoot",
        '@uuid': transform_uuid(di["@UniqueId"]),
        '@name': child_by_tag(di, "ApplicableEntity")["@href"],
        '@applicableRootEntity': child_by_tag(di, "ApplicableEntity")["@href"]
    }
    
def transform_DocTemplateUsage(di, parent):
    href = child_by_tag(di, "Definition")["@href"]
    if href not in used_template_ids:
        used_template_ids[href] = 1    
    return {
        '#tag': "Concept",
        '@uuid': transform_uuid(di["@UniqueId"]),
        '@name': templates[href]["@Name"],
        '@status': "sample",
        '@override': "false",
    }
    
def transform_DocTemplateItem(di, parent):
    r = {'#tag': "TemplateRule"}
    if "@RuleParameters" in di:
        try:
            parse_mvd_expr(di["@RuleParameters"])
        except:
            print("Failed to parse", di["@RuleParameters"])
            return None         
        r["@Parameters"] = di["@RuleParameters"]
    else: return None
    return r

def transform_Items(di, parent):
    href = child_by_tag(parent, "Definition")["@href"]
    ref = transform_uuid(templates[href]["@UniqueId"])
    return [{'#tag': "Template", "@ref": ref}, {'#tag': "TemplateRules", "@operator": "and"}]
    
def transform_Rules(di, parent):
    if parent["#tag"] == "DocTemplateDefinition":
        tag = "Rules"
    elif parent["#tag"] == "DocModelRuleAttribute":
        tag = "EntityRules"
    else:
        tag = "AttributeRules"        
    return {"#tag": tag}
    
def transform(di, parent=None):
    F = globals().get(f"transform_{di['#tag']}", do_transform_skip)
    di2 = F(di, parent)
    children = sum(map(functools.partial(transform, parent=di), di.get("_children", [])), [])
    if di2 is None:
        return children
    elif isinstance(di2, dict):
        di2["_children"] = children
        di2 = [di2]
    elif isinstance(di2, list):
        # di2.extend(children)
        di2[-1]["_children"] = children
    elif children:
        # nested templates aren't supported in mvdXML, or how?
        # raise ValueError("Should be leaf")
        pass
    return di2
    
    
def create_mvd(roots):
    return [{
        "#tag": "mvdXML",
        # "@xmlns:xsd": "http://www.w3.org/2001/XMLSchema",
        # "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "@uuid": transform_uuid(ifcopenshell.guid.new()),
        "@name": "",
        "@status": "sample",
        # "@xsi:schemaLocation": "http://www.buildingsmart-tech.org/mvd/XML/1.1 http://www.buildingsmart-tech.org/mvd/XML/1.1/mvdXML_V1.1_add1.xsd",
        # "@xmlns": "http://buildingsmart-tech.org/mvd/XML/1.1",
        "_children": [{
            "#tag": "Templates",
            "_children": [templates[t] for t in used_template_ids.keys()]
        },{
            "#tag": "Views",
            "_children": roots
        }]
    }]
    
    
def strip_child_rules(d):
    def inner(di):
        if di["#tag"] == "TemplateRule" and "_children" in di:
            del di["_children"]
        else:
            for c in di.get("_children", []):
                inner(c)
        return di
    return [inner(d[0])]
    
    
def serialize(di, ofn):
    def inner(d, parent=None):
        if parent is None:
            node = ET.Element(d["#tag"])
        else:
            node = ET.SubElement(parent, d["#tag"])

        for k, v in d.items():
            if k == "#tag":
                pass
            elif k == "#text":
                node.text = v
            elif k.startswith('@'):
                node.set(k[1:], v)
            elif k == "_children":
                for child in v:
                    inner(child, node)
            else:
                raise ValueError("Unexpected")
                
        return node

    ET.ElementTree(inner(di[0])).write(ofn, pretty_print=True)
    
if __name__ == "__main__":
    import sys
    parse_templates(os.path.join(sys.argv[1], "..", "..", "..", "Templates"))
    serialize(create_mvd(strip_child_rules(transform(read(sys.argv[1])))), sys.argv[2])
