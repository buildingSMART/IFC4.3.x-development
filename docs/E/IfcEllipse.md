IfcEllipse
==========
An _IfcEllipse_ is a curve consisting of a set of points whose distances to
two fixed points add to the same constant.  
  
The inherited _SELF\\\IfcConic.Position.Location_ is the center of the
_IfcEllipse_, and the inherited S_ELF\\\IfcConic.Position.Position.P[1]_ is
the direction of the _SemiAxis1_.  
  
  
  
![ellipse](../figures/ifcellipse-layout1.gif)  
|  

Definition of the _IfcEllipse_ within the a three-dimensional position  
coordinate system is shown in Figure 1.

  

It is placed within the object coordinate system of an element of which it is
a  
representation.

  
  
  
---|---  
  
  
  

Figure 1 -- Ellipse placement and parameterization

  
  
|  
  
  
  
  
> NOTE  An elliptical arc segment is defined by using the _IfcTrimmedCurve_
> with _BasisCurve_  
  
{ .extDef}  
> NOTE Definition according to ISO/CD 10303-42:1992  
> An ellipse is a conic section defined by the lengths of the semi-major and
> semi-minor diameters and the position (center or mid point of the line
> joining the foci) and orientation of the curve. Interpretation of the data
> shall be as follows:  
>  
>>  
>> ```  
>> C = position.location  
>> x = position.p[1]  
>> y = position.p[2]  
>> z = position.p[3]  
>> R1 = semi axis 1  
>> R2 = semi axis 2  
>> ```  
> and the ellipse is parameterized as:  
>  
>> ![formula](../figures/ifcellipse-math1.gif)  
> The parameterization range is 0 ≤ _u_ <≤ 2π (0 ≤ _u_ ≤ 360 degree). In the
> placement coordinate system defined above, the ellipse is the equation _C_ =
> 0, where  
>  
>> ![formula](../figures/ifcellipse-math2.gif)  
>>  
> The positive sense of the ellipse at any point is in the tangent direction,
> T, to the curve at the point, where  
>  
>> ![formula](../figures/ifcellipse-math3.gif)  
>>  
  
  
>  
> NOTE  Entity adapted from **ellipse** defined in ISO 10303-42  
  
> HISTORY  New entity in IFC1.0  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometryresource/lexical/ifcellipse.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                      |
|-------------|------------------------------------------------------------------------------------------------------------------|
| SemiAxis1   | The first radius of the ellipse which shall be positive. Placement.Axes[1] gives the direction of the SemiAxis1. |
| SemiAxis2   | The second radius of the ellipse which shall be positive.                                                        |

