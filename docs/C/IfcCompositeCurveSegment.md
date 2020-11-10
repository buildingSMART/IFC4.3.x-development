IfcCompositeCurveSegment
========================
An _IfcCompositeCurveSegment_ is a bounded curve constructed for the sole
purpose to be a segment within an _IfcCompositeCurve_.  
  
{ .extDef}  
> NOTE  Definition according to ISO/CD 10303-42:1992  
> A composite curve segment is a bounded curve together with transition
> information which is used to construct a composite curve.  
  
> NOTE  Entity adapted from **composite_curve_segment** defined in ISO
> 10303-42.  
  
> HISTORY  New entity in IFC1.0  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometryresource/lexical/ifccompositecurvesegment.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                                                                                                                                                                                                                                |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UsingCurves |                                                                                                                                                                                                                                                                                                                                                                            |
| ParentCurve |                                                                                                                                                                                                                                                                                                                                                                            |
| Transition  | The state of transition (i.e., geometric continuity from the last point of this segment to the first point of the next segment) in a composite curve.                                                                                                                                                                                                                      |
| SameSense   | An indicator of whether or not the sense of the segment agrees with, or opposes, that of the parent curve. If _SameSense_ is false, the point with highest parameter value is taken as the first point of the segment.\X\0D> NOTE  If the datatype of _ParentCurve_ is _IfcTrimmedCurve_, the value of _SameSense_ overrides the value of _IfcTrimmedCurve.SenseAgreement_ |
| Dim         | The space dimensionality of this class, defined by the dimensionality of the first ParentCurve.                                                                                                                                                                                                                                                                            |

