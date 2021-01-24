# IfcPointByDistanceExpression

An _IfcPointByDistanceExpression_ describes a point relative to a basis curve according to distance along the basis curve. The offsets default  to the initial context of the curve relative to it's tangent either specified in _IfcProduct.Placement_ or in the case of a segmented curve to the _IfcCurveSegment_ _StartPlacement_ where the values correspond to the following:
* lateral to the basis curve
* offset vertical to the basis curve
* optional additional offset parallel to the basis curve that may be used to address locations otherwise unreachable where the basis curve is tangentially discontinuous.

## Attributes

### DistanceAlong
The distance along the basis curve measured as either a _IfcLengthMeasure_ or _IfcParameterValue_.

### OffsetLateral
Default offset horizontally is measured perpendicular to the basis curve, where positive values indicate to the left of the basis curve as facing in the positive parametrization direction of the basis curve, and negative values indicate to the right. If DistanceAlong coincides with a point of tangential discontinuity (within precision limits), then the tangent of the previous segment governs.

### OffsetVertical
Default offset vertical to the basis curve where positive values indicate perpendicular to the tangent at DistanceAlong in the plane of the tangent perpendicular to the global XY plane.

### OffsetLongitudinal
Offset parallel to the basis curve after applying DistanceAlong, OffsetLateral, and OffsetVertical to reach locations for the case of a tangentially discontinuous basis curve.

### BasisCurve


### Dim

