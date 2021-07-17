IfcBSplineSurfaceWithKnots
==========================

The _IfcBSplineSurfaceWithKnots_ is a general form of rational or polynomial parametric surface in which the knot values are explicitly given.

{ .extDef}
> NOTE&nbsp; Definition according to ISO/CD 10303-42:1992  
> This is a B-spline surface in which the knot values are explicitly given. This subtype shall be used to represent non-uniform B-spline surfaces, and may also be used for other knot types.  
> All knot multiplicities except the first and the last shall be in the range 1,....,_d_; the first and last may have a maximum value of _d_ + 1. In evaluating the basis functions, a knot _u_ of, e.g., multiplicity 3 is interpreted as a sequence _u_, _u_, _u_, in the knot array.

> NOTE&nbsp; Entity adapted from **b_spline_surface_with_knots** defined in ISO10303-42.

> HISTORY&nbsp; New entity in IFC4.
