# IfcFacilityPart

_IfcFacilityPart_ provides for spatial breakdown of built facilities. It may be further specialised according to the type of facility being broken down.

## Attributes

### PredefinedType


### UsageType


## Formal Propositions

### CorrectPredefinedType
Either _PredefinedType_ is unset or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED or _PredefinedType_.

## Concepts

### Body Geometry

The body (or solid model) geometric representation (if the facility part has an independent geometric representation) of IfcFacilityPart is defined using faceted B-Rep capabilities (with or without voids), based on the IfcFacetedBrep or on the IfcFacetedBrepWithVoids or in the case of alignment based infrastructure using IfcSectionedSolidHorizontal optionally IfcSweptAreaSolid.

> NOTE  Since the facility part shape is usually described by the exterior facility elements, an independent shape representation shall only be given, if the facility part is exposed independently from its constituting elements and such independent geometric representation may be prohibited in model view definitions.

### Product Local Placement

The local placement for IfcFacilityPart is defined in its supertype IfcProduct. It is defined by the IfcLocalPlacement, which defines the local coordinate system that is referenced by all geometric representations or by IfcLinearPlacement which measures along a linear positioning element.

* The PlacementRelTo attribute of IfcObjectPlacement shall point (if relative placement is used) to the IfcSpatialStructureElement of type IfcFacility, or of type IfcFacilityPart (e.g. to position a facility relative to a facility part complex, or a partial facility part to a facility part).
* If the relative placement is not used, the absolute placement is defined within the world coordinate system.

### Spatial Composition

> NOTE  By using the inverse relationship _IfcFacilityPart.Decomposes_ it references (IfcFacility || IfcFacilityPart) through _IfcRelAggregates.RelatingObject_IfcFacilityPart_, the referenced
IfcFacilityPart needs to have a different and higher
 CompositionType, i.e. COMPLEX (if the other IfcFacilityPart has ELEMENT), or ELEMENT (if the other
 IfcFacilityPart has PARTIAL)._

#### IfcBuilding

Assignment to the building, where the building storey is a part of.

#### IfcBuildingStorey

Assignment to another building storey, e.g. if this building storey is a partial storey that refer to another storey.

### Spatial Container

If there are building elements and/or other elements directly related to the IfcFacilityPart (like most building elements, such as walls, columns, etc.), they are associated with the IfcFacilityPart by using the objectified relationship IfcRelContainedInSpatialStructure. The IfcFacilityPart references them by its inverse relationship:

* _IfcFacilityPart.ContainsElements_ -- referencing any subtype of IfcProduct (with the exception of other spatial structure element) by _IfcRelContainedInSpatialStructure.RelatedElements_.

Elements can also be referenced in an IfcFacilityPart, for example, if they span through several storeys. This is expressed by using the objectified relationship IfcRelReferencedInSpatialStructure. Systems, such as building service or electrical distribution systems, zonal systems, or structural analysis systems, relate to IfcFacilityPart by using the objectified relationship IfcRelServicesBuildings.

