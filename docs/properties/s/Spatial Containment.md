Spatial Containment
===================

The _Spatial Containment_ concept defines the relationship of physical elements, such as building elements, distribution elements, or furnishing elements as being contained within a spatial structure element.

Any subtype of _IfcElement_ may participate in two different containment relationships. The first (and in most implementation scenarios mandatory) relationship is the hierachical spatial containment, the second (optional) relationship is the aggregation within an element assembly.

* The subtypes of _IfcElement_ are placed within the project spatial hierarchy using the objectified relationship _IfcRelContainedInSpatialStructure_, refering to it by its inverse attribute _SELF\IfcElement.ContainedInStructure_. Subtypes of _IfcSpatialElement_ are valid spatial containers.
* The subtypes of _IfcElement_ may be aggregated into an element assembly using the objectified relationship _IfcRelAggregates_, refering to it by its inverse attribute _SELF\IfcObjectDefinition.Decomposes_. Any subtype of _IfcElement_ can be an element assembly, with _IfcElementAssembly_ as a special focus subtype. In this case it should not be additionally contained in the project spatial hierarchy, i.e. _SELF\IfcElement.ContainedInStructure_ should be _NIL_.
