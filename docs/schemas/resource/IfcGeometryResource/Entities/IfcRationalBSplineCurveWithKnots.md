# IfcRationalBSplineCurveWithKnots

A rational B-spline curve with knots is a B-spline curve described in terms of control points and basic functions. It describes weights in addition to the control points defined at the supertype _IfcBSplineCurve_.

All weights shall be positive and the curve is given by:

> ![Math](../../../../../../figures/ifcrationalbsplinecurvewithknots-math1.gif)

where

<table>
<tr>
<td width="100" align="right"><em>k</em>+1</td>
<td>number of control points</td>
</tr>
<tr>
<td align="right">P<sub><em>i</em></sub></td>
<td>control points</td>
</tr>
<tr>
<td align="right"><em>w<sub>i</sub></em></td>
<td>weights</td>
</tr>
<tr>
<td align="right"><em>d</em></td>
<td>degree</td>
</tr>
</table>

> NOTE&nbsp; Entity adapted from **rational_b_spline_curve** in ISO 10303-42.

> HISTORY&nbsp; New entity in IFC4.

## Attributes

### WeightsData
The supplied values of the weights.

### Weights
The array of weights associated with the control points. This is derived from the weights data.

## Formal Propositions

### SameNumOfWeightsAndPoints
There shall be the same number of weights as control points.

### WeightsGreaterZero
All the weights shall have values greater than 0.0.
