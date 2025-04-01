Cubic Transition Segment
========================

The cubic transition segment is modelled with _IfcPolynomialCurve_ with certain restrictions. The size of the attribute _CoefficientsY_ is restricted to 4. The cubic term is on position 4. In general, the _CoefficientsX_ size would be restricted to 2 and values specified as [0, 1]. This produces the following result:

y = CoefficientsY[3]*x³, where other values in _CoefficientsY_ are 0.

```
concept {
    IfcCurveSegment:ParentCurve -> IfcPolynomialCurve
    IfcPolynomialCurve:CoefficientsX -> IfcReal_0
    IfcPolynomialCurve:CoefficientsY -> IfcReal_1
}
```
