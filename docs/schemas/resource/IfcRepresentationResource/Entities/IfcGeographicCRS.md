# IfcGeographicCRS

A _IfcGeographicCRS_ is a coordinate reference system (CRS) that uses a three-dimensional ellipsoid surface to reference locations on the Earth. Any location on Earth can be described by a point with longitude and latitude coordinates and the height above or below the ellipsoid surface.<!-- end of definition -->

> HISTORY New entity in IFC4X3_ADD1.

## Attributes

### PrimeMeridian

The identification of the meridian defining zero longitude in the used geographic CRS.

### AngleUnit

Unit of latitude and longitude coordinate axes composing the geographic coordinate system.

> NOTE  Only plane angle measures are in scope and both longitude and latitude coordinate axes of the geographic coordinate system shall have the same plane angle unit.

> NOTE  If _AngleUnit_ is omitted, the unit for latitude and longitude coordinate axes is taken from the default project angle units, as stated in _IfcProject.UnitInContext_.

### HeightUnit

Unit of the height coordinate axis of the geographic coordinate system.

> NOTE  Only length measures are in scope.

> NOTE  If _HeightUnit_ is omitted, the unit for the height coordinate axis is taken from the default project length units, as stated in _IfcProject.UnitInContext_.

## Formal Propositions

### AngleUnitIsPlaneAngle

The type of _AngleUnit_ in the operation shall be _IfcUnitEnum.PLANEANGLEUNIT_.

### HeightUnitIsLength

The type of _HeightUnit_ in the operation shall be _IfcUnitEnum.LENGTHUNIT_.
