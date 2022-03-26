import re
import sys
import itertools

import xml_dict

from dataclasses import dataclass

from append_xmi import namespace
from ifcopenshell.express import express_parser
from xmi_document import SCHEMA_NAME

def flatmap(func, *iterable):
    return itertools.chain.from_iterable(map(func, *iterable))

namespaces = {
    'xs': "http://www.w3.org/2001/XMLSchema",
    'xlink': "http://www.w3.org/1999/xlink",
    'ifc': f"https://standards.buildingsmart.org/IFC/RELEASE/{'/'.join(re.split('_|X', SCHEMA_NAME))}"
}

XS = namespace(namespaces['xs'])
XLINK = namespace(namespaces['xlink'])
IFC = namespace(namespaces['ifc'])

class xml_serializable:
    def to_xml(self):
        return xml_dict.xml_node(getattr(XS, self.__dict__.get('tagname', type(self).__name__)), {k:v for k, v in self.__dict__.items() if v and k != 'tagname'})
    

@dataclass
class attribute(xml_serializable):
    name : str
    type : str = None
    use : str = "optional"


@dataclass
class attribute_ref(xml_serializable):
    ref : str
    fixed : str = None
    use : str = "optional"
    
    tagname : str = "attribute"


@dataclass
class element(xml_serializable):
    name : str
    type : str = None
    abstract : str = None
    minOccurs : str = "0"
    substitutionGroup : str = None
    nillable : str = None
    

@dataclass
class element_ref(xml_serializable):
    ref : str
    minOccurs : str = None
    maxOccurs : str = None
    
    tagname : str = "element"
    

def complex_type(elements, attributes, content=None, **kwargs):
    if content:
        children = [content]
    else:
        children = [
            xml_dict.xml_node(
                XS.sequence,
                children=elements
            )
        ]
    return xml_dict.xml_node(
        XS.complexType,
        kwargs,
        children=children + list(map(attribute.to_xml, attributes))
    )

def do_try(fn):
    try:
        return fn()
    except:
        pass

def create_attribute(a):
    a_type = a.type
    
    is_optional = a.optional
    
    if isinstance(a_type, express_parser.NamedType):
        ty = a_type.type
        
        is_binary = do_try(lambda: isinstance(schema.types[ty].type.type, express_parser.BinaryType))
        
        if ty in schema.entities or is_binary:
            assert isinstance(ty, str)
            return element(a.name, f"ifc:{ty}", nillable=None if is_binary else "true", minOccurs="0" if is_optional else None).to_xml()
        elif ty in schema.selects:
            assert isinstance(ty, str)
            elm = element(a.name, None, nillable="true" if is_optional else None, minOccurs="0" if is_optional else None).to_xml()
            elm.children = [xml_dict.xml_node(
                XS.complexType,
                children=[xml_dict.xml_node(
                    XS.group,
                    {"ref": f"ifc:{ty}"}
                )]
            )]
            return elm
        return attribute(a.name, f"ifc:{ty}", "optional").to_xml()
    elif isinstance(a_type, express_parser.SimpleType):
        ty = a_type.type
        simple_type_mapping = {
            'integer': 'xs:long',
            'logical': 'ifc:logical'
        }
        return attribute(a.name, simple_type_mapping[ty], "optional").to_xml()
    elif isinstance(a_type, express_parser.AggregationType):

        min_occurs_mult = 1
        max_occurs_mult = 1
        aggregate_type_prefix = ""
        if isinstance(a_type.type, express_parser.AggregationType):
            # nested lists don't require a lot of special handling, just list list
            min_occurs_mult = int(a_type.bounds.lower)
            max_occurs_mult = float("inf") if a_type.bounds.upper == "?" else int(a_type.bounds.upper)
            aggregate_type_prefix = a_type.aggregate_type + " "
            a_type = a_type.type

                                                   # v this should probably be enabled, but discussion pending in issue #462
        if a_type.type.type in schema.simpletypes: # and not isinstance(mapping.flatten_type(a_type.type).type, express_parser.StringType):
        
            max_length_constraint = []
            if a_type.bounds.upper != "?" and max_occurs_mult != float("inf"):
                max_length_constraint = [xml_dict.xml_node(
                    XS.maxLength,
                    {"value": a_type.bounds.upper}
                )]
                
            attr = attribute(a.name, None, "optional").to_xml()
            attr.children = [xml_dict.xml_node(
                XS.simpleType,
                
                
                children=[xml_dict.xml_node(
                    XS.restriction,
                    children=[xml_dict.xml_node(
                        XS.simpleType,
                        children=[xml_dict.xml_node(
                            XS.list,
                            {"itemType": f"ifc:{a_type.type.type}"}
                        )]
                    )] + max_length_constraint  
                )]
            )]
        else:
            if a_type.type.type in schema.simpletypes:
                wrapper_postfix = "-wrapper"
            else:
                wrapper_postfix = ""
            ty = a_type.type.type
            assert isinstance(ty, str)
            attr = element(a.name, None, nillable="true" if is_optional else None, minOccurs="0" if is_optional else None).to_xml()
            
            min_occurs = str(min_occurs_mult * int(a_type.bounds.lower))
            if min_occurs == "1":
                min_occurs = None
            
            attr.children = [complex_type([
                element_ref(f"ifc:{a_type.type.type}{wrapper_postfix}", minOccurs=min_occurs, maxOccurs="unbounded").to_xml()
            ],
            [
                attribute_ref("ifc:itemType", fixed=f"ifc:{a_type.type.type}{wrapper_postfix}", use=None),
                attribute_ref("ifc:cType", fixed=aggregate_type_prefix + a_type.aggregate_type, use=None),
                attribute_ref("ifc:arraySize", use="optional")
            ])]
            
        return attr
    else:
        breakpoint()
        

def convert(e):
    supertype = e.supertypes[0] if e.supertypes else "Entity"
    abstract_if_abstract = {"abstract": "true"} if e.abstract else {}
    yield element(e.name, f"ifc:{e.name}", substitutionGroup=f"ifc:{supertype}", nillable="true", minOccurs=None, **abstract_if_abstract).to_xml()
    attrs = [create_attribute(a) for a in e.attributes]
    elems = [e for e in attrs if e.tag == XS.element]
    attrs = [e for e in attrs if e.tag == XS.attribute]
    if elems:
        elems = [xml_dict.xml_node(
            XS.sequence,
            children=elems
        )]
    children = elems + attrs
    yield complex_type([], [], content=xml_dict.xml_node(
        XS.complexContent,
        children=[xml_dict.xml_node(
            XS.extension,
            {"base": f"ifc:{supertype}"},
            children=children
        )]
    ), name=e.name, **abstract_if_abstract)

mapping = express_parser.parse(sys.argv[1])
schema = mapping.schema
entities = list(schema.entities.values())
# entities = [schema.entities["IfcPerson"]]

header = complex_type(
    [
        xml_dict.xml_node(
            XS.element,
            {"name": "header", "minOccurs": "0"},
            children=[complex_type(
                [
                    element("name", "xs:string", minOccurs="0").to_xml(),
                    element("time_stamp", "xs:dateTime", minOccurs="0").to_xml(),
                    element("author", "xs:string", minOccurs="0").to_xml(),
                    element("organization", "xs:string", minOccurs="0").to_xml(),
                    element("preprocessor_version", "xs:string", minOccurs="0").to_xml(),
                    element("originating_system", "xs:string", minOccurs="0").to_xml(),
                    element("authorization", "xs:string", minOccurs="0").to_xml(),
                    element("documentation", "xs:string", minOccurs="0").to_xml(),               
                ],
                []
            )],
        )
    ],
    [
        attribute("id", "xs:ID"),
        attribute("express", "ifc:Seq-anyURI"),
        attribute("configuration", "ifc:Seq-anyURI")
    ],
    name="uos", abstract="true"
)

content = xml_dict.xml_node(
    XS.schema,
    {
        "targetNamespace": namespaces['ifc'],
        "elementFormDefault": "qualified",
        "attributeFormDefault": "unqualified"
    },
    namespaces=namespaces,
    children=[
        xml_dict.xml_node(XS.element,
            {
                "name": "uos",
                "type": "ifc:uos",
                "abstract": "true"
            },
        ),
        xml_dict.xml_node(XS.simpleType,
            {
                "name": "Seq-anyURI",
            },
            children=[
                xml_dict.xml_node(XS.list,
                    {
                        "itemType": "xs:anyURI",
                    }
                )
            ]
        ),
        header,
        element("ifcXML", "ifc:ifcXML", minOccurs=None, substitutionGroup="ifc:uos").to_xml(),
        complex_type([], [], content=xml_dict.xml_node(
            XS.complexContent,
            children=[xml_dict.xml_node(
                XS.extension,
                {"base": "ifc:uos"},
                children = [xml_dict.xml_node(
                    XS.choice,
                    {"minOccurs": "0", "maxOccurs": "unbounded"},
                    children=[(
                        xml_dict.xml_node(XS.element, {"ref": "ifc:Entity"})
                    )]
                )]
            
            )]
        ),name="ifcXML")
    ] + list(flatmap(convert, entities))
)

xml_dict.serialize([content], "ifc4x3.xsd")
