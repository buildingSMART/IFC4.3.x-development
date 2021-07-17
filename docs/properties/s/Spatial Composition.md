Spatial Composition
===================

Provision of a spatial structure of the project by aggregating spatial elements. The spatial structure is a hierarchical tree of spatial elements ultimately assigned to the project. Composition refers to the relationship to a higher level element (e.g. this storey is part of a building).

> NOTE&nbsp; The link between the highest level spatial element and the project is provided by this concept through _IfcRelContainedInSpatialStructure_ and not through declaration using _IfcRelDeclares_. This is a known anomaly intruduced to maintain compatibility with earlier versions of this standard.

The order of spatial structure elements being included in the concept for builing projects are from high to low level: _IfcProject_, _IfcSite_, _IfcBuilding_, _IfcBuildingStorey_, and _IfcSpace_ with _IfcSite_, _IfcBuildingStorey_ and _IfcSpace_ being optional levels. Therefore an spatial structure element can only be part of an element at the same or higher level.

In addition a more general hierarchical tree of spatial elements can be created by using _IfcSpatialZone_, from high to low: _IfcProject_, _IfcSite_, and _IfcSpatialZone_ with _IfcSite_ being an optional level.

> NOTE&nbsp; The more general hiearchical tree has been introduced as an intermediate solution and stub for further extensions to support infrastructure works.
