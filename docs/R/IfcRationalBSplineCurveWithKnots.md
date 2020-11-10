IfcRationalBSplineCurveWithKnots
================================
A rational B-spline curve with knots is a B-spline curve described in terms of
control points and basic functions. It describes weights in addition to the
control points defined at the supertype _IfcBSplineCurve_.  
  
All weights shall be positive and the curve is given by:  
  
> ![Math](../figures/ifcrationalbsplinecurvewithknots-math1.gif)  
  
where  
  
  
  
 _k_ +1  
| number of control points  
  
---|---  
  
  
P _i_  
|  control points  
  
  
  
 _w i_  
| weights  
  
  
  
 _d_  
|  degree  
  
  
  
  
> NOTE  Entity adapted from **rational_b_spline_curve** in ISO 10303-42.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometryresource/lexical/ifcrationalbsplinecurvewithknots.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------|
| WeightsData | The supplied values of the weights.                                                             |
| Weights     | The array of weights associated with the control points. This is derived from the weights data. |

