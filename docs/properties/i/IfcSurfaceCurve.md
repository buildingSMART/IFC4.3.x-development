IfcSurfaceCurve
===============

An _IfcSurfaceCurve_ is a 3-dimensional curve that has additional representations provided by one or two pcurves.

{ .extDef}
> NOTE&nbsp; Definition according to ISO/CD 10303-42:1992  
> A surface curve is a type of curve, that is a curve on a surface. The curve is represented as a curve (curve_3d) in three-dimensional space and possibly as a curve, corresponding to a pcurve, in the two-dimensional parametric space of a surface. The ability of this curve to reference a list of 1 or 2 pcurves enables this entity to define either a curve on a single surface, or an intersection curve which has two distinct surface associations. A `seam' on a closed surface can also be represented by this entity; in this case each associated_geometry will be a pcurve lying on the same surface. Each pcurve shall be parametrised to have the same sense as curve_3d. The surface curve takes its parametrisation directly from either curve_3d or pcurve as indicated by the attribute master representation.

> NOTE&nbsp; Entity adapted from **surface_curve** defined in ISO 10303-42.

> HISTORY&nbsp; New entity in IFC4 Add2.

{ .spec-head}
Informal Propositions:

1. Where _Curve3D_ and one or two pcurves exist they shall represent the same mathematical point set. (i.e., they shall coincide geometrically but may differ in parametrisation.)
2. The _Curve3D_ and any associated pcurves shall agree with respect to their senses.
