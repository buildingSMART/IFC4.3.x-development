# IfcFacility

A Facility (derived from _IfcSpatialStructureElement_) may be an _IfcBuilding_, an _IfcBridge_, an _IfcRailway_, an _IfcRoad_, an _IfcMarineFacility_ (or any other type of built facility defined in the future, such as IfcTunnel).<!-- end of definition -->

## Concepts

### Body Geometry

In the case of alignment based infrastructure, the geometric representation can be defined using _IfcSectionedSolidHorizontal_ or _IfcSweptAreaSolid_.

### Product Local Placement

The placement for _IfcFacility_ is defined in its supertype _IfcProduct_. It is defined by either _IfcLocalPlacement_ or by _IfcLinearPlacement> which defines the local coordinate system that is referenced by all geometric representations.

* The _PlacementRelTo_ relationship of _IfcObjectPlacement_ shall point (if relative placement is used) to the _IfcSpatialStructureElement_ of type _IfcSite_, or of type _IfcFacility_ (e.g. to position a facility relative to a facility complex, or a facility section to a facility).
* If the relative placement is not used, the absolute placement is defined within the world coordinate system.

### Spatial Composition

> NOTE  By using the inverse relationship _IfcFacility.Decomposes_ it references _IfcProject_ || _IfcSite_ || _IfcFacility_ through _IfcRelAggregates.RelatingObject_. If it refers to another instance of _IfcFacility_, the referenced _IfcFacility_ needs to have a different and higher _CompositionType_, i.e. _COMPLEX_ (if the other _IfcBuilding_ has _ELEMENT_), or _ELEMENT_ (if the other _IfcFacility_ has _PARTIAL_).

#### IfcProject

Direct assignment to project, if the facility is the outermost spatial container, and no site information is provided for the building projects.

#### IfcSite

Assignment to site, if the facility is the spatial container for the building project with site information.

#### IfcFacility

Assignment to another facility as spatial container, e.g. if this facility represents a facility section.

### Spatial Container

> NOTE  If there are building elements and/or other elements directly related to the _IfcFacility_ (like a curtain wall spanning several stories), they are associated with the _IfcFacility_ by using the objectified relationship _IfcRelContainedInSpatialStructure_. The _IfcFacility_ references them by its inverse relationship _IfcFacility.ContainsElements_, referencing any subtype of _IfcProduct_ (with the exception of other spatial structure element) by _IfcRelContainedInSpatialStructure.RelatedElements_.

#### IfcElement

Physical elements contained in the facility.

#### IfcAnnotation

Annotations that are directly related to the facility.

#### IfcPositioningElement

Positioning elements that are directly related to the facility.

### Spatial Decomposition

> NOTE  By using the inverse relationship _IfcFacility.IsDecomposedBy_ it references _IfcFacility_ || _IfcFacilityPart_ through _IfcRelAggregates.RelatedObjects_. If it refers to another instance of _IfcFacility_, the referenced _IfcFacility_ needs to have a different and lower _CompositionType_, i.e. _ELEMENT_ (if the other _IfcFacility_ has _COMPLEX_), or _PARTIAL_ (if the other _IfcFacility_ has _ELEMENT_).

#### IfcFacilityPart

Spatial decomposition into facility parts.

#### IfcFacility

Spatial decomposition into other buildings, e.g. if this building represents a complex facilities that is subdivided into facility sections.

