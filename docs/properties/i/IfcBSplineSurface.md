IfcBSplineSurface
=================

The _IfcBSplineSurface_ is a general form of rational or polynomial parametric surface.

{ .extDef}
> NOTE&nbsp; Definition according to ISO/CD 10303-42:1992  
> A b_spline_surface is a general form of rational or polynomial parametric surface which is represented by control points, basis functions, and possibly, weights. As with the corresponding curve entity it has some special subtypes where some of the data can be derived. <ol style="list-style-type:lower-roman; font-size:inherit;">
<li style=" font-size:inherit;">The symbology used here is:
<table border="0" cellpadding="2" cellspacing="0" summary="symbology" style=" font-size:inherit;">
<tr style=" font-size:inherit;">
<td align="right" width="100" style=" font-size:inherit;"><em>K</em>1</td>
<td align="left" style=" font-size:inherit;">= upper_index_on_u_control_points</td>
</tr>
<tr style=" font-size:inherit;">
<td align="right" width="100" style=" font-size:inherit;"><em>K</em>2</td>
<td align="left" style=" font-size:inherit;">= upper_index_on_v_control_points</td>
</tr>
<tr style=" font-size:inherit;">
<td align="right" width="100" style=" font-size:inherit;"><b>P</b><sub>ij</sub></td>
<td align="left" style=" font-size:inherit;">= control_points</td>
</tr>
<tr style=" font-size:inherit;">
<td align="right" width="100" style=" font-size:inherit;">w<sub>ij</sub></td>
<td align="left" style=" font-size:inherit;">= weights</td>
</tr>
<tr style=" font-size:inherit;">
<td align="right" width="100" style=" font-size:inherit;"><em>d</em>1</td>
<td align="left" style=" font-size:inherit;">= u_degree</td>
</tr>
<tr style=" font-size:inherit;">
<td align="right" width="100" style=" font-size:inherit;"><em>d</em>2</td>
<td align="left" style=" font-size:inherit;">= v_degree</td>
</tr>
</table>
<br></li>
<li style=" font-size:inherit;">The control points are ordered as
<blockquote style=" font-size:inherit;">P<sub>00</sub>, P<sub>01</sub>, P<sub>02</sub>, ......,
P<sub><em>K</em>1(<em>K</em>2-1)</sub>, P<sub><em>K</em>1<em>K</em>2</sub></blockquote>
The weights, in the case of the rational subtype, are ordered similarly.<br>
<br></li>
<li style=" font-size:inherit;">For each parameter, <em>s</em> = <em>u</em> or <em>v</em>, if <em>k</em> is the upper
index on the control points and <em>d</em> is the degree for <em>s</em>, the knot array is an array of (<em>k</em> +
<em>d</em> + 2) real numbers [s<sub>-d</sub>, ...., s<sub><em>k</em>+1</sub>], such that for all indices j in
[-<em>d</em>, <em>k</em>]; <em>s</em><sub><em>j</em></sub> &le; <em>s</em><sub><em>j</em>+1</sub>. This array is
obtained from the appropriate u_knots or v_knots list by repeating each multiple knot according to the
multiplicity.<br>
<br>
N<sub><em>i</em></sub><sup><em>d</em></sup>, the <em>i</em>th normalised B-spline basis function of degree <em>d</em>,
is defined on the subset [<em>s</em><sub>i-<em>d</em></sub>, ...., <em>s</em><sub><em>i</em>+1</sub>] of this
array.<br>
<br></li>
<li style=" font-size:inherit;">Let <em>L</em> denote the number of distinct values amongst the knots in the knot list;
<em>L</em> will be referred to as the &lsquo;upper index on knots&rsquo;. Let <em>m</em><sub><em>j</em></sub> denote
the multiplicity (i.e., number of repetitions) of the <em>j</em>th distinct knot value. Then:
<blockquote><img src="../../../../../../figures/ifcbsplinecurve-math2.gif" alt="formula" border="0"></blockquote>
All knot multiplicities except the first and the last shall be in the range 1, ...., <em>d</em>; the first and last may
have a maximum value of <em>d</em>+1. In evaluating the basis functions, a knot <em>u</em> of, e.g., multiplicity 3 is
interpreted as a sequence <em>u</em>, <em>u</em>, <em>u</em>, in the knot array.<br>
<br></li>
<li style=" font-size:inherit;">The surface form is used to identify specific quadric surface types (which shall have
degree two), ruled surfaces and surfaces of revolution. As with the b-spline curve, the surface form is informational
only and the spline data takes precedence.<br>
<br></li>
<li style=" font-size:inherit;">The surface is to be interpreted as follows: In the polynomial case the surface is
given by the equation:
<blockquote><img src="../../../../../../figures/ifcbsplinesurface-math1.gif" alt="formula" border=""></blockquote>
In the rational case the surface equation is:
<blockquote><img src="../../../../../../figures/ifcbsplinesurface-math2.gif" alt="formula" border=""></blockquote>
</li>
</ol>

> NOTE&nbsp; Entity adapted from **b_spline_surface** defined in ISO10303-42.

> HISTORY&nbsp; New entity in IFC4.
