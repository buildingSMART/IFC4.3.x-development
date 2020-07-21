IfcRectangularTrimmedSurface
============================
The _IfcRectangularTrimmedSurface_ is a surface created by bounding its
_BasisSurface_ along two pairs of parallel curves defined within the
parametric space of the referenced surface.  
  
{ .extDef}  
> NOTE  Definition according to ISO/CD 10303-42:1992  
> The trimmed surface is a simple bounded surface in which the boundaries are
> the constant parametric lines _u_\X\7E1\X\7E = u1, _u_\X\7E2\X\7E = u2,
> _v_\X\7E1\X\7E = v1 and _v_\X\7E2\X\7E = v2. All these values shall be
> within the parametric range of the referenced surface. Cyclic properties of
> the parameter range are assumed. The rectangular trimmed surface inherits
> its parameterization directly from the basis surface and has parameter
> ranges from 0 to |_u_\X\7E2\X\7E - _u_\X\7E1\X\7E| and 0
> to|_v_\X\7E2\X\7E-_v_\X\7E1\X\7E|.  
  
> NOTE  If the surface is closed in a given parametric direction, the values
> of _u_\X\7E2\X\7E or _v_\X\7E2\X\7E may require to be increased by the
> cyclic range.  
  
> EXAMPLE  370 degrees is equivalent to 10 degrees, for those surfaces whose
> parametric form is defined using circular functions (sine and cosine).  
  
> NOTE  Entity adapted from **rectangular_trimmed_surface** in ISO 10303-42.  
  
> HISTORY  New entity in IFC2x.  
  
{ .spec-head}  
Informal Propositions:  
  
1\. The domain of the trimmed surface shall be within the domain of the
surface being trimmed.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometryresource/lexical/ifcrectangulartrimmedsurface.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                       |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| U1          | First u parametric value.                                                                                                                         |
| V1          | First v parametric value.                                                                                                                         |
| U2          | Second u parametric value.                                                                                                                        |
| V2          | Second v parametric value.                                                                                                                        |
| Usense      | Flag to indicate whether the direction of the first parameter of the trimmed surface agrees with or opposes the sense of u in the basis surface.  |
| Vsense      | Flag to indicate whether the direction of the second parameter of the trimmed surface agrees with or opposes the sense of v in the basis surface. |

Formal Propositions
-------------------
| Rule             | Description   |
|------------------|---------------|
| U1AndU2Different |               |
| V1AndV2Different |               |
| UsenseCompatible |               |
| VsenseCompatible |               |

Associations
------------
| Attribute    | Description   |
|--------------|---------------|
| BasisSurface |               |

