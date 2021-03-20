# IfcAlignment2DVerSegParabolicArc

The vertical parabolic segment is defined as a parabola using the inherited attributes from _IfcAlignment2DVerticalSegment_ and the following additional curve parameters _ParabolaConstant_ as the minimum radius of the parabolic arc at its apex, and _IsConvex_ to indicate the whether the parabolic arc defined a sag or a crest.

The parabolic arc is described by (see figure 1):

* R = signed _ParabolaConstant_, if _IsConvex_ = true, then -R, if _IsConvex_ = false, then +R as length measure
* s~0~ = _StartDistAlong_ as length measure
* z~0~ = _StartHeight_ as length measure
* g~0~ = _StartGradient_ as ratio measure
*  

The following equations are used for any point along the parabola:

* at any point s~1~ along the _HorizontalLength_ 
* the gradient g~1~ = (s~1~-s~0~) / R + g~0~ 
* the height z~1~ = (s~1~-s~0~) \* (g~1~+g~0~)/2 + z~0~ 

<table>
<tr><td><img src="../../../../figures/ifcalignment2dversegparabolicarc_fig1.png"></td></tr>
<tr><td>
Legend:<br>
red: the parabolic curve with start point and calculated end point used as an vertical alignment</br>
yellow: the underlying unbounded parabola definition<br>
blue: the minimum circle defined by the parabola constant agreeing to the "is convex" fag, the constant, and the start gradient 
</td></tr>
<tr><td><p class="figure">Figure 1 &mdash; Alignment vertical segment parabola convex</p></td></tr>
</table>

&nbsp;

<table>
<tr><td><img src="../../../../figures/ifcalignment2dversegparabolicarc-convex.png"></td><td style="vertical-align: bottom">start point provided by <i>StartDistAlong</i> and <i>StartHeight</i><br>instanteneous gradient provided by <i>StartGradient</i>, <br>and length provided by <i>HorizontalLength</i></td></tr>
<tr><td><p class="figure">Figure 3 &mdash; Alignment vertical parabolic arc segment convex</p></td><td>&nbsp;</td></tr>
</table>

&nbsp;

<table>
<tr><td><img src="../../../../figures/ifcalignment2dversegparabolicarc-concave.png"></td><td style="vertical-align: bottom">start point provided by <i>StartDistAlong</i> and <i>StartHeight</i><br>instanteneous gradient provided by <i>StartGradient</i>, <br>and length provided by <i>HorizontalLength</i></td></tr>
<tr><td><p class="figure">Figure 3 &mdash; Alignment vertical parabolic arc segment concave</p></td><td>&nbsp;</td></tr>
</table>

## Attributes

### ParabolaConstant
Parabola constant (determining the “steepness” of the parabola). The parabola constant is provided by the “minimum parabola radius”, the true radius of a parabola at its vertical axis (the zero-gradient point of the parabola). The minimum radius is twice the focal length of the parabola (the distance between the focal point and the vertex).

### IsConvex
Orientation of the parabolic arc, convex (Boolean=”true”) means decreasing gradient along the arc at the beginning such as at the crest of a hill, concave (Boolean=”false”) means increasing gradient along the arc at the beginning such as at the base of a valley.
