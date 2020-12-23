# IfcRationalBSplineSurfaceWithKnots

A rational B-spline surface with knots is a piecewise parametric rational surface described in terms of control points, and associated weight values.

The surface is to be interpreted as follows:

> <big>&sigma;</big>![formula](../../../../../../figures/ifcbsplinesurface-math2.gif)

> NOTE&nbsp; Entity adapted from **rational_b_spline_surface** in ISO 10303-42.

> HISTORY&nbsp; New entity in IFC4.

## Attributes

### WeightsData
The weights associated with the control points in the rational case.

### Weights
Array (two-dimensional) of weight values constructed from the _WeightsData_.

## WhereRules

### CorrespondingWeightsDataLists
The array dimensions for the weights shall be consistent with the control points data.

### WeightValuesGreaterZero
The weight value associated with each control point shall be greater than zero.
