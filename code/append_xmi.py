import uuid
import itertools
import functools

from dataclasses import dataclass, field
from itertools import zip_longest as zip_l
from collections import defaultdict

import xml_dict

class namespace:
    def __init__(self, uri):
        self.uri = uri
        
    def __getattr__(self, k):
        return f"{{{self.uri}}}{k}"
        
XMI = namespace("http://schema.omg.org/spec/XMI/2.1")

def new_id():
    return str(uuid.uuid4()).upper()
    
def flatmap(func, *iterable):
    return itertools.chain.from_iterable(map(func, *iterable))

@dataclass
class uml_package:
    name : str
    id : str = field(default_factory=new_id)
    
    @functools.cached_property
    def xml(self):
        return xml_dict.xml_node(
            tag = 'packagedElement',
            attributes = {
                XMI.type: 'uml:Package',
                XMI.id: self.id,
                'name': self.name,
                'visibility': 'public'
            }
        )
        
@dataclass
class uml_class:
    name : str
    id : str = field(default_factory=new_id)
    
    @functools.cached_property
    def xml(self):
        return xml_dict.xml_node(
            tag = 'packagedElement',
            attributes = {
                XMI.type: 'uml:Class',
                XMI.id: self.id,
                'name': self.name,
                'visibility': 'public'
            }
        )
        
@dataclass
class uml_enumeration:
    name : str
    values : list
    id : str = field(default_factory=new_id)
    
    @functools.cached_property
    def xml(self):
        return xml_dict.xml_node(
            tag = 'packagedElement',
            attributes = {
                XMI.type: 'uml:Enumeration',
                XMI.id: self.id,
                'name': self.name,
            },
            children = [
                xml_dict.xml_node(
                    tag = 'ownedLiteral',
                    attributes = {
                        XMI.type: 'uml:EnumerationLiteral',
                        XMI.id: new_id(),
                        'name': v,
                    }
                ) for v in self.values
            ]
        )
    
# @todo mutable: inserts into owner.children
def create_connector(assoc_id):
    def inner(type_id_connector_id, owner):
        # @todo flatstarmap?
        type_id, connector_id = type_id_connector_id
        li = [
            xml_dict.xml_node(
                tag = 'memberEnd',
                attributes = {
                    XMI.idref: connector_id,
                }
            )
        ]
        if owner is None:
            li.append(xml_dict.xml_node(
                tag = 'ownedEnd',
                attributes = {
                    XMI.type: 'uml:Property',
                    XMI.id: connector_id,
                    "association": assoc_id
                },
                children = [
                    xml_dict.xml_node(
                        tag = 'type',
                        attributes = {
                            XMI.idref: type_id,
                        }
                    )
                ]
            ))
        else:
            owner.children.append(xml_dict.xml_node(
                tag = 'ownedAttribute',
                attributes = {
                    XMI.type: 'uml:Property',
                    XMI.id: connector_id,
                    "association": assoc_id
                },
                children = [
                    xml_dict.xml_node(
                        tag = 'type',
                        attributes = {
                            XMI.idref: type_id,
                        }
                    )
                ]
            ))
            
        return li
    return inner
    
    
@dataclass
class uml_assoc_class:
    name : str
    connector_types : list
    id : str = field(default_factory=new_id)
    connector_ids : list = None
    type : str = "uml:AssociationClass"
    owners : list = None
    
    @functools.cached_property
    def xml(self):
    
        c_ids = [cid or new_id() for _, cid in zip_l(self.connector_types, self.connector_ids or [])]
        owners = self.owners or ([None] * len(c_ids))
        
        return xml_dict.xml_node(
            tag = 'packagedElement',
            attributes = {
                XMI.type: self.type,
                XMI.id: self.id,
                'name': self.name,
                'visibility': 'public'
            },
            children = list(flatmap(create_connector(self.id), zip(self.connector_types, c_ids), owners))
        )
        
        
@dataclass
class uml_association:
    connector_types : list
    id : str = field(default_factory=new_id)
    connector_ids : list = None
    type : str = "uml:Association"
    owners : list = None
    
    @functools.cached_property
    def xml(self):
    
        c_ids = [cid or new_id() for _, cid in zip_l(self.connector_types, self.connector_ids or [])]
        owners = self.owners or ([None] * len(c_ids))
        
        return xml_dict.xml_node(
            tag = 'packagedElement',
            attributes = {
                XMI.type: self.type,
                XMI.id: self.id,
                'visibility': 'public'
            },
            children = list(flatmap(create_connector(self.id), zip(self.connector_types, c_ids), owners))
        )
        
        
@dataclass
class uml_realization:
    supplier : str
    client : str
    id : str = field(default_factory=new_id)
    
    @functools.cached_property
    def xml(self):        
        return xml_dict.xml_node(
            tag = 'packagedElement',
            attributes = {
                XMI.type: 'uml:Realization',
                XMI.id: self.id,
                "supplier": self.supplier,
                "client": self.client
            }
        )
        
        
class context:
    
    def __init__(self, fn):
        self.content = xml_dict.read(fn)
        
        self.to_node = {}
        
        def v(nd, stack):
            if nd.tag == "packagedElement" and "name" in nd.attributes:
                self.to_node[(
                    nd.attributes[XMI.type],
                    nd.attributes["name"]
                )] = nd
                self.to_node[
                    nd.attributes["name"]
                ] = nd
                self.to_node[
                    nd.attributes[XMI.id]
                ] = nd
                
        self._recurse(v)
        
        self.superclass = {}
        self.subclasses = defaultdict(list)
        
        def v(nd, stack):
            if nd.tag == "packagedElement" and nd.attributes.get(XMI.type) == "uml:Class":
                gens = [ch for ch in nd.children if ch.tag == "generalization"]
                if gens:
                    gen_name = self.to_node[gens[0].attributes['general']].attributes["name"]
                    self_name = nd.attributes["name"]
                    self.superclass[self_name] = gen_name
                    self.subclasses[gen_name].append(self_name)
                
        self._recurse(v)
        
        self.substitutions = defaultdict(list)

        def v(nd, stack):
            if nd.tag == "packagedElement" and nd.attributes[XMI.type] == "uml:Substitution":
                self.substitutions[nd.attributes["supplier"]].append(nd.attributes["client"])
                
        self._recurse(v)
        
    def write(self, fn):
        xml_dict.serialize([self.content], fn)
        
    def package_by_name(self, package_name):
        def v(nd, stack):
            if nd.tag == "packagedElement" and nd.attributes[XMI.type] == "uml:Package":
                if nd.attributes["name"] == package_name:
                    return nd
        return self._recurse(v)
        
    def insert(self, location, element):
        nd = element.xml
        location.children.append(nd)
        nd.parent = location
        return nd
        
    def _recurse(self, fn, nd=None, stack=None):
        if nd is None: nd = self.content
        if stack is None: stack = []
        
        r = fn(nd, stack)
        if r is not None:
            return r

        for ch in nd.children:
            r = self._recurse(fn, ch, stack + [nd])
            if r is not None:
                return r
            
    def print_packages(self):
        def v(nd, stack):
            if nd.tag == "packagedElement" and nd.attributes[XMI.type] == "uml:Package":
                print(" "*len(stack), nd.attributes["name"])
        self._recurse(v)
        
    def to_id(self, *args):
        return self.to_node[args].attributes[XMI.id]
        
if __name__ == "__main__":
    
    c = context("..\schemas\IFC.xml")
    ifc_package = c.package_by_name("IFC4x3_RC4")
    views_package = c.insert(ifc_package, uml_package("Views"))
    gu_package = c.insert(views_package, uml_package("GeneralUsage"))
    axis_geom_package = c.insert(gu_package, uml_package("GeneralUsage"))
    axis_geom = uml_class("AxisGeometry")
    c.insert(axis_geom_package, axis_geom)
    c.insert(axis_geom_package, uml_assoc_class("IfcWallAxisGeometryUsage", [axis_geom.id, c.to_id("uml:Class", "IfcWall")]))
    c.write("test.xml")
    # breakpoint()
    