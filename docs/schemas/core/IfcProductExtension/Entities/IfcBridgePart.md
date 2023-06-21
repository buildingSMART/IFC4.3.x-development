# IfcBridgePart

Part of a bridge.

## Concepts

### Body Geometry

### Object Predefined Type

### Product Local Placement

The local placement for IfcBridgePart is defined in its supertype IfcProduct. It is defined by the IfcLocalPlacement or IfcLinearPlacement, which defines the local coordinate system that is referenced by all geometric representations.

* The PlacementRelTo relationship of IfcLocalPlacement or IfcLinearPlacement shall point (if relative placement is used) to the IfcSpatialStructureElement of type IfcBridge, or of type IfcBridgePart (e.g. to position a bridge part relative to a bridge part complex, or a partial bridge part to a bridge part).
* If the relative placement is not used, the absolute placement is defined within the world coordinate system.

### Spatial Composition

> NOTE  By using the inverse relationship _IfcBridgePart.Decomposes_ it references (IfcBridge || IfcBridgePart) through _IfcRelAggregates.RelatingObject_IfcBridgePart_, the referenced
IfcBridgePart needs to have a different and higher
 CompositionType, i.e. COMPLEX (if the other IfcBridgePart has ELEMENT), or ELEMENT (if the other
 IfcBridgePart has PARTIAL)._

#### IfcBridge

Assignment to the bridge, where the bridge part is a part of.

#### IfcBridgePart

Assignment to another bridge part, e.g. if this bridge part is a part that refers to another bridge part.

### Spatial Container

If there are building elements and/or other elements directly related to the IfcBridgePart (like most building elements, such as walls, columns, etc.), they are associated with the IfcBridgePart by using the objectified relationship IfcRelContainedInSpatialStructure. The IfcBridgePart references them by its inverse relationship:

* _IfcBridgePart.ContainsElements_ -- referencing any subtype of IfcProduct (with the exception of other spatial structure element) by _IfcRelContainedInSpatialStructure.RelatedElements_.

Elements can also be referenced in an IfcBridgePart, for example, if they span through several storeys. This is expressed by using the objectified relationship IfcRelReferencedInSpatialStructure. Systems, such as building service or electrical distribution systems, zonal systems, or structural analysis systems, relate to IfcBridgePart by using the objectified relationship IfcRelServicesBuildings.

### Spatial Decomposition

> NOTE  By using the inverse relationship _IfcBridgePart.IsDecomposedBy_ it references IfcBridgePart through _IfcRelAggregates.RelatedObjects_. If it refers to another instance of IfcBridgePart, the referenced IfcBridgePart needs to have a different and lower CompositionType, i.e. ELEMENT (if the other IfcBridgePart has COMPLEX), or PARTIAL (if the other IfcBridgePart has ELEMENT).

> NOTE  Multi storey spaces shall be spatially contained by only a single building storey, usually it is the building storey where the base of the space lies.

#### IfcBridgePart

Spatial decomposition into bridge parts, if this bridge part is a main bridge part having subdivisions.

