Alignment Geometry - Horizontal and Vertical
============================================

This concept template applies to alignments defined by an horizontal and a vertical layouts.

For the _IfcCompositeCurve_:
* _RepresentationIdentifier_ = 'FootPrint'
* _RepresentationType_ = 'Curve2D'

For the _IfcGradientCurve_:
* _RepresentationIdentifier_ = 'Axis'
* _RepresentationType_ = 'Curve3D'

When defining the list of segments for the business logic (i.e., _IfcAlignmentHorizontalSegment_, _IfcAlignmentVerticalSegment_, _IfcAlignmentCantSegment_):

1. A **zero-length segment** shall be added, at the end of the list of segments for _IfcAlignmentSegment.DesignParameters_.
2. If the geometry definition is also present, then each of the zero-length segments shall have a _IfcCurveSegment_ counterpart - of length zero.

```
concept {
    IfcAlignment:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation_0
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation_1
    IfcShapeRepresentation_0:RepresentationIdentifier -> IfcLabel_2
    IfcShapeRepresentation_0:RepresentationType -> IfcLabel_3
    IfcShapeRepresentation_0:Items -> IfcCompositeCurve
    IfcLabel_2 -> constraint_2
    constraint_2[label="='FootPrint'"]
    IfcLabel_3 -> constraint_3
    constraint_3[label="='Curve2D'"]
    IfcCompositeCurve:Segments -> IfcCurveSegment_0
    IfcShapeRepresentation_0:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation_0:RepresentationType[binding="Type"]
    IfcShapeRepresentation_1:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation_1:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation_1:Items -> IfcGradientCurve
    IfcLabel_0 -> constraint_0
    constraint_0[label="='Axis'"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="='Curve3D'"]
    IfcGradientCurve:BaseCurve -> IfcCompositeCurve
    IfcGradientCurve:Segments -> IfcCurveSegment_1
    IfcShapeRepresentation_1:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation_1:RepresentationType[binding="Type"]
}
```