IfcBSplineSurface
=================
The _IfcBSplineSurface_ is a general form of rational or polynomial parametric
surface.  
  
{ .extDef}  
> NOTE  Definition according to ISO/CD 10303-42:1992  
> A b_spline_surface is a general form of rational or polynomial parametric
> surface which is represented by control points, basis functions, and
> possibly, weights. As with the corresponding curve entity it has some
> special subtypes where some of the data can be derived.

  

  1. The symbology used here is:  
  
  
 _K_ 1  
| = upper_index_on_u_control_points  
  
---|---  
  
  
 _K_ 2  
| = upper_index_on_v_control_points  
  
  
  
 **P** ij  
| = control_points  
  
  
  
wij  
| = weights  
  
  
  
 _d_ 1  
| = u_degree  
  
  
  
 _d_ 2  
| = v_degree  
  
  
  
  

  

  2. The control points are ordered as  

> P00, P01, P02, ......,  
> P _K_ 1( _K_ 2-1), P _K_ 1 _K_ 2

  
The weights, in the case of the rational subtype, are ordered similarly.  
  
  

  

  3. For each parameter, _s_ = _u_ or _v_ , if _k_ is the upper  
index on the control points and _d_ is the degree for _s_ , the knot array is
an array of ( _k_ +  
 _d_ \+ 2) real numbers [s-d, ...., s _k_ +1], such that for all indices j in  
[- _d_ , _k_ ]; _s_ _j_ ≤ _s_ _j_ +1. This array is  
obtained from the appropriate u_knots or v_knots list by repeating each
multiple knot according to the  
multiplicity.  
  
  
  
N _i_ _d_ , the _i_ th normalised B-spline basis function of degree _d_ ,  
is defined on the subset [ _s_ i- _d_ , ...., _s_ _i_ +1] of this  
array.  
  
  

  

  4. Let _L_ denote the number of distinct values amongst the knots in the knot list;  
 _L_ will be referred to as the 'upper index on knots'. Let _m_ _j_ denote  
the multiplicity (i.e., number of repetitions) of the _j_ th distinct knot
value. Then:  

> ![formula](figures/ifcbsplinecurve-math2.gif)

  
All knot multiplicities except the first and the last shall be in the range 1,
...., _d_ ; the first and last may  
have a maximum value of _d_ +1. In evaluating the basis functions, a knot _u_
of, e.g., multiplicity 3 is  
interpreted as a sequence _u_ , _u_ , _u_ , in the knot array.  
  
  

  

  5. The surface form is used to identify specific quadric surface types (which shall have  
degree two), ruled surfaces and surfaces of revolution. As with the b-spline
curve, the surface form is informational  
only and the spline data takes precedence.  
  
  

  

  6. The surface is to be interpreted as follows: In the polynomial case the surface is  
given by the equation:  

> ![formula](figures/ifcbsplinesurface-math1.gif)

  
In the rational case the surface equation is:  

> ![formula](figures/ifcbsplinesurface-math2.gif)

  

  

  
  
> NOTE  Entity adapted from **b_spline_surface** defined in ISO10303-42.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometryresource/lexical/ifcbsplinesurface.htm)


