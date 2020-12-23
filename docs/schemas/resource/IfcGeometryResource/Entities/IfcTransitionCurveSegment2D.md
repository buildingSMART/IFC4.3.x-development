# IfcTransitionCurveSegment2D

An _IfcTransitionCurveSegment2D_ is a curve that transitions between a straight line and a circular arc (or the reverse).

## Attributes

### StartRadius
The radius of the curve at the start point. If the radius is not provided by a value, i.e. being “NIL” it is interpreted as INFINITE – the _StartPoint_ is at the point, where it does not have a curvature.

### EndRadius
The radius of the curve at the end point. If the radius is not provided by a value, i.e. being “NIL” it is interpreted as INFINITE – the end point is at the point, where it does not have a curvature.

### IsStartRadiusCCW
Indication of the curve starting counter-clockwise or clockwise. The orientation of the curve is IsCcw=”true”, if the spiral arc goes counter-clockwise as seen from the start point and start direction, or “to the left", and with IsCcw=”false” if the spiral arc goes clockwise, or “to the right”.

### IsEndRadiusCCW
Indication of the curve ending counter-clockwise or clockwise. The orientation of the clothoidal arc is IsCcw=”true”, if the spiral arc goes counter-clockwise as seen towards the end point and end direction, or “to the left", and with IsCcw=”false” if the spiral arc goes clockwise, or “to the right”.

### TransitionCurveType
Indicates the specific type of transition curve.
