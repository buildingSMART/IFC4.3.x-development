CompositeCurve Profile Definition
=================================

Composite curve profile definitons define the closed two-dimensional curve used for the cross-section by a composite curve, consisting of multiple composite curve segments. Each composite curve segment has a parent curve, being either a polyline or a trimmed curve. Trimmed curves have basis curves of type line, circle or ellipse.

```
concept {
    IfcArbitraryProfileDefWithVoids:ProfileType -> IfcProfileTypeEnum
    IfcArbitraryProfileDefWithVoids:ProfileName -> IfcLabel
    IfcArbitraryProfileDefWithVoids:OuterCurve -> IfcCompositeCurve_0
    IfcArbitraryProfileDefWithVoids:InnerCurves -> IfcCompositeCurve_1
    IfcCompositeCurve_0:Segments -> IfcCompositeCurveSegment
    IfcCompositeCurveSegment:Transition -> IfcTransitionCode
    IfcCompositeCurveSegment:SameSense -> IfcBoolean_0
    IfcCompositeCurveSegment:ParentCurve -> IfcTrimmedCurve
    IfcTrimmedCurve:BasisCurve -> IfcPolyline
    IfcTrimmedCurve:BasisCurve -> IfcCircle
    IfcTrimmedCurve:BasisCurve -> IfcEllipse
    IfcTrimmedCurve:Trim1 -> IfcCartesianPoint_1
    IfcTrimmedCurve:Trim1 -> IfcParameterValue_0
    IfcTrimmedCurve:Trim2 -> IfcCartesianPoint_2
    IfcTrimmedCurve:Trim2 -> IfcParameterValue_1
    IfcTrimmedCurve:SenseAgreement -> IfcBoolean_1
    IfcTrimmedCurve:MasterRepresentation -> IfcTrimmingPreference
    IfcPolyline:Points -> IfcCartesianPoint_0
    IfcCircle:Position -> IfcAxis2Placement2D_0
    IfcCircle:Radius -> IfcPositiveLengthMeasure_0
    IfcEllipse:Position -> IfcAxis2Placement2D_1
    IfcEllipse:SemiAxis1 -> IfcPositiveLengthMeasure_1
    IfcEllipse:SemiAxis2 -> IfcPositiveLengthMeasure_2
}
```
