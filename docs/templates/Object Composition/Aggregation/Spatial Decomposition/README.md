Spatial Decomposition
=====================

Provision of a spatial structure of the project by aggregating spatial elements. The spatial structure is a hierarchical tree of spatial elements ultimately assigned to the project. Decomposition refers to the relationship to a lower level element (e.g. this storey has spaces).

> NOTE&nbsp; The link between the project and the highest level spatial element is provided by this concept through _IfcRelContainedInSpatialStructure_ and not through declaration using _IfcRelDeclares_. This is a known anomaly introduced to maintain compatibility with earlier versions of this standard.

The order of spatial structure elements being included in the concept for builing projects are from low to high level: _IfcSpace_, _IfcBuildingStorey_, _IfcBuilding_, _IfcSite_ and _IfcProject_ with _IfcSite_, _IfcBuildingStorey_ and _IfcSpace_ being optional levels. Therefore an spatial structure element can only be part of an element at the same or higher level.

In addition a more general hierarchical tree of spatial elements can be created by using _IfcSpatialZone_, from low to high: _IfcSpatialZone_, _IfcSite_, and _IfcProject_, with _IfcSite_ being an optional level.

> NOTE&nbsp; The more general hiearchical tree has been introduced as an intermediate solution and stub for further extensions to support infrastructure works.

```
concept {
    IfcObjectDefinition:IsDecomposedBy -> IfcRelAggregates:RelatingObject
    IfcRelAggregates:RelatedObjects -> IfcSpatialElement
    IfcSpatialElement:Name -> IfcLabel
}
```
