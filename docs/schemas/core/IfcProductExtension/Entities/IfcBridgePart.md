# IfcBridgePart

Part of a bridge.<!-- end of definition -->

## Concepts

### Body Geometry

### Object Predefined Type

### Product Local Placement

The local placement for _IfcBridgePart_ is defined in its supertype _IfcProduct_. It is defined by the _IfcLocalPlacement_ or _IfcLinearPlacement_, which defines the local coordinate system that is referenced by all geometric representations.

* The *PlacementRelTo* relationship of _IfcLocalPlacement_ or _IfcLinearPlacement_ shall point (if relative placement is used) to the _IfcSpatialStructureElement_ of type _IfcBridge_, or of type _IfcBridgePart_ (e.g. to position a bridge part relative to a bridge part complex, or a partial bridge part to a bridge part).
* If the relative placement is not used, the absolute placement is defined within the world coordinate system.

### Spatial Composition

> NOTE  By using the inverse relationship _IfcBridgePart.Decomposes_ it references (_IfcBridge_|| _IfcBridgePart_) through _IfcRelAggregates.RelatingObject_, the referenced _IfcBridgePart_ needs to have a different and higher *CompositionType*, i.e. COMPLEX (if the other _IfcBridgePart_ has ELEMENT), or ELEMENT (if the other _IfcBridgePart_ has PARTIAL).

#### IfcBridge

Assignment to the bridge, where the bridge part is a part of.

#### IfcBridgePart

Assignment to another bridge part, e.g. if this bridge part is a part that refers to another bridge part.

### Spatial Container

If there are building elements and/or other elements directly related to the _IfcBridgePart_ (like most building elements, such as walls, columns, etc.), they are associated with the _IfcBridgePart_ by using the objectified relationship _IfcRelContainedInSpatialStructure_. The _IfcBridgePart_ references them by its inverse relationship:

* _IfcBridgePart.ContainsElements_ -- referencing any subtype of _IfcProduct_ (with the exception of other spatial structure element) by _IfcRelContainedInSpatialStructure.RelatedElements_.

Elements can also be referenced in an _IfcBridgePart_, for example, if they span through several storeys. This is expressed by using the objectified relationship _IfcRelReferencedInSpatialStructure_. Systems, such as building service or electrical distribution systems, zonal systems, or structural analysis systems, relate to _IfcBridgePart_ by using the objectified relationship _IfcRelServicesBuildings_.

### Spatial Decomposition

> NOTE  By using the inverse relationship _IfcBridgePart.IsDecomposedBy_ it references _IfcBridgePart_ through _IfcRelAggregates.RelatedObjects_. If it refers to another instance of _IfcBridgePart_, the referenced _IfcBridgePart_ needs to have a different and lower *CompositionType*, i.e. ELEMENT (if the other _IfcBridgePart_ has COMPLEX), or PARTIAL (if the other _IfcBridgePart_ has ELEMENT).

#### IfcBridgePart

Spatial decomposition into bridge parts, if this bridge part is a main bridge part having subdivisions.
