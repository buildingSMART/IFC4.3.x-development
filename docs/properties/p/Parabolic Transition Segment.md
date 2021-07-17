Parabolic Transition Segment
============================

The parabolic transition segment is modelled with _IfcPolynomialCurve_ with certain restrictions. The size of the attribute CoefficientsY is restricted to 3. The quadratic term is on position 3. In general, the CoefficietsX size would be restricted to 2 and values specified as [0, 1]. This produces the following result:

y = CoefficientsX[3]*x², where other values in CoefficientsY are 0.
