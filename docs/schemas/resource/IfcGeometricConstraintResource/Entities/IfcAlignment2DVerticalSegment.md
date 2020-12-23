# IfcAlignment2DVerticalSegment

Individual segment along the _IfcAlignment2DVertical_, being defined in the distance-along/z coordinate space.

The vertical alignment is defined by segments that connects end-to-start. The vertical alignment curve geometry is defined in a plane with x = distance along horizontal, the y = height (or elevation). The transition at the segment connection is not enforced to be tangential, if the “tangential continuity” flag is set to false, otherwise a tangential continuity shall be preserved.

The following vertical segment types are defined:

* line segment - _IfcAlignment2DVerSegLine_
* circular arc segment - _IfcAlignment2DVerSegCircularArc_
* parabolic arc segment - _IfcAlignment2DVerSegParabolicArc_ which can describe symmetric and unsymmetric parabolas

For each vertical segment, the following non-redundant information is provided:

* the start point (in distance along/ height coordinates)
* the start gradient (as a ratio measure with horizontal being 0, uphill positive, and downhill negative) usually between 1 < n < -1 (equal to a percentage of 100% < n < -100%, or to a degree of 45&deg; < n < -45&deg; but higher values are possible)
* the length (as horizontal length along the distance along (not the curve segment length))
* the curve parameter needed for circular and parabolic arc segments

The following information can be calculated (and is therefore not exchanged explicitly to avoid redundancy and inconsistencies)

* the end distance along (from the distance along and segment length)
* the end height (from start distance along, gradient, length and curve parameter)
* the end direction (from start direction, segment length and curve parameter)
* the point of vertical intersection (from start direction and end direction)

The following checks can be done to validate the correct exchange:

* continuity – does the calculated end distance along of the previous segment matches with the provided start distance along of this segment
* tangential continuity – does the calculated end gradient of the previous segment matches with the provided start gradient of this segment

> NOTE&nbsp; Specific subtypes of the <span class="self-ref">IfcAlignment2DVerticalSegment</span> add specific geometric curve parameters. Connectivity between vertical segments is not necessarily tangential, but this can be enforced as a requirement through the attribute _TangentialContinuity_.

!["Alignment vertical segment"](../../../../figures/ifcalignment2dverticalsegment.png "Figure 1 &mdash; Alignment vertical segment")

## Attributes

### StartDistAlong
Distance along the horizontal alignment, measured along the _IfcAlignment2DHorizontal_ given in the length unit of the global _IfcUnitAssignment_.

### HorizontalLength
Length measured as distance along the horizontal alignment of the segment.

### StartHeight
Elevation in Z of the start point relative to the IfcAlignment coordinate system.
> NOTE&nbsp; It is strongly advised to not offset the IfcAlignment coordinate system from the project engineering coordinate system.

### StartGradient
Gradient of the tangent of the vertical segment at the start point. It is provided as a ratio measure. The ratio is percentage/100 (0.1 is equal to 10%). It has a theoretical range of -∞ < n < ∞ using a ratio measure. The equivalent range measured in degree is -90° < n < 90°.
> NOTE&nbsp; For practical application of start gradient, the range of the ratio measure should be within the limits of -1 ≤ n ≤ 1 (equivalent in degree -45° ≤ n ≤ 45°). However larger limits might apply for particular usages.

Positive gradient means an increasing height at the start (or uphill), a negative gradient means decreasing height at the start (or downhill).

### ToVertical

