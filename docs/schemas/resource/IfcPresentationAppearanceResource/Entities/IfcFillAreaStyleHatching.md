# IfcFillAreaStyleHatching

The _IfcFillAreaStyleHatching_ is used to define simple, vector-based hatching patterns, based on styled straight lines. The curve font, color and thickness is given by the _HatchLineAppearance_, the angle by the _HatchLineAngle_ and the distance to the next hatch line by _StartOfNextHatchLine_, being either an offset distance or a vector.

{ .extDef}
> NOTE&nbsp; Definition according to ISO 10303-46:  
> The fill area style hatching defines a styled pattern of curves for hatching an annotation fill area or a surface.

> NOTE&nbsp; If the hatch pattern involves two (potentially crossing) rows of hatch lines, then two instances of _IfcFillAreaStyleHatching_ should be assigned to the _IfcFillAreaStyle_. Both share the same (virtual) point of origin of the hatching that is used by the reference hatch line (or the _PointOfReferenceHatchLine_ if there is an offset).

For better control of the hatching appearance, when using hatch lines with other fonts then continuous, the _PatternStart_ allows to offset the start of the curve font pattern along the reference hatch line (if not given, the _PatternStart_ is at zero distance from the virtual point of origin). If the reference hatch line does not go through the origin (of the virtual hatching coordinate system), it can be offset by using the _PatternStart_ .

> NOTE&nbsp; The coordinates of the _PatternStart_ are given relative to the origin of the object coordinate of _IfcAnnotationFillArea_, or if present, the _FillAreaTarget_ attribute of _IfcAnnotationFillArea_. The measure values are given in global drawing length units, representing a model hatching, and can be translated into drawing units by the _TargetScale_ for a scale depended _IfcGeometricRepresentationSubcontext_, if provided.

{ .deprecated}
> DEPRECATION&nbsp; The use of _PointOfReferenceHatchLine_ is deprecated.

<small>Figure 1 illustrates hatch attributes.</small>

<table>
<tr>
<td>
<table border="0" cellpadding="2" cellspacing="2" width="100%">
<tbody>
<tr>
<td align="left" valign="top" width="280"><img src="../../../../../../figures/ifcfillareastylehatching_fig1.gif" alt="hatch example 1"></td>
<td align="left" valign="top"><small><u>Example 1</u><br>
This example shows simple hatching given by using a curve font "continuous" at <em>HatchLineAppearance</em>.<br>
<br>
The distance of hatch lines is given by a positive length measure. The angle (here 45' if measures in degree) is provided by <em>HatchLineAngle</em>.<br>
<br>
The <em>PatternStart</em> is set to NIL ($) in this example.</small></td>
<td align="left" valign="top" width="280"> <img src="../../../../../../figures/ifcfillareastylehatching_fig2.gif" alt="hatch example 2"></td>
<td align="left" valign="top"><small><u>Example 2</u><br>
This shows hatching from example 1 with using a different curve font at <em>HatchLineAppearance</em>.<br>
<br></small> <small>The distance of hatch lines is given by a positive length
measure, therefore the font pattern start is at a point at the next hatch line
given by a vector being perpendicular to the point of origin at the reference
hatch line.<br>
<br></small> <small>The <em>PatternStart</em> is set to NIL ($) in this
example.</small></td>
</tr>
<tr>
<td width="280"><img src="../../../../../../figures/ifcfillareastylehatching_fig3.gif" alt="hatch example 3"></td>
<td align="left" valign="top"><small><u>Example 3</u><br>
This example uses hatching from example 2 with a vector to determine the pattern start of the next hatch lines.<br>
<br>
The pattern start is the beginning of the first visual curve font pattern segment at <em>IfcCurveFont.CurveFont</em>.<br>
<br></small> <small>The <em>PatternStart</em> is set to NIL ($) in this
example.</small><br></td>
<td width="280"><img src="../../../../../../figures/ifcfillareastylehatching_fig4.gif" alt="hatch example 4"></td>
<td align="left" valign="top"><small><u>Example 4</u><br>
This example uses hatching from example 3 where the pattern start is offset
from the point of origin at the reference hatch line. That is, the first
visible curve font pattern segment now does not start at the point of origin at
the reference hatch line.</small><br>
<small><br></small></td>
</tr>
<tr>
<td><img src="../../../../../../figures/ifcfillareastylehatching_fig5.gif" alt="hatch example 5"></td>
<td align="left" valign="top"><small><u>Example 5</u><br>
This example uses hatching from example 4 where the hatch pattern is shifted
against the underlying coordinate system.<br>
<br>
The point that is mapped to the insertion point of the
<em>IfcAnnotationFillAreaOccurrence</em> now has an X and Y offset from the
start of the reference hatch line. That is, the reference hatch line now does
not go through the insertion point of the hatching.<br>
<br>
<br>
<br></small></td>
<td valign="top"><img src="../../../../../../figures/ifcfillareastylehatching_fig6.gif" alt="fig 6"></td>
<td valign="top"><small><u>Example 6</u><br>
This example shows use of <em>IfcFillAreaStyleHatching</em> attributes for two <em>IfcFillAreaStyleHatching</em>'s within one <em>IfcFillAreaStyle</em>.<br>
<br>
Note that the <em>PatternStart</em> now displaces both the reference hatch line from the point of origin and the start of the curve pattern. This can be used
in cases when more than one <em>IfcFillAreaStyleHatching</em> is used in an <em>IfcFillAreaStyle</em> in order to place rows of hatch lines with an offset
from each other.</small></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td>
<p class="figure">Figure 1 &mdash; Fill area style hatching</p>
</td>
</tr>
</table>

> NOTE&nbsp; Entity adapted from **fill_area_style_hatching** defined in ISO10303-46

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; The _IfcFillAreaStyleHatching_ has been changed by making the attributes _PatternStart_ and _PointOfReferenceHatchLine_ OPTIONAL. The attribute _StartOfNextHatchLine_ has changed to a SELECT with the additional choice of _IfcPositiveLengthMeasure_. Upward compatibility for file based exchange is guaranteed.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attribute data type for _StartOfNextHatchLine_ has been changed to be a select of _IfcPositiveLengthMeasure_ and _IfcVector_.

## Attributes

### HatchLineAppearance
The curve style of the hatching lines. Any curve style pattern shall start at the origin of each hatch line.

### StartOfNextHatchLine
A repetition factor that determines the distance between adjacent hatch lines. The factor can either be defined by a parallel offset, or by a repeat factor provided by _IfcVector_.
  
{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; The attribute type of _StartOfNextHatchLine_ has changed to a SELECT of _IfcPositiveLengthMeasure_ (new) and _IfcOneDirectionRepeatFactor_.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attribute type of _StartOfNextHatchLine_ has changed to a SELECT of _IfcPositiveLengthMeasure_ (new) and _IfcVector_.

### PointOfReferenceHatchLine
A Cartesian point which defines the offset of the reference hatch line from the origin of the (virtual) hatching coordinate system. The origin is used for mapping the fill area style hatching onto an annotation fill area or surface. The reference hatch line would then appear with this offset from the fill style target point.  
If not given the reference hatch lines goes through the origin of the (virtual) hatching coordinate system.
  
{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; The usage of the attribute _PointOfReferenceHatchLine_ has changed to not provide the Cartesian point which is the origin for mapping, but to provide an offset to the origin for the mapping. The attribute has been made OPTIONAL.

### PatternStart
A distance along the reference hatch line which is the start point for the curve style font pattern of the reference hatch line.  
If not given, the start point of the curve style font pattern is at the (virtual) hatching coordinate system.
  
{ .change-ifc2x2}
> IFC2x2 Add2 CHANGE The attribute _PatternStart_ has been made OPTIONAL.

### HatchLineAngle
A plane angle measure determining the direction of the parallel hatching lines.

## Formal Propositions

### PatternStart2D
The _IfcCartesianPoint_, if given as value to _PatternStart_ shall have the dimensionality of 2.

### RefHatchLine2D
The _IfcCartesianPoint_, if given as value to _PointOfReferenceHatchLine_ shall have the dimensionality of 2.
