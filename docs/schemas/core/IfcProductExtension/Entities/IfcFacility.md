# IfcFacility

A Facility (derived from _IfcSpatialStructureElement_) may be an _IfcBuilding_, an _IfcBridge_, an _IfcRailway_, an _IfcRoad_, an _IfcMarineFacility_ (or any other type of built facility defined in the future, such as IfcTunnel).

## Concepts

### Body Geometry

In the case of alignment based infrastructure, the geometric representation can be defined using IfcSectionedSolidHorizontal or IfcSweptAreaSolid.

### Product Local Placement

The placement for IfcFacility is defined in its supertype IfcProduct. It is defined by either IfcLocalPlacement or by _IfcLinearPlacement>/em> which define the local coordinate
 system  that is referenced by all geometric representations._

* The PlacementRelTo relationship of IfcObjectPlacement shall point (if relative placement is used) to the IfcSpatialStructureElement of type IfcSite, or of type IfcFacility (e.g. to position a facility relative to a facility complex, or a facility section to a facility).
* If the relative placement is not used, the absolute placement is defined within the world coordinate system.

### Spatial Composition

> NOTE  By using the inverse relationship _IfcFacility.Decomposes_ it references IfcProject || IfcSite || IfcFacility through _IfcRelAggregates.RelatingObject_. If it refers to another instance of IfcFacility, the referenced IfcFacility needs to have a different and higher CompositionType, i.e. COMPLEX (if the other IfcBuilding has ELEMENT), or ELEMENT (if the other IfcFacility has PARTIAL).

#### IfcProject

Direct assignment to project, if the facility is the outermost spatial container, and no site information is provided for the building projects

#### IfcSite

Assignment to site, if the facility is the spatial container for the building project with site information

#### IfcFacility

Assignment to another facility as spatial container, e.g. if this facility represents a facility section.

### Spatial Container

> NOTE  If there are building elements and/or other elements directly related to the IfcFacility (like a curtain wall spanning several stories), they are associated with the IfcFacility by using the objectified relationship IfcRelContainedInSpatialStructure. The IfcFacility references them by its inverse relationship: > *  _IfcFacility.ContainsElements_ -- referencing any subtype of IfcProduct (with the exception of other spatial structure element) by _IfcRelContainedInSpatialStructure.RelatedElements_.

#### IfcElement

Physical elements contained in the facility.

#### IfcAnnotation

Annotations that are directly related to the facility.

#### IfcPositioningElement

Positioning elements that are directly related to the facility.

### Spatial Decomposition

> NOTE  By using the inverse relationship _IfcFacility.IsDecomposedBy_ it references IfcFacility || IfcFacilityPart through _IfcRelAggregates.RelatedObjects_. If it refers to another instance of IfcFacility, the referenced IfcFacility needs to have a different and lower CompositionType, i.e. ELEMENT (if the other IfcFacility has COMPLEX), or PARTIAL (if the other IfcFacility has ELEMENT).

#### IfcFacilityPart

Spatial decomposition into facility parts.

#### IfcFacility

Spatial decomposition into other buildings, e.g. if this building represents a complex facilities that is subdivided into facility sections.

