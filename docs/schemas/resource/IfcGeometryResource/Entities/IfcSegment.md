# IfcSegment

Definition of a curve segment with a trimming mechanism built in with a StartPlacement (first point) and SegmentLength (second point).
<!-- end of short definition -->

## Attributes

### Transition
The state of transition (i.e., geometric continuity from the last point of this segment to the first point of the next segment) in IfcCompositeCurve and subtypes.
t
### UsingCurves
The set of composite curves which use this composite curve segment as a segment. This set shall not be empty.

### Dim
The space dimensionality of this abstract class, handled by a function specific for concrete subtypes which returns the dimensionality of the ParentCurve attribute (defined on both subtypes).
