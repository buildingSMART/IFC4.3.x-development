IfcTransitionCurveSegment2D
===========================
An _IfcTransitionCurveSegment2D_ is a curve that transitions between a
straight line and a circular arc (or the reverse).  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometryresource/lexical/ifctransitioncurvesegment2d.htm)


Attribute definitions
---------------------
| Attribute           | Description                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StartRadius         | The radius of the curve at the start point. If the radius is not provided by a value, i.e. being \X2\201C\X0\NIL\X2\201D\X0\ it is interpreted as INFINITE \X2\2013\X0\ the _StartPoint_ is at the point, where it does not have a curvature.                                                                                                                                               |
| EndRadius           | The radius of the curve at the end point. If the radius is not provided by a value, i.e. being \X2\201C\X0\NIL\X2\201D\X0\ it is interpreted as INFINITE \X2\2013\X0\ the end point is at the point, where it does not have a curvature.                                                                                                                                                    |
| IsStartRadiusCCW    | Indication of the curve starting counter-clockwise or clockwise. The orientation of the curve is IsCcw=\X2\201D\X0\true\X2\201D\X0\, if the spiral arc goes counter-clockwise as seen from the start point and start direction, or \X2\201C\X0\to the left", and with IsCcw=\X2\201D\X0\false\X2\201D\X0\ if the spiral arc goes clockwise, or \X2\201C\X0\to the right\X2\201D\X0\\.       |
| IsEndRadiusCCW      | Indication of the curve ending counter-clockwise or clockwise. The orientation of the clothoidal arc is IsCcw=\X2\201D\X0\true\X2\201D\X0\, if the spiral arc goes counter-clockwise as seen towards the end point and end direction, or \X2\201C\X0\to the left", and with IsCcw=\X2\201D\X0\false\X2\201D\X0\ if the spiral arc goes clockwise, or \X2\201C\X0\to the right\X2\201D\X0\\. |
| TransitionCurveType | Indicates the specific type of transition curve.                                                                                                                                                                                                                                                                                                                                            |

