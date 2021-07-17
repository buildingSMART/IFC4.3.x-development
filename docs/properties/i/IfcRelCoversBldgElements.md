IfcRelCoversBldgElements
========================

The _IfcRelCoversBldgElements_ relationship is an objectified relationship between an element and one to many coverings, which cover that element.

> NOTE&nbsp; The definition of _IfcCoverings_ include both the coverings of building elements, such as flooring or cladding. and the covering of distribution elements, such as wrapping or sleeving.

The IFC specification provides two relationships:

* _IfcRelCoversBldgElements_ to assign coverings to elements. 
>> NOTE&nbsp; This relationship is now deprecated and replaced by _IfcRelAggregates_. 
* _IfcRelCoversSpaces_ to assign coverings to spaces   
>> NOTE&nbsp; This relationship is now deprecated and replaced by _IfcRelContainedInSpatialStructure_. 

Whether the relationship between the covering and the space, or between the covering and the element, is regarded as primary, has to be determined within the context of a model view definition.

> HISTORY&nbsp; New entity in IFC1.5

{ .deprecated}
> DEPRECATION&nbsp; The relationship _IfcRelCoversBldgElements_ shall not be used anymore, use _IfcRelAggregates_ instead.
