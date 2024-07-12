# IfcGradientCurve

Gradient curve is a type of curve 3D curve representation that is based on its 2D projection (BaseCurve) and a height deifned by its gradient segments which can be derived from a function that retrieves it from the segment start height, its placement and the ParentCurve instance and the type of the ParentCurve.
<!-- end of short definition -->

The parametrization of the gradient curve is based on the underlying segments of its _BaseCurve_. The value of the parameter equals the parameter value of _BaseCurve_.

## Attributes

### BaseCurve
Base curve also the 2D projection of gradient curve.

### EndPoint
End point of gradient curve.

### RelativeElevation

