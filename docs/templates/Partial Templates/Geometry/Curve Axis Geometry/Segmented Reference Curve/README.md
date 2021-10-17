Segmented Reference Curve
=========================



```
concept {
    IfcBoundedCurve:Segments -> IfcCurveSegment
    IfcBoundedCurve:EndPoint -> IfcPlacement
    IfcCurveSegment:Transition -> IfcTransitionCode
    IfcCurveSegment:Placement -> IfcPlacement
    IfcCurveSegment:SegmentStart -> IfcCurveMeasureSelect
    IfcCurveSegment:SegmentLength -> IfcCurveMeasureSelect
    IfcCurveSegment:ParentCurve -> IfcCurve
}
```
