IfcOffsetCurveByDistances
=========================
An _IfcOffsetCurveByDistances_ is a curve defined by a list of offsets along
its _BasisCurve_. If only one offset is provided, it indicates a constant
offset along the extents of the basis curve.  
  
Figure 1 illustrates eight instances of _IfcOffsetCurveByDistances_ (in green)
defined relative to an _IfcAlignmentCurve_ (in blue).  
  
!["spatial structure"](../figures/ifcoffsetcurvebydistances.png "Figure 1 --
Offset curve by distances")  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometryresource/lexical/ifcoffsetcurvebydistances.htm)


Attribute definitions
---------------------
| Attribute    | Description                                                                                            |
|--------------|--------------------------------------------------------------------------------------------------------|
| OffsetValues |                                                                                                        |
| Tag          | Optional identifier of the curve, which may be used to correlate points from a variable cross-section. |

