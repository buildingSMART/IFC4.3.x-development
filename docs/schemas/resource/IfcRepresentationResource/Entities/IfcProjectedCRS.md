# IfcProjectedCRS

_IfcProjectedCRS_ is a coordinate reference system of the map to which the map translation of the local engineering coordinate system of the construction or facility engineering project relates. The _MapProjection_ and _MapZone_ attributes uniquely identify the projection to the underlying geographic coordinate reference system, provided that they are well-known in the receiving application. The projected coordinate reference system is assumed to be a 2D or 3D right-handed Cartesian coordinate system, the optional _MapUnit_ attribute can be used determine the length unit used by the map.

{ .extDef}
> NOTE&nbsp; Definition from OpenGIS Abstract Specification, Topic 2:  
> A 2D (or with vertical coordinate axis 3D) coordinate reference system used to approximate the shape of the earth on a planar surface, but in such a way that the distortion that is inherent to the approximation is carefully controlled and known. Distortion correction is commonly applied to calculated bearings and distances to produce values that are a close match to actual field values.

The unambiguous identifier by which the coordinate reference system is know, is stored in the inherited _Name_ attribute. Well defined identifiers include the map projection and also the map zone information. In these cases the _MapProjection_ and the _MapZone_ attributes can be omitted.

> EXAMPLE&nbsp; The identifier 'EPSG:25832' defines the map projection 'UTM' and the zone '32N' in additon to the geodetic and vertical datum.

> HISTORY&nbsp; New entity in IFC4.

## Attributes

### MapProjection
Name by which the map projection is identified.

{ .examples}
> EXAMPLE&nbsp; map projects include: { .note}
> * UTM
> * Gaus-Krueger

### MapZone
Name by which the map zone, relating to the _MapProjection_, is identified. 

{ .examples}
> EXAMPLE&nbsp; { .note}
> * for UTM, the zone number, like 32 for UTM32
> * for Gaus-Krueger, the zones of longitudinal width, like 3'

### MapUnit
Unit of the coordinate axes composing the map coordinate system.
> NOTE 1&nbsp; Only length measures are in scope and all two or three axes of the map coordinate system shall have the same length unit.
> NOTE 2&nbsp; If MapUnit is omited, the unit for the coordinate axes is taken from the default units, as stated in IfcProject.UnitInContext.

## Formal Propositions

### IsLengthUnit
The map unit shall be given, if present, as a length unit.
