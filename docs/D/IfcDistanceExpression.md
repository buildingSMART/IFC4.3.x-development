IfcDistanceExpression
=====================
An IfcDistanceExpression describes a point relative to a basis curve according
to distance along the basis curve in 3D or as projected onto the horizontal
plane, offset lateral to the basis curve according to the horizontal
orientation at the specified distance, offset vertical to the basis curve, and
an optional additional offset parallel to the basis curve that may be used to
address locations otherwise unreachable where the basis curve is tangentially
discontinuous.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometryresource/lexical/ifcdistanceexpression.htm)


Attribute definitions
---------------------
| Attribute          | Description                                                                                                                                                                                                                                                                                                                                                    |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DistanceAlong      | The distance along the basis curve, measured according to projection in the horizontal plane if AlongHorizontal is True, or according to 3D distance otherwise. If the basis curve refers to _IfcAlignmentCurve_ and AlongHorizontal is True, then this measurement directly corresponds to _IfcAlignment2DHorizontal_.                                        |
| OffsetLateral      | Offset horizontally perpendicular to the basis curve, where positive values indicate to the left of the basis curve as facing in the direction of the basis curve, and negative values indicate to the right. If DistanceAlong coincides with a point of tangential discontinuity (within precision limits), then the tangent of the previous segment governs. |
| OffsetLongitudinal | Offset parallel to the basis curve after applying DistanceAlong, OffsetLateral, and OffsetVertical to reach locations for the case of a tangentially discontinuous basis curve.                                                                                                                                                                                |
| OffsetVertical     | Offset vertical to the basis curve where positive values indicate vertically upwards in global coordinates at DistanceAlong, regardless of the slope of the basis curve at such point.                                                                                                                                                                         |
| AlongHorizontal    | Indicates whether DistanceAlong is measured according to horizontal projection of distance (if True), or 3D distance (if False or unset).                                                                                                                                                                                                                      |

