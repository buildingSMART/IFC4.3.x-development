IfcAlignment2DCantSegTransition
===============================
The cant transition segment is a 2D transition curve using the inherited
attributes from IfcAlignment2DCantSegment.  


Attribute definitions
---------------------
| Attribute           | Description                                                                                                                                                                                                                                                                                             |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StartRadius         | The radius of the curve at the start point. If the radius is not provided by a value, i.e. being “NIL” it is interpreted as INFINITE – the StartPoint is at the point, where it does not have a curvature.                                                                                              |
| EndRadius           | The radius of the curve at the end point. If the radius is not provided by a value, i.e. being “NIL” it is interpreted as INFINITE – the end point is at the point, where it does not have a curvature.                                                                                                 |
| IsStartRadiusCCW    | Indication of the curve starting counter-clockwise or clockwise. The orientation of the curve is IsCcw=”true”, if the spiral arc goes counter-clockwise as seen from the right side of the curve, or “to the upside", and with IsCcw=”false” if the spiral arc goes clockwise, or “to the downside”.    |
| IsEndRadiusCCW      | Indication of the curve ending counter-clockwise or clockwise. The orientation of the clothoidal arc is IsCcw=”true”, if the spiral arc goes counter-clockwise as seen from right side of the curve, or “to the upside", and with IsCcw=”false” if the spiral arc goes clockwise, or “to the downside”. |
| TransitionCurveType | Indicates the specific type of transition curve.                                                                                                                                                                                                                                                        |

