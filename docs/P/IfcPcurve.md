IfcPcurve
=========
The _IfcPcurve_ is a curve defined within the parameter space of its reference
surface.  
  
{ .extDef}  
> NOTE  Definition according to ISO/CD 10303-42:1992  
> A pcurve is a curve which lies on the basis of a surface and is defined in
> the parameter space of that surface. The basis curve is a curve defined in
> the two-dimensional parametric space of a reference basis surface. Although
> it is defined by a curve in two dimensional space, the variables involved
> are _u_ and _v_, which occur in the parametric representation of the
> referenced surface, rather than the _x_, _y_, Cartesian coordinates. The
> basis curve is only defined within the parametric range of the surface.  
  
> NOTE  Entity adapted from **pcurve** in ISO 10303-42.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometryresource/lexical/ifcpcurve.htm)


Formal Propositions
-------------------
| Rule    | Description   |
|---------|---------------|
| DimIs2D |               |

Associations
------------
| Attribute      | Description   |
|----------------|---------------|
| ReferenceCurve |               |
| BasisSurface   |               |
|                |               |

