import os
import re
import sys
import glob
import html
import json
import subprocess

import xml.etree.ElementTree as ET
from xml.dom import minidom
from collections import defaultdict

from xmi_document import xmi_document, SCHEMA_NAME

GUID_PATTERN = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$')
HTML_TAG_PATTERN = re.compile('<.*?>')
MULTIPLE_SPACE_PATTERN = re.compile(r'\s+')
def strip_html(s):
    S = html.unescape(s or '')
    i = S.find('\n')
    return re.sub(HTML_TAG_PATTERN, '', S)
    
    
def strip(s):
    return strip_html(s).replace("bSI Documentation", "").strip().replace("''", "'").encode('ascii', 'xmlcharrefreplace').decode('ascii')
    
    
def format(s):
    return re.sub(MULTIPLE_SPACE_PATTERN, ' ', ''.join([' ', c][c.isalnum() or c in '.,'] for c in s)).strip()
    
   
def get_parent_of_pt(xmi_doc, enum_type):
    enum_id = enum_type.idref
    type_refs = []
    for assoc in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Association"]:
        try:
            c1, c2 = assoc/'ownedEnd'
        except ValueError as e:
            # print("encountered exception `%s' on %s" % (e, assoc))
            continue
        assoc_type_refs = set(map(lambda c: (c|"type").idref, (c1, c2)))
        if enum_id in assoc_type_refs:
            other_idref = list(assoc_type_refs - {enum_id})[0]
            type_refs.append(xmi_doc.xmi.by_id[other_idref].name)
            
    # @todo filter this based on inheritance hierarchy
    type_refs_without_type = [s for s in type_refs if 'Type' not in s]
    if len(type_refs_without_type) != 1:
        print("WARNING:", len(type_refs_without_type), "type associations on", enum_type.name, file=sys.stderr)
    
    return type_refs_without_type[0] if type_refs_without_type else None


def build_property_defs(xmi_doc, pset, node, by_name):
    
    def elem_by_name(nm):
        els = [c for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Class"] if c.name == ty_arg] + \
            [c for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Enumeration"] if c.name == ty_arg]
        return els[0]
    
    orders = [xmi_doc.try_get_order(x) for x in pset.children]
   
    for _, a, (nm, (ty_ty_arg)) in sorted(zip(orders, pset.children, pset.definition)):
    
        is_pset = pset.type == "CPROP" or pset.stereotype == "PSET"
        
        pd = ET.SubElement(node, "PropertyDef" if is_pset else 'QtoDef')
        ET.SubElement(pd, 'Name').text = a.name
        ET.SubElement(pd, 'Definition').text = strip((a.node/"documentation")[0].value)
        pt = ET.SubElement(pd, 'PropertyType' if pset.stereotype == "PSET" else 'QtoType')
        
        if is_pset:
            ty, ty_args = ty_ty_arg
            
            if ty in ("PropertySingleValue", "PropertyBoundedValue", "PropertyListValue"):
            
                ty_arg = list(ty_args.values())[0]
                            
                tpsv = ET.SubElement(pt, 'Type' + ty)
                
                if ty == "PropertyListValue":
                    # unnecessary intermediate node
                    tpsv = ET.SubElement(tpsv, 'ListValue')
                
                ET.SubElement(tpsv, 'DataType').set('type', ty_arg)
                
            elif ty == "PropertyEnumeratedValue":
                
                ty_arg = list(ty_args.values())[0]
            
                tpev = ET.SubElement(pt, 'TypePropertyEnumeratedValue')
                el = ET.SubElement(tpev, 'EnumList')
                el.set('name', ty_arg)
                
                enum_type = elem_by_name(ty_arg)
                p_id_values = sorted((xmi_doc.try_get_order(x), x.name) for x in enum_type/"ownedLiteral")
                
                for pid, pv in p_id_values:
                    ET.SubElement(el, 'EnumItem').text = pv
                    
            elif ty == "PropertyComplexProperty":
                
                ty_arg = list(ty_args.values())[0]
                
                tcp = ET.SubElement(pt, 'TypeComplexProperty')
                tcp.set('name', ty_arg)
                
                build_property_defs(xmi_doc, by_name[ty_arg], tcp, by_name)

            elif ty == "PropertyReferenceValue":
                
                ty_arg = list(ty_args.values())[0]
                
                tprv = ET.SubElement(pt, 'TypePropertyReferenceValue')
                tprv.set("reftype", ty_arg)
                
            elif ty == "PropertyTableValue":
                
                # what's this?
                ET.SubElement(pt, 'Expression')
                
                ET.SubElement(ET.SubElement(pt, 'DefiningValue'), "DataType").set("type", ty_args["Defining"])
                ET.SubElement(ET.SubElement(pt, 'DefinedValue'), "DataType").set("type", ty_args["Defined"])
            
        else:
            pt.text = ty_ty_arg


def construct_xml(xmi_doc, pset, path, by_id, by_name):

    # The XMI data contains IFC base64 guids and rfc encoded hex guids
    
    """
    guid = pset.node.tags().get("IFCDOC_GUID")
    if guid is None:
        print("WARNING: no guid for", pset.name)
        guid = ifcopenshell.guid.expand(ifcopenshell.guid.new())
    elif re.match(GUID_PATTERN, guid.lower()):
        guid = guid.lower().replace("-", "")
    else:
        guid = ifcopenshell.guid.expand(guid)
    """

    psd = ET.Element('PropertySetDef' if pset.stereotype == "PSET" else 'QtoSetDef')
    psd.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    psd.set('xmlns:xsd', 'http://www.w3.org/2001/XMLSchema')
    # psd.set('ifdguid', guid)
    psd.set('templatetype', 'PSET_TYPEDRIVENOVERRIDE')
    
    if pset.stereotype == "PSET":
        psd.set('xsi:noNamespaceSchemaLocation', 'http://buildingSMART-tech.org/xml/psd/PSD_IFC4.xsd')
    else:
        psd.set('xsi:noNamespaceSchemaLocation', 'http://buildingSMART-tech.org/xml/psd/QTO_IFC4.xsd')
    # psd.set('xmlns', 'http://buildingSMART-tech.org/xml/psd/PSD_IFC4.xsd')
    
    ET.SubElement(psd, 'IfcVersion').set('version', SCHEMA_NAME)
    
    ET.SubElement(psd, 'Name').text = pset.name
    
    ET.SubElement(psd, 'Definition').text = strip((pset.node/"properties")[0].documentation)
    
    ET.SubElement(psd, 'Applicability')
    
    acs = ET.SubElement(psd, 'ApplicableClasses')
    atv = ET.SubElement(psd, 'ApplicableTypeValue')
    
    for x in (pset.meta.get("refs") or []):
        if x in by_id:
            x = by_id[x]
            if x.type == "ENTITY" or (x.parent and x.parent.type == "ENUM"):
                nm = x.name
                if x.parent and get_parent_of_pt(xmi_doc, x.parent.node):
                    nm = get_parent_of_pt(xmi_doc, x.parent.node) + "." + nm
                nm = nm.replace(".", "/")
                ET.SubElement(acs, 'ClassName').text = nm
                atv.text = nm
        else:
            print("WARNING:", x, "on", pset.name, "not recorded", file=sys.stderr)
        
    pdefs = ET.SubElement(psd, 'PropertyDefs' if pset.stereotype == "PSET" else 'QtoDefs')
    
    build_property_defs(xmi_doc, pset, pdefs, by_name)
    
    with open(os.path.join(path, pset.name + ".xml"), 'w') as f:
        f.write(
            minidom.parseString(ET.tostring(psd))\
                .toprettyxml(indent="  ")
        )
        
def run(xmi_doc, path):
    psets = []
    by_id = {}
    by_name = {}
    
    for item in xmi_doc:
        if item.type == "PSET":
            psets.append(item)
        else:
            by_id[item.id] = item
            by_name[item.name] = item
            for c in item.children:
                by_id[c.id] = c
        
    for item in psets:
        construct_xml(xmi_doc, item, path, by_id, by_name)
            
            
def compare(path1, path2, output):
    with open(output, "w") as f:
        fn1, fn2 = map(lambda fn: list(map(os.path.basename, glob.glob(os.path.join(fn, "*.xml")))), (path1, path2))
        
        print(file=f)
        print("Missing in output", file=f)
        print("=================", file=f)
        for p in set(fn1) - set(fn2):
            print("*", p, file=f)
        
        print(file=f)        
        print("Missing in reference", file=f)
        print("=================", file=f)
        for p in set(fn2) - set(fn1):
            print("*", p, file=f)
            
        for p in set(fn1) & set(fn2):
            print(file=f)
            print(p, file=sys.stderr)
            data = subprocess.check_output([
                sys.executable,
                os.path.join(os.path.dirname(__file__), "compare_pset.py"),
                os.path.join(path1, p),
                os.path.join(path2, p)])
            if data:
                print(p, file=f)
                print("="*len(p), file=f)
                print(data.decode('ascii'), file=f)
            
            
if __name__ == "__main__":
    
    if len(sys.argv) == 3:
        fn, path = sys.argv[1:]
        run(xmi_document(fn), path)
        
    elif len(sys.argv) == 5 and sys.argv[1] == "--compare":
        path, ref_path, md_out = sys.argv[2:]
        compare(ref_path, path, md_out)
        
    else:
        print("Usage: python to_pset.py <schema.xml> <output dir>", file=sys.stderr)
        print("Usage: python to_pset.py --compare <output dir> <ref dir> <markdown output>", file=sys.stderr)
        exit()
