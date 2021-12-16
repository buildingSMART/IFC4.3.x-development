Cosine Transition Segment
=========================

The cosine transition segment is a special case of a spiral where the curvature rate of change is a cosine function and the terms are dependent on the length L measured from the inflection point. The parameter value is defined as the deflection i.e. bearing angle &Theta.

The values of its individual terms dependent on segment length L:
CosineTerm = L
Constant = 1

```
concept {
    IfcCurveSegment:ParentCurve -> IfcCosine
    IfcCurveSegment:SegmentStart -> IfcParameterValue_0
    IfcCurveSegment:SegmentLength -> IfcParameterValue_1
    IfcCosine:CosineTerm -> IfcLengthMeasure
    IfcCosine:ConstantTerm -> IfcReal
}
```
