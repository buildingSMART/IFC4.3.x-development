IfcPointByDistanceExpression
============================

An _IfcPointByDistanceExpression_ describes a point relative to a basis curve according to distance along the basis curve. The offsets default  to the initial context of the curve relative to it's tangent either specified in _IfcProduct.Placement_ or in the case of a segmented curve to the _IfcCurveSegment_ _StartPlacement_ where the values correspond to the following:
* lateral to the basis curve
* offset vertical to the basis curve
* optional additional offset parallel to the basis curve that may be used to address locations otherwise unreachable where the basis curve is tangentially discontinuous.
