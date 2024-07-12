# IfcAlignmentHorizontalSegment

Individual segment along the _IfcAlignmentHorizontal_, being defined in the x/y coordinate space. Each single horizontal alignment segment has an optional associated segment definition. The placement of _IfcAlignmentHorizontalSegment_ and the _IfcCurveSegment_ _StartPlacement_ correspond to each other.
<!-- end of short definition -->

The following information can be calculated (and is therefore not exchanged explicitly to avoid redundancy and inconsistencies)

* the end point (from start point, direction, segment length and curve parameter)
* the start distance along (from the end distance along of the previous segment, or the start distance along of the horizontal alignment (if it is the first segment)
* the end distance along (from the start distance and the segment length)
* the end direction (from the curve parameter, the start direction and the segment length)
* the point of intersection (from the start direction and the end direction)

The following checks can be done to validate the correct exchange:

* continuity – does the calculated end point of the previous segment matches with the provided start point of this segment
* tangential continuity – does the calculated end direction of the previous segment matches with the provided start direction of this segment

## Attributes

### StartPoint
The start point of the segment defined by a Cartesian point.

### StartDirection
The direction of the tangent at the start point. Direction value 0. indicates a curve with a start tangent along the positive x-axis. Values increases counter-clockwise, and decreases clockwise. Depending on the plane angle unit, either degree or radians, the sensible range is -360° ≤ n ≤ 360° (or -2π ≤ n ≤ 2π). Values larger then a full circle (>|360°| or >|2 π| shall not be used.

### StartRadiusOfCurvature
For a NONLINEAR horizontal segment type the radius of the curve at the start point (_Placement_ of the segment). For CIRCULAR type it is constant i.e. _StartRadiusOfCurvature_ and _EndRadiusOfCurvature_ are always the same. For LINE type, both _StartRadiusOfCurvature_ and _EndRadiusOfCurvature_ is 0. If the radius is 0 it shall be interpreted as INFINITE. Positive values imply a CCW direction whereas negative CW.

### EndRadiusOfCurvature
For a NONLINEAR horizontal segment type the radius of the curve at the end point. If the radius is 0 it shall be interpreted as INFINITE. Positive values imply a CCW direction whereas negative CW.

### SegmentLength
The length along the curve.

### GravityCenterLineHeight
Optional attribute require for the exchange of Vienna bend transition segment.

### PredefinedType
Predefined type of the horizontal alignmnent segment.
