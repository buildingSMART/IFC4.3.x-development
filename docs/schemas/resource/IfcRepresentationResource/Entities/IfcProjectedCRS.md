# IfcProjectedCRS

_IfcProjectedCRS_ is a coordinate reference system of the map to which the map translation of the local engineering coordinate system of the construction or facility engineering project relates. The _MapProjection_ and _MapZone_ attributes uniquely identify the projection to the underlying geographic coordinate reference system, provided that they are well-known in the receiving application. The projected coordinate reference system is assumed to be a 2D or 3D right-handed Cartesian coordinate system, the optional _MapUnit_ attribute can be used determine the length unit used by the map.

{ .extDef}
> NOTE  Definition from OpenGIS Abstract Specification, Topic 2:
> A 2D (or with vertical coordinate axis 3D) coordinate reference system used to approximate the shape of the earth on a planar surface, but in such a way that the distortion that is inherent to the approximation is carefully controlled and known. Distortion correction is commonly applied to calculated bearings and distances to produce values that are a close match to actual field values.

In IFC, the _IfcProjectedCRS_ can also be used to represent a **Compound coordinate reference system**, which combines the coordinate of two other coordinate systems. For example, a compound 3D coordinate system can be made of a horizontal coordinate system and a vertical coordinate system.

> EXAMPLE  The code EPSG:9286 (ETRS89 + NAP height), is the combination of a Geographic CS (ETRS89) and a Vertical CS (NAP height). Or the code EPSG:9306 (HS2 Survey Grid + HS2-VRF height), is the combination of a Projected CS (HS2 Survey Grid), and a Vertical CS (HS2-VRF height). These examples, using EPSG codes, also have a corresponding description using OGC WKT literals.

> NOTE  The Well Known Text (WKT) definition of an _IfcCoordinateReferenceSystem_ is done by means of its inverse attribute *WellKnownText* referenced by an _IfcWellKnownText_.

The unambiguous identifier by which the coordinate reference system is know, is stored in the inherited _Name_ attribute. Well defined identifiers include the map projection and also the map zone information. In these cases the _MapProjection_ and the _MapZone_ attributes can be omitted.

> EXAMPLE  The identifier 'EPSG:25832' defines the map projection 'UTM' and the zone '32N' in addition to the geodetic and vertical datum.

> HISTORY  New entity in IFC4.

## Attributes

### GeodeticDatum
Name by which this datum is identified. The geodetic datum is associated with the coordinate reference system and indicates the shape and size of the rotation ellipsoid and this ellipsoid's connection and orientation to the actual globe/earth. It needs to be provided, if the _Name_ identifier does not unambiguously define the geodetic datum as well.

{ .examples}
> EXAMPLE  geodetic datums include: { .note}
> * ED50
> * EUREF89
> * WSG84

### VerticalDatum
Name by which the vertical datum is identified. The vertical datum is associated with the height axis of the coordinate reference system and indicates the reference plane and fundamental point defining the origin of a height system. It needs to be provided, if the _Name_ identifier does not unambiguously define the vertical datum as well and if the coordinate reference system is a 3D reference system.

{ .examples}
> EXAMPLE  vertical datums include: { .note}
> * DHHN92: the German 'Haupth&ouml;hennetz'
> * EVRS2007; the European Vertical Reference System

### MapProjection
Name by which the map projection is identified.

{ .examples}
> EXAMPLE  map projects include: { .note}
> * UTM
> * Gaus-Krueger

### MapZone
Name by which the map zone, relating to the _MapProjection_, is identified.

{ .examples}
> EXAMPLE  { .note}
> * for UTM, the zone number, like 32 for UTM32
> * for Gaus-Krueger, the zones of longitudinal width, like 3'

### MapUnit

Unit of the coordinate axes composing the map coordinate system.

> NOTE 1  Only length measures are in scope and all two or three axes of the map coordinate system shall have the same length unit.

> NOTE 2  If MapUnit is omitted, the unit for the coordinate axes is taken from the default units, as stated in IfcProject.UnitInContext.

## Formal Propositions

### IsLengthUnit
The map unit shall be given, if present, as a length unit.
