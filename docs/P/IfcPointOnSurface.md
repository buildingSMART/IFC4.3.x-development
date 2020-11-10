IfcPointOnSurface
=================
The _IfcPointOnSurface_ is a point defined by two parameter value of its
defining surface.  
  
{ .extDef}  
> NOTE  Definition according to ISO/CD 10303-42:1992  
> A point on surface is a point which lies on a parametric surface. The point
> is determined by evaluating the surface at a particular pair of parameter
> values.  
  
> NOTE  Entity adapted from **point_on_surface** in ISO 10303-42.  
  
> HISTORY  New entity in IFC2x2.  
  
{ .spec-head}  
Informal Propositions:  
  
1\. The parametric values specified for u and v shall not be outside the
parametric range of the basis surface.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometryresource/lexical/ifcpointonsurface.htm)


Attribute definitions
---------------------
| Attribute       | Description                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------------|
| BasisSurface    |                                                                                                      |
| PointParameterU | The first parameter value of the point location.                                                     |
| PointParameterV | The second parameter value of the point location.                                                    |
| Dim             | The space dimensionality of this class, determined by the space dimensionality of the basis surface. |

