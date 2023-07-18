Alignment Geometry - Segments
=============================

This concept template applies to segments of all type of alignment layout: _IfcAlignmentHorizontalSegment_, _IfcAlignmentVerticalSegment_ and _IfcAlignmentCantSegment_.

* _RepresentationIdentifier_ = 'Axis'
* _RepresentationType_ = 'Segment'

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
    constraint_2[label="=Axis"]
    IfcLabel_3 -> constraint_3
    constraint_3[label="=Segment"]
}
```