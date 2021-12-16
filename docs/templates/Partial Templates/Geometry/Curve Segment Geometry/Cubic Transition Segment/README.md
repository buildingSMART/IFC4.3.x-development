Cubic Transition Segment
========================

The cubic transition segment is modelled with _IfcPolynomialCurve_ with certain restrictions. The size of the attribute CoefficientsY is restricted to 4. The cubic term is on position 4. In general, the CoefficietsX size would be restricted to 2 and values specified as [0, 1]. This produces the following result:

y = CoefficientsX[3]*x³, where other values in CoefficientsY are 0.

```
concept {
    IfcCurveSegment:ParentCurve -> IfcPolynomialCurve
    IfcPolynomialCurve:CoefficientsX -> IfcReal_0
    IfcPolynomialCurve:CoefficientsY -> IfcReal_1
}
```
