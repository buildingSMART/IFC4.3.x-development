IfcRelCoversBldgElements
========================
The _IfcRelCoversBldgElements_ relationship is an objectified relationship
between an element and one to many coverings, which cover that element.  
  
> NOTE  The definition of _IfcCoverings_ include both the coverings of
> building elements, such as flooring or cladding. and the covering of
> distribution elements, such as wrapping or sleeving.  
  
The IFC specification provides two relationships:  
  
* _IfcRelCoversBldgElements_ to assign coverings to elements.   
>> NOTE  This relationship is now deprecated and replaced by
_IfcRelAggregates_.  
* _IfcRelCoversSpaces_ to assign coverings to spaces   
>> NOTE  This relationship is now deprecated and replaced by
_IfcRelContainedInSpatialStructure_.  
  
Whether the relationship between the covering and the space, or between the
covering and the element, is regarded as primary, has to be determined within
the context of a model view definition.  
  
> HISTORY  New entity in IFC1.5  
  
{ .deprecated}  
> DEPRECATION  The relationship _IfcRelCoversBldgElements_ shall not be used
> anymore, use _IfcRelAggregates_ instead.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifcrelcoversbldgelements.htm)


Attribute definitions
---------------------
| Attribute               | Description   |
|-------------------------|---------------|
| RelatingBuildingElement |               |
| RelatedCoverings        |               |

