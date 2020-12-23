# IfcAlignment2DVerSegCircularArc

The vertical circular arc segment is defined as an arc using the inherited attributes from _IfcAlignment2DVerticalSegment_ and the following additional curve parameters _Radius_ as the radius of the circular arc, and _IsConvex_ to indicate the whether the circular arc defines a sag (i.e. concave, increasing gradiant) or a crest (i.e. convex, decreasing gradiant).

The circular arc is described by:

* x = offset as length measure relative to start of curve segment (i.e. 0 is at head).
* g~1~ = _StartGradient_ as ratio measure
*  
* R = _Radius_ as length measure

For crest curves (where _IsConvex_ is True), the elevation of a point along the curve (relative to _StartHeight_) is defined as:

![Image](../../../../figures/ifcalignment2dversegcirculararc-formula-concave.png)<table>
<tr><td><img src="../../../../figures/ifcalignment2dversegcirculararc-convex.png"></td><td style="vertical-align: bottom">start point provided by <i>StartDistAlong</i> and <i>StartHeight</i><br>instanteneous gradient provided by <i>StartGradient</i>, <br>and length provided by <i>HorizontalLength</i></td></tr>
<tr><td><p class="figure">Figure 1 &mdash; Alignment vertical arc segment convex</p></td><td>&nbsp;</td></tr>
</table>

&nbsp;

For sag curves (where _IsConvex_ is False), the elevation of a point along the curve (relative to _StartHeight_) is defined as:

![Image](../../../../figures/ifcalignment2dversegcirculararc-formula-convex.png)<table>
<tr><td><img src="../../../../figures/ifcalignment2dversegcirculararc-concave.png"></td><td style="vertical-align: bottom">start point provided by <i>StartDistAlong</i> and <i>StartHeight</i><br>instanteneous gradient provided by <i>StartGradient</i>, <br>and length provided by <i>HorizontalLength</i></td></tr>
<tr><td><p class="figure">Figure 2 &mdash; Alignment vertical arc segment concave</p></td><td>&nbsp;</td></tr>
</table>

## Attributes

### Radius
radius of the circular arc

### IsConvex
Orientation of the circular arc, convex (Boolean=”true”) means decreasing gradient along the arc at the beginning such as at the crest of a hill, concave (Boolean=”false”) means increasing gradient along the arc at the beginning such as at the base of a valley.
