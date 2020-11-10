IfcSpatialElement
=================
A spatial element is the generalization of all spatial elements that might be
used to define a spatial structure or to define spatial zones.  

  

  * a hierarchical spatial structure element as [_IfcSpatialStructureElement_]($element://{30E08EC3-5B14-45f4-8246-B4811D2ECF1B})
  

  * a spatial structure is a hierarchical decomposition of the project. That spatial structure is often used to provide a project structure to organize a building project.
  

  * A spatial project structure might define as many levels of decomposition as necessary for the building project. Elements within the spatial project structure are site, facility (including subtypes), facility part, building storey, and space
  

  * a spatial zone as [_IfcSpatialZone_]($element://{C6BFC05D-09D4-4bed-92A9-1823739DE0C8})
  

  * a spatial zone is a non-hierarchical and potentially overlapping decomposition of the project under some functional consideration.
  

  * a spatial zone might be used to represent a thermal zone, a lighting zone, a usable area zone.
  

  * a spatial zone might have its independent placement and shape representation.
  

  
HISTORY New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcspatialelement.htm)


Attribute definitions
---------------------
| Attribute          | Description                                                                                                                                                                                                                                                                                                                     |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ContainsElements   |                                                                                                                                                                                                                                                                                                                                 |
| ReferencesElements |                                                                                                                                                                                                                                                                                                                                 |
| ServicedBySystems  |                                                                                                                                                                                                                                                                                                                                 |
| LongName           | Long name for a spatial structure element, used for informal purposes. It should be used, if available, in conjunction with the inherited _Name_ attribute.\X\0D> NOTE  In many scenarios the _Name_ attribute refers to the short name or number of a spacial element, and the _LongName_ refers to the full descriptive name. |

