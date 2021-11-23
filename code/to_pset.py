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

import ifcopenshell.guid

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
    
    
def generalization(xmi_doc, pe):
    try:
        P = xmi_doc.xmi.by_id[(pe|"generalization").general]
    except:
        P = None
    if P: return generalization(P)
    else: return pe
    
    
def get_prop_type(xmi_doc, a):
    type_name = "PEnum_" + a.name
    # @todo why is this lookup by name?
    enum_types_by_name = [c for c in xmi_doc.xmi.by_tag_and_type["packagedElement"]["uml:Class"] if c.name == type_name]
    if len(enum_types_by_name) == 1:
        return type_name, [x.name for x in enum_types_by_name[0]/"ownedLiteral"]
    else:
        type_values = None
        try:
            pe_type = xmi_doc.xmi.by_id[(xmi_doc.xmi.by_id[a.node.idref]|"type").idref]
            return pe_type.name, None
            
            root_generalization = generalization(pe_type)
            type_name = root_generalization.name.lower()
            
        except ValueError as e:
            print("WARNING:", a.name, "has no associated type", file=sys.stderr)
            type_name = 'any'
    return None, None
    
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


def construct_xml(xmi_doc, pset, path, by_id):
    
    # The XMI data contains IFC base64 guids and rfc encoded hex guids
       
    guid = pset.node.tags().get("IFCDOC_GUID")
    if guid is None:
        print("WARNING: no guid for", pset.name)
        guid = ifcopenshell.guid.expand(ifcopenshell.guid.new())
    elif re.match(GUID_PATTERN, guid.lower()):
        guid = guid.lower().replace("-", "")
    else:
        guid = ifcopenshell.guid.expand(guid)

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
        
    for a in pset.children:
        
        pd = ET.SubElement(pdefs, "PropertyDef" if pset.stereotype == "PSET" else 'QtoDef')
        ET.SubElement(pd, 'Name').text = a.name
        ET.SubElement(pd, 'Definition').text = strip((a.node/"documentation")[0].value)
        
        ptype_name, pvalues = get_prop_type(xmi_doc, a)
        if ptype_name:
            pt = ET.SubElement(pd, 'PropertyType' if pset.stereotype == "PSET" else 'QtoType')
            
            if pset.stereotype == "PSET":
                if pvalues is None:
                    tpsv = ET.SubElement(pt, 'TypePropertySingleValue')
                    ET.SubElement(tpsv, 'DataType').set('type', ptype_name)
                else:
                    tpev = ET.SubElement(pt, 'TypePropertyEnumeratedValue')
                    el = ET.SubElement(tpev, 'EnumList')
                    el.set('name', ptype_name)
                    
                    for pv in pvalues:
                        ET.SubElement(el, 'EnumItem').text = pv
                        
                    # apparently, similarly to the USERDEFINED and NOTDEFINED predefined
                    # type labels, these three also not (always?) modelled in UML.
                    additional = "OTHER", "NOTKNOWN", "UNSET"
                    
                    for x in additional:
                        if x not in pvalues:
                            ET.SubElement(el, 'EnumItem').text = x
            else:
                pt.text = ptype_name
                       
    with open(os.path.join(path, pset.name + ".xml"), 'w') as f:
        f.write(
            minidom.parseString(ET.tostring(psd))\
                .toprettyxml(indent="  ")
        )
        
def run(xmi_doc, path):
    psets = []
    by_id = {}
    for item in xmi_doc:
        if item.type == "PSET":
            psets.append(item)
        else:
            by_id[item.id] = item
            for c in item.children:
                by_id[c.id] = c

    for item in psets:
        construct_xml(xmi_doc, item, path, by_id)
            
            
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
