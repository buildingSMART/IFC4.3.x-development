IfcRationalBSplineSurfaceWithKnots
==================================
A rational B-spline surface with knots is a piecewise parametric rational
surface described in terms of control points, and associated weight values.  
  
The surface is to be interpreted as follows:  
  
> σ![formula](../figures/ifcbsplinesurface-math2.gif)  
  
> NOTE  Entity adapted from **rational_b_spline_surface** in ISO 10303-42.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometryresource/lexical/ifcrationalbsplinesurfacewithknots.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                  |
|-------------|------------------------------------------------------------------------------|
| WeightsData | The weights associated with the control points in the rational case.         |
| Weights     | Array (two-dimensional) of weight values constructed from the _WeightsData_. |

Formal Propositions
-------------------
| Rule                          | Description   |
|-------------------------------|---------------|
| CorrespondingWeightsDataLists |               |
| WeightValuesGreaterZero       |               |

