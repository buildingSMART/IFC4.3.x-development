# IfcCurveSegment

A type of segment positioned along a curve cutting a segment from the parent curve. If the segment is placed through IfcAxis2PlacementLinear, the positioning curve (Placement.Location.BasisCurve) does not necessarily correspond with the ParentCurve.

{ .spec-head}
Informal Propositions:

1. _SegmentStart_ and _SegmentLength_ are of the same type (i.e., both IfcNonNegativeLengthMeasure or both IfcParameterValue)


## Attributes

### Placement
Placement in the context of the curve using this segment. As insertion point _SegmentStart_ is the reference point of _Placement_. _RefDirection_ of _Placement_ also specifies the sense of the trimmed segment of _ParentCurve_. RefDirection is bound to the paramettrization sense of the segment.

### SegmentStart
First trimming point of the curve segment on the _ParentCurve_. This point is used as the insertion point into the segmented, gradient or composite curve using this segment.

### SegmentLength
Length of segment measured as length or parameter value from _SegmentStart_. The sign of this value defines the sense agreement.
> NOTE When the curve is a cricle, the IfcParameterValue is a value between 0 and 2π.

### ParentCurve
Curve to be used as base for the segment definition.
