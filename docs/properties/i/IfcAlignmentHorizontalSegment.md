IfcAlignmentHorizontalSegment
=============================

Individual segment along the _IfcAlignmentHorizontal_, being defined in the x/y coordinate space. Each single horizontal alignment segment has an optional associated segment definition. The placement of _IfcAlignmentHorizontalSegment_ and the _IfcCurveSegment_ _StartPlacement_ correspond to each other.

The following information can be calculated (and is therefore not exchanged explicitly to avoid redundancy and inconsistencies)

* the end point (from start point, direction, segment length and curve parameter)
* the start distance along (from the end distance along of the previous segment, or the start distance along of the horizontal alignment (if it is the first segment)
* the end distance along (from the start distance and the segment length)
* the end direction (from the curve parameter, the start direction and the segment length)
* the point of intersection (from the start direction and the end direction)

The following checks can be done to validate the correct exchange:

* continuity – does the calculated end point of the previous segment matches with the provided start point of this segment
* tangential continuity – does the calculated end direction of the previous segment matches with the provided start direction of this segment
