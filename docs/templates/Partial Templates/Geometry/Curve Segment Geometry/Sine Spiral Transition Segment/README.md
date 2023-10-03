Sine Spiral Transition Segment
==============================

The sine spiral transition segment is a special case of a spiral where the curvature rate of change is a sine function and the terms are dependent on the length L measured from the inflection point. The parameter value is defined as the deflection i.e. bearing angle &Theta.

The values of its individual terms are identical and equal to the length of the segment L:
SineTerm = L
LinearTerm = L

```
concept {
    IfcCurveSegment:ParentCurve -> IfcSineSpiral
    IfcCurveSegment:SegmentStart -> IfcLengthMeasure_0
    IfcCurveSegment:SegmentLength -> IfcLengthMeasure_1
    IfcSineSpiral:SineTerm -> IfcLengthMeasure_0
    IfcSineSpiral:LinearTerm -> IfcLengthMeasure_1
}
```
