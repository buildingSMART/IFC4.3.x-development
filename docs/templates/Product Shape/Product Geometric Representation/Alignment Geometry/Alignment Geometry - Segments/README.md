Alignment Geometry - Segments
=============================

This concept template applies to segments of all type of alignment layout: _IfcAlignmentHorizontalSegment_, _IfcAlignmentVerticalSegment_ and _IfcAlignmentCantSegment_.

* _RepresentationIdentifier_ = 'Axis'
* _RepresentationType_ = 'Segment'

When defining the list of segments for the business logic (i.e., _IfcAlignmentHorizontalSegment_, _IfcAlignmentVerticalSegment_, _IfcAlignmentCantSegment_):

1. A **zero-length segment** shall be added, at the end of the list of segments for _IfcAlignmentSegment.DesignParameters_.
2. If the geometry definition is also present, then each of the zero-length segments shall have a _IfcCurveSegment_ counterpart - of length zero.

```
concept {
    IfcAlignmentSegment:Representation -> IfcProductDefinitionShape
    IfcAlignmentSegment:DesignParameters -> IfcAlignmentHorizontalSegment
    IfcAlignmentSegment:DesignParameters -> IfcAlignmentVerticalSegment
    IfcAlignmentSegment:DesignParameters -> IfcAlignmentCantSegment
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation_0

    IfcShapeRepresentation_0:RepresentationIdentifier -> IfcLabel_2
    IfcShapeRepresentation_0:RepresentationType -> IfcLabel_3
    IfcShapeRepresentation_0:Items -> IfcCurveSegment
    IfcLabel_2 -> constraint_2
    constraint_2[label="='Axis'"]
    IfcLabel_3 -> constraint_3
    constraint_3[label="='Segment'"]
}
```