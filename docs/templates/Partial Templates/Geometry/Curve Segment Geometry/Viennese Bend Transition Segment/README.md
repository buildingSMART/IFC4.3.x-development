Viennese Bend Transition Segment
================================

The Viennese Bend (R) transition segment is a kinematic high performance transition. The horizontal curvature is assembled by the baseformula and a term depending on the height of the gravity center line relative to the track plane and by the applied cant values at the start and the end of the segment.

 The x/y coordinates can be calculated using a 7th order polynominal spiral.

```
concept {
    IfcCurveSegment:ParentCurve -> IfcSeventhOrderPolynomialSpiral
    IfcCurveSegment:SegmentStart -> IfcParameterValue_0
    IfcCurveSegment:SegmentLength -> IfcParameterValue_1
    IfcSeventhOrderPolynomialSpiral:ConstantTerm -> IfcReal
    IfcSeventhOrderPolynomialSpiral:QuadraticTerm -> IfcLengthMeasure_0
    IfcSeventhOrderPolynomialSpiral:CubicTerm -> IfcLengthMeasure_1
    IfcSeventhOrderPolynomialSpiral:QuarticTerm -> IfcLengthMeasure_2
    IfcSeventhOrderPolynomialSpiral:QuinticTerm -> IfcLengthMeasure_3
    IfcSeventhOrderPolynomialSpiral:SexticTerm -> IfcLengthMeasure_4
    IfcSeventhOrderPolynomialSpiral:SepticTerm -> IfcLengthMeasure_5
}
```
