# IfcRigidOperation

A rigid operation specifies an offset in the coordinate reference system. It does not specify any conversion or distortion. It is a coordinate operation that tells that the whole virtual model is **translated** in the same way. For example, using lengths to translate along x,y,z; or using angles for a 2D translation (e.g., lambda, phi), plus a change in height.
<!-- end of short definition -->


> EXAMPLE If data is in truncated map coordinates (i.e., the map coordinates have the leading digits removed in x and y), then _IfcRigidOperation_ simply translates the data in x and y to replace the ignored leading digits. This is also known as subtraction.

> HISTORY New entity in IFC4X3_ADD1

## Attributes

### FirstCoordinate

The first coordinate of the translation. Can be a length measure in case of map coordinates or a plane angle measure in case of geographic reference systems.

### SecondCoordinate

The second coordinate of the translation. Can be a length measure in case of map coordinates or a plane angle measure in case of geographic reference systems.

### Height

Translation above (positive) or below (negative) the coordinate surface.

> NOTE In case of _IfcGeographicCRS_, *Height* is a translation relative to the geodetic datum ellipsoid's surface. In case of a _IfcProjectedCRS_, *Height* is a translation relative to the vertical datum.

## Formal Propositions

### SameCoordinateType

Restricts the value type of _FirstCoordinate_ and _SecondCoordinate_ to _IfcLengthMeasure_ or _IfcPlaneAngleMeasure_ and asserts the same type is used for both.
