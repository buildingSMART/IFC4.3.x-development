IfcAlignmentVerticalSegment
===========================

Individual segment along the _IfcAlignmentVertical_, being defined in the distance-along/z coordinate space.

The vertical alignment is defined by segments that connects end-to-start. The vertical alignment curve geometry is defined in a plane with x = distance along horizontal, the y = height (or elevation). The transition at the segment connection is not enforced to be tangential, The _IfcSegment_ _Transition_ enumeration specifies the type of transition explicitly.

The following vertical segment types are defined:

* line segment - _IfcAlignmentVerticalSegmentTypeEnum_ .LINE.
* circular arc segment - _IfcAlignmentVerticalSegmentTypeEnum_ .ARC.
* parabolic arc segment - _IfcAlignmentVerticalSegmentTypeEnum_ .PARABOLICARC. which can describe symmetric and unsymmetric parabolas
* transition segment with linear curvature variation - _IfcAlignmentVerticalSegmentTypeEnum_ .CLOTHOID.

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

> NOTE&nbsp; Specific subtypes of the <span class="self-ref">IfcAlignmentVerticalSegment</span> add specific geometric curve parameters. Connectivity between vertical segments is not necessarily tangential, but this can be enforced as a requirement through the attribute _TangentialContinuity_.

!["Alignment vertical segment"](../../../../../../figures/ifcalignment2dverticalsegment.png "Figure 1 &mdash; Alignment vertical segment")
