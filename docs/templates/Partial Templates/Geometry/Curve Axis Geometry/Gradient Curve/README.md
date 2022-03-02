Gradient Curve
==============

Curve geometry based on a 2D horizontal projection as an _IfcCompositeCurve_ referencing _IfcCurveSegment_ occurrences. The vertical profile is represented by another independent list of _IfcCurveSegment_ occurrences.

```
concept {
    IfcGradientCurve:BaseCurve -> IfcCompositeCurve
    IfcGradientCurve:Segments -> IfcCurveSegment_1
    IfcCompositeCurve:Segments -> IfcCurveSegment_0
    IfcCurveSegment_0 -> Arc_Segment
    IfcCurveSegment_0 -> Bloss_Transition_Segment
    IfcCurveSegment_0 -> Clothoid_Transition_Segment
    IfcCurveSegment_0 -> Cosine_Spiral_Transition_Segment
    IfcCurveSegment_0 -> Cubic_Transition_Segment
    IfcCurveSegment_0 -> Helmert_Transition_Segment
    IfcCurveSegment_0 -> Linear_Segment
    IfcCurveSegment_0 -> Sine_Spiral_Transition_Segment
    IfcCurveSegment_0 -> Viennese_Bend_Transition_Segment
    IfcCurveSegment_1 -> Arc_Segment
    IfcCurveSegment_1 -> Clothoid_Transition_Segment
    IfcCurveSegment_1 -> Linear_Segment
    IfcCurveSegment_1 -> Parabolic_Transition_Segment
    IfcCompositeCurve:Segments[binding="CompositeSegments"]
    IfcGradientCurve:Segments[binding="VerticalSegments"]
}
```
