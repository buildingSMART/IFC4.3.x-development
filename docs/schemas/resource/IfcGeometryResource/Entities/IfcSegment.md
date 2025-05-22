# IfcSegment

Definition of a curve segment with a trimming mechanism built in with a StartPlacement (first point) and SegmentLength (second point).
<!-- end of short definition -->

## Attributes

### Transition
The state of transition (i.e., geometric continuity from the last point of this segment to the first point of the next segment) in a composite curve. Connectivity between the continuous segments is not enforced per se to be tangential. Setting "TangentialContinuity" to True means that the current segment shall continue with tangential continuity to the previous one.

### UsingCurves
The set of composite curves which use this composite curve segment as a segment. This set shall not be empty.

### Dim
The space dimensionality of this abstract class, handled by a function specific for concrete subtypes which returns the dimensionality of the ParentCurve attribute (defined on both subtypes).
