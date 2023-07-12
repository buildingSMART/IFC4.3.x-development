# IfcGeographicCRS

A _IfcGeographicCRS_ is a coordinate reference system (CRS) that uses a three-dimensional ellipsoid surface to reference locations on the Earth. Any location on Earth can be described by a point with longitude and latitude coordinates and the height above or below the ellipsoid surface.

> HISTORY New entity in IFC4X3_ADD1.

## Attributes

### GeodeticDatum

Name by which this datum is identified.

### PrimeMeridian

The identification of the meridian defining zero longitude in the used geographic CRS.

### Unit

Unit of the coordinate tuple composing the coordinate system.

## Formal Propositions

### IsPlaneAngleUnit

The map unit shall be given, if present, as a plane angle unit.
