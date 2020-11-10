IfcTypeResource
===============
_IfcTypeResource_ defines a specific (or type) definition of a resource.\S\ It
is used to define a resource specification (the specific resource, that is
common to all occurrences that are defined for that resource) and could act as
a resource template.  
  
An _IfcTypeResource_ may have a list of property sets attached. Values of
these properties are common to all occurrences of that resource type. The type
occurrence relationship is realized using the objectified relationship
_IfcRelDefinesByType_.  
  
Subtypes of _IfcTypeResource_ may be exchanged without being already assigned
to subtypes of _IfcResource_.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifctyperesource.htm)


Attribute definitions
---------------------
| Attribute       | Description                                                                                                                                                                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ResourceOf      |                                                                                                                                                                                                                                                                          |
| Identification  | An identifying designation given to a resource type.                                                                                                                                                                                                                     |
| LongDescription | An long description, or text, describing the resource in detail.\X\0D> NOTE  The inherited _SELF\\\IfcRoot.Description_ attribute is used as the short description.                                                                                                      |
| ResourceType    | The type denotes a particular type that indicates the resource further. The use has to be established at the level of instantiable subtypes. In particular it holds the user defined type, if the enumeration of the attribute ''PredefinedType'' is set to USERDEFINED. |

