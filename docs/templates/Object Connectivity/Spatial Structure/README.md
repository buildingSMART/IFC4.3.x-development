Spatial Structure
=================

Spatial structures, such as site, building, storey, or spaces, may contain physical elements, including building elements, distribution elements, and furnishing elements. The containment relationship between the physical elements and the spatial structures is hierarchical, i.e. a physical element shall only be contained within a single spatial structure.

> EXAMPLE  An _IfcBeam_ is placed within the spatial hierarchy using the objectified relationship _IfcRelContainedInSpatialStructure_, refering to it by its inverse attribute _SELF\IfcElement.ContainedInStructure_. Subtypes of _IfcSpatialStructureElement_ are valid spatial containers, with _IfcBuildingStorey_ being the default container.

The spatial containment relationship, together with the Spatial decomposition relationship, being hierarchical as well, establishes the hiearchical project tree structure in a building information model.

> EXAMPLE  The _IfcBuildingStorey_ that logically contains the _IfcBeam_ decomposes the _IfcBuilding_ using the _IfcRelAggregates_ relationship. Therefore the _IfcBeam_ is also indirectly contained in the building.
