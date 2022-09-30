# IfcRigidOperation

A rigid operation specifies an offset in the coordinate reference system. It does not specify any conversion or distortion only a translation. The coordinate axes of the _IfcGeometricRepresentationContext_ can rotate and set a new basis coordinate system.

> HISTORY New entity in IFC4X3_ADD1

## Attributes

### FirstCoordinate

The first coordinate of the translation. Can be a length measure in case of map coordinates or a plane angle measure in case of geographic reference systems.

### SecondCoordinate

The second coordinate of the translation. Can be a length measure in case of map coordinates or a plane angle measure in case of geographic reference systems.

### Height

Height above (positive) or below (negative) the coordinate surface.

## Formal Propositions

### SameCoordinateType

Restricts the value type of _FirstCoordinate_ and _SecondCoordinate_ to _IfcLengthMeasure_ or _IfcPlaneAngleMeasure_ and asserts the same type is used for both.
