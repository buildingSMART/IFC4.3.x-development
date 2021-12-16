Alignment Geometry Cant
=======================



```
concept {
    IfcAlignment:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcSegmentedReferenceCurve
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Axis"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=Curve3D"]
    IfcSegmentedReferenceCurve:BaseCurve -> IfcGradientCurve
    IfcSegmentedReferenceCurve:Segments -> IfcCurveSegment
    IfcGradientCurve -> Gradient_Curve
    IfcCurveSegment -> Arc_Segment
    IfcCurveSegment -> Bloss_Transition_Segment
    IfcCurveSegment -> Clothoid_Transition_Segment
    IfcCurveSegment -> Cosine_Transition_Segment
    IfcCurveSegment -> Helmert_Transition_Segment
    IfcCurveSegment -> Linear_Segment
    IfcCurveSegment -> Sine_Transition_Segment
    IfcCurveSegment -> Viennese_Bend_Transition_Segment
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
}
```
