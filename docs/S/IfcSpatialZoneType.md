IfcSpatialZoneType
==================
The [_IfcSpatialZoneType_]($element://{982267FC-426A-48b9-936C-EE619E7C26AB})
defines a list of commonly shared property set definitions of a space and an
optional set of product representations. It is used to define a space
specification (i.e. the specific space information, that is common to all
occurrences of that space type).  
NOTE The product representations are defined as representation maps (at the
level of the supertype
[_IfcTypeProduct_]($element://{BA61CFBF-8CD7-44c2-AD99-072068F55C99}), which
gets assigned by an element occurrence instance through the
_IfcShapeRepresentation.Item[1]_ being an
[_IfcMappedItem_]($element://{F1BD66A5-8531-41ca-BD3B-E02D0F1BE3C1}).  
A spatial zone type is used to define the common properties of a certain type
of space that may be applied to many instances of that type to assign a
specific style. Space types may be exchanged without being already assigned to
occurrences.  
NOTE The spatial zone types are often used to represent space catalogues, less
so for sharing a common representation map. Spatial zone types in a space
catalogue share same space classification and a common set of space
requirement properties.  
The occurrences of
[_IfcSpatialZoneType_]($element://{982267FC-426A-48b9-936C-EE619E7C26AB}) are
represented by instances of
[_IfcSpatialZone_]($element://{C6BFC05D-09D4-4bed-92A9-1823739DE0C8}).  
HISTORY New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcspatialzonetype.htm)


Attribute definitions
---------------------
| Attribute      | Description                                                                                                                                                                                                                                                                                                          |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PredefinedType |                                                                                                                                                                                                                                                                                                                      |
| LongName       | Long name for a spatial zone type, used for informal purposes. It should be used, if available, in conjunction with the inherited _Name_ attribute.\X\0D> NOTE  In many scenarios the _Name_ attribute refers to the short name or number of a spatial zone, and the _LongName_ refers to the full descriptive name. |

