CompositeCurve Profile Definition
=================================

Composite curve profile definitions define the closed two-dimensional curve used for the cross-section by a composite curve, consisting of multiple composite curve segments. Each composite curve segment has a parent curve, being either a polyline or a trimmed curve. Trimmed curves have basis curves of type line, circle or ellipse.

```
concept {
    IfcArbitraryProfileDefWithVoids:ProfileType -> IfcProfileTypeEnum
    IfcArbitraryProfileDefWithVoids:ProfileName -> IfcLabel
    IfcArbitraryProfileDefWithVoids:OuterCurve -> IfcCompositeCurve
    IfcArbitraryProfileDefWithVoids:InnerCurves -> IfcCompositeCurve
    IfcCompositeCurve:Segments -> IfcCompositeCurveSegment
    IfcCompositeCurveSegment:Transition -> IfcTransitionCode
    IfcCompositeCurveSegment:SameSense -> IfcBoolean
    IfcCompositeCurveSegment:ParentCurve -> IfcTrimmedCurve
    IfcTrimmedCurve:BasisCurve -> IfcPolyline
    IfcTrimmedCurve:BasisCurve -> IfcCircle
    IfcTrimmedCurve:BasisCurve -> IfcEllipse
    IfcTrimmedCurve:Trim1 -> IfcCartesianPoint
    IfcTrimmedCurve:Trim1 -> IfcParameterValue
    IfcTrimmedCurve:Trim2 -> IfcCartesianPoint
    IfcTrimmedCurve:Trim2 -> IfcParameterValue
    IfcTrimmedCurve:SenseAgreement -> IfcBoolean
    IfcTrimmedCurve:MasterRepresentation -> IfcTrimmingPreference
    IfcPolyline:Points -> IfcCartesianPoint
    IfcCircle:Position -> IfcAxis2Placement2D
    IfcCircle:Radius -> IfcPositiveLengthMeasure
    IfcEllipse:Position -> IfcAxis2Placement2D
    IfcEllipse:SemiAxis1 -> IfcPositiveLengthMeasure
    IfcEllipse:SemiAxis2 -> IfcPositiveLengthMeasure
}
```
