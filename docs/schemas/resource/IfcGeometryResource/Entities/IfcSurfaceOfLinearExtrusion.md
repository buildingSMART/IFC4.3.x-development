# IfcSurfaceOfLinearExtrusion

The _IfcSurfaceOfLinearExtrusion_ is a surface derived by sweeping a curve along a vector.

{ .extDef}
> NOTE  Definition according to ISO/CD 10303-42:1992
> This surface is a simple swept surface or a generalized cylinder obtained by sweeping a curve in a given direction. The parameterization is as follows where the curve has a parameterization &lambda;(_u_):
>
> V = ExtrusionAxis
>
> ![Image](../../../../figures/ifcsurfaceoflinearextrusion-math1.gif)
>  The parameterization range for _v_ is -&infin; < _v_ < &infin; and for _u_ it is defined by the curve parameterization.

> NOTE  Entity adapted from **surface_of_linear_extrusion** defined in ISO 10303-42.

> HISTORY  New entity in IFC2x.

{ .spec-head}
Informal Propositions:

1. The surface shall not self-intersect

## Attributes

### ExtrudedDirection
The direction of the extrusion.

### Depth
The depth of the extrusion, it determines the parameterization.

### ExtrusionAxis
The extrusion axis defined as vector.

## Formal Propositions

### DepthGreaterZero

