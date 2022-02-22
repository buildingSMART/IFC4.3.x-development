# IfcCurve

An _IfcCurve_ is a curve in two-dimensional or three-dimensional space. It includes definitions for bounded and unbounded curves.

> NOTE  Definition according to ISO 10303-42:
> A curve can be envisioned as the path of a point moving in its coordinate space.

> NOTE Entity adapted from **curve** defined in ISO 10303-42

> HISTORY  New entity in IFC1.0

{ .spec-head}
Informal Propositions:

1. A curve shall be arcwise connected
2. A curve shall have an arc length greater than zero.

## Attributes

### Dim
The space dimensionality of this abstract class, defined differently for all subtypes, i.e. for IfcLine, IfcConic and IfcBoundedCurve.
