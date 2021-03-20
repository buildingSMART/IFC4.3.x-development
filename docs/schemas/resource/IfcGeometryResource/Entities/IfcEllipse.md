# IfcEllipse

An _IfcEllipse_ is a curve consisting of a set of points whose distances to two fixed points add to the same constant.

The inherited _SELF\IfcConic.Position.Location_ is the center of the _IfcEllipse_, and the inherited S_ELF\IfcConic.Position.Position.P[1]_ is the direction of the _SemiAxis1_.

<table summary="example" cellpadding="2" cellspacing="2">
<tr>
<td><img src="../../../../figures/ifcellipse-layout1.gif" alt="ellipse" width="400" height="300" border="0"></td>
<td style="vertical-align:bottom; text-align:left;">
<p><span style="font-size:smaller">Definition of the <em>IfcEllipse</em> within the a three-dimensional position
coordinate system is shown in Figure 1.</span></p>
<p><span style=" font-size:smaller;">It is placed within the object coordinate system of an element of which it is a
representation.</span></p>
</td>
</tr>
<tr>
<td>
<p class="figure">Figure 1 &mdash; Ellipse placement and parameterization</p>
</td>
<td>&nbsp;</td>
</tr>
</table>

> NOTE&nbsp; An elliptical arc segment is defined by using the _IfcTrimmedCurve_ with _BasisCurve_

{ .extDef}
> NOTE Definition according to ISO/CD 10303-42:1992  
> An ellipse is a conic section defined by the lengths of the semi-major and semi-minor diameters and the position (center or mid point of the line joining the foci) and orientation of the curve. Interpretation of the data shall be as follows:
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
>> ![formula](../../../../figures/ifcellipse-math1.gif)
> The parameterization range is 0 &le; _u_ &lt;&le; 2&pi; (0 &le; _u_ &le; 360 degree). In the placement coordinate system defined above, the ellipse is the equation _C_ = 0, where
> 
>> ![formula](../../../../figures/ifcellipse-math2.gif)
>>
> The positive sense of the ellipse at any point is in the tangent direction, T, to the curve at the point, where
> 
>> ![formula](../../../../figures/ifcellipse-math3.gif)
>>


> 
> NOTE&nbsp; Entity adapted from **ellipse** defined in ISO 10303-42

> HISTORY&nbsp; New entity in IFC1.0

## Attributes

### SemiAxis1
The first radius of the ellipse which shall be positive. Placement.Axes[1] gives the direction of the SemiAxis1.

### SemiAxis2
The second radius of the ellipse which shall be positive.
