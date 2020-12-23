# IfcAlignment2DSegment

An abstract entity defining common information about horizontal and vertical alignment segments.

> NOTE&nbsp; The start and end tag are defined as annotations, not as referents along the alignment. Only absolute distance expressions are in scope, not distances ahead or behind a referent, such as a station. However such information can be exchanged as tags.

## Attributes

### TangentialContinuity
Connectivity between the continuous segments is not enforced per se to be tangential. Setting "TangentialContinuity" to True means that the current segment shall continue with tangential continuity to the previous one.

### StartTag
Tag to annotate the start point of the alignment segment.

### EndTag
Tag to annotate the end point of the alignment segment.
