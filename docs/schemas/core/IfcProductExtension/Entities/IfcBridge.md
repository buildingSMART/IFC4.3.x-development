# IfcBridge

A Bridge is civil engineering works that affords passage to pedestrians, animals, vehicles, and services above obstacles or between two points at a height above ground.

{ .extDef}
> NOTE  Definition from [ISO 6707-1:2014:
> Civil engineering works that affords passage to pedestrians, animals, vehicles, and services above obstacles or between two points at a height above ground.

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either _PredefinedType_ is unset or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED or _PredefinedType_.

## Concepts

### Body Geometry

### Object Predefined Type

### Product Local Placement

The local placement for IfcBridge is defined in its supertype IfcProduct. It is defined by IfcLocalPlacement or by _IfcLinearPlacement_ which defines the local coordinate system that is referenced by all geometric representations.

* The PlacementRelTo relationship of IfcLocalPlacement shall point (if relative placement is used) to the IfcSpatialStructureElement of type IfcSite, or of type IfcBuilding (e.g. to position a building relative to a building complex, or a building section to a building).
* If the relative placement is not used, the absolute placement is defined within the world coordinate system.

### Property Sets for Objects



### Property Sets for Objects



### Spatial Composition

> NOTE  By using the inverse relationship _IfcBridge.Decomposes_ it references IfcProject || IfcSite || IfcBridge through _IfcRelAggregates.RelatingObject_. If it refers to another instance of IfcBridge, the referenced IfcBridge needs to have a different and higher CompositionType, i.e. COMPLEX (if the other IfcBridge has ELEMENT), or ELEMENT (if the other IfcBridge has PARTIAL).

#### IfcProject

Direct assignment to project, if the bridge is the outermost spatial container, and no site information is provided for bridge projects

#### IfcSite

Assignment to site, if the bridge is the spatial container for the bridge project with site information

#### IfcBridge

Assignment to another bridge as spatial container, e.g. if this bridge represents a bridge section.

### Spatial Container

> NOTE  If there are building elements and/or other elements directly related to the IfcBridge, they are associated with the IfcBridge by using the objectified relationship IfcRelContainedInSpatialStructure. The IfcBridge references them by its inverse relationship: > *  _IfcBridge.ContainsElements_ -- referencing any subtype of IfcProduct (with the exception of other spatial structure element) by _IfcRelContainedInSpatialStructure.RelatedElements_.

#### IfcElement

Physical elements that are directly related to the building.

#### IfcAnnotation

Annotations that are directly related to the building.

#### IfcPositioningElement

Positioning elements that are directly related to the building.

### Spatial Decomposition

> NOTE  By using the inverse relationship _IfcBridge.IsDecomposedBy_ it references IfcBridge || IfcBridgePart through _IfcRelAggregates.RelatedObjects_. If it refers to another instance of IfcBridge, the referenced IfcBridge needs to have a different and lower CompositionType, i.e. ELEMENT (if the other IfcBridge has COMPLEX), or PARTIAL (if the other IfcBridge has ELEMENT).

#### IfcBridgePart

Spatial decomposition into bridge parts

#### IfcBridge

Spatial decomposition into other bridges, e.g. if this bridge represents a complex bridge that is subdivided into bridge sections.

### Spatial Service Connectivity



