# IfcSegment

Definition of a curve segment with a trimming mechanism built in with a StartPlacement (first point) and SegmentLength (second point).

## Attributes

### Transition
Connectivity between the continuous segments is not enforced per se to be tangential. Setting "TangentialContinuity" to True means that the current segment shall continue with tangential continuity to the previous one.
