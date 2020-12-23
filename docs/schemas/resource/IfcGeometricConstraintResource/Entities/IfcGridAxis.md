# IfcGridAxis

An individual axis, _IfcGridAxis_, is defined in the context of a design grid. The axis definition is based on a curve of dimensionality 2. The grid axis is positioned within the XY plane of the position coordinate system defined by the _IfcGrid_.

The standard geometric representation of _IfcGridAxis_ is defined using a 2D curve entity. Grid axes are normally defined by an offset to another axis. The _IfcOffsetCurve2D_ supports this concept. Each grid axis has a sense given by the parameterization of the curve. The attribute _SameSense_ is an indicator of whether or not the sense of the grid axis agrees with, or opposes, that of the underlying curve.

<table cellpadding="2" cellspacing="2">
<tr>
<td><img src="../../../../figures/ifcgridaxis-layout1.gif" alt="design grid" border="0" height="300" width="400"></td>
<td style="vertical-align:bottom">
<p class="small">As shown in Figure 1, the grid axis is defined as a 2D curve within
the xy plane of the position coordinate system. Any curve can be
used to define a grid axis, most common is the use of IfcLine for
linear grids and <em>IfcCircle</em> for radial grids.</p>
<p class="small">Most grids are defined by a pair of axis
lists, each defined by a base grid axis and axes given by an
offset to the base axis. The use of <em>IfcOffsetCurve2D</em> as
underlying AxisCurve supports this concept.</p>
</td>
</tr>
<tr><td><p class="figure">Figure 1 &mdash; Grid axis</p></td>
<td>&nbsp;</td>
</tr>
</table>

> HISTORY&nbsp; New entity in IFC1.0

## Attributes

### AxisTag
The tag or name for this grid axis.

### AxisCurve
Underlying curve which provides the geometry for this grid axis.

### SameSense
Defines whether the original sense of curve is used or whether it is reversed in the context of the grid axis.

### PartOfW
If provided, the _IfcGridAxis_ is part of the _WAxes_ of _IfcGrid_.
{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; New inverse attribute.

### PartOfV
If provided, the _IfcGridAxis_ is part of the _VAxes_ of _IfcGrid_.
{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; New inverse attribute.

### PartOfU
If provided, the _IfcGridAxis_ is part of the _UAxes_ of _IfcGrid_.
{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; New inverse attribute.

### HasIntersections
The reference to a set of <IfcVirtualGridIntersection's, that connect other grid axes to this grid axis.
{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; New inverse attribute.

## WhereRules

### WR1
The dimensionality of the grid axis is 2.

### WR2
The _IfcGridAxis_ needs to be used by exactly one of the three attributes of _IfcGrid_:
* _UAxes_
* _VAxes_
* _WAxes_


i.e. it can only refer to a single instance of _IfcGrid_ in one of the three list of axes.
