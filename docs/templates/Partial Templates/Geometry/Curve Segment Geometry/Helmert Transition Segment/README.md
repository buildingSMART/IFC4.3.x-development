Helmert Transition Segment
==========================

The Helmert transition segment is a special case of a fourth order spiral where the curvature rate of change is a quadratic function and the terms are dependent on the length L measured from the inflection point. The parameter value is defined as the deflection i.e. bearing angle &Theta.

The terms for the first half of the segment:
QuadraticTerm = L/√2
rest are 0.

Terms for the second half of the segment:
QuadraticTerm =  -L/√2
LinearTerm = L/4
Constant = -1

SegmentStart is the bearing angle at start and Segment length is the bearing angle at the end of the segment.

```
concept {
    IfcCurveSegment:ParentCurve -> IfcSecondOrderPolynomialSpiral
    IfcCurveSegment:SegmentStart -> IfcParameterValue
    IfcCurveSegment:SegmentLength -> IfcParameterValue
    IfcSecondOrderPolynomialSpiral:QuadraticTerm -> IfcLengthMeasure
    IfcSecondOrderPolynomialSpiral:LinearTerm -> IfcLengthMeasure
    IfcSecondOrderPolynomialSpiral:ConstantTerm -> IfcReal
}
```
