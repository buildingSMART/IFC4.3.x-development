IfcSweptAreaSolid
=================
An _IfcSweptAreaSolid_ represents the 3D shape by a sweeping representation
scheme allowing a two dimensional planar cross section to sweep through space.  
  
The swept area is defined by a cross section, represented by a subtype if
_IfcProfileDef_, that is provided as a closed two-dimensional boundary on an
implicit plane. The swept area is defined in the xy plane of the object
coordinate system. The sweeping operation is applied to the swept area as
defined within the subtypes of _IfcSweptAreaSolid_, some subtypes require an
implicit transformation of the swept area to the start position of the sweep.  
  
The optional _Positio_n coordinate system allows for re-positioning the
resulting swept solid relative to the object coordinate system.  
  
{ .extDef}  
> NOTE  Definition according to ISO/CD 10303-42:1992  
> The swept area solid entity collects the entities which are defined
> procedurally by sweeping action on planar bounded surfaces. The position is
> space of the swept solid will be dependent upon the position of the swept
> area. The swept area will be a face of the resulting swept area solid,
> except for the case of a revolved area solid with angle equal to 2π (or 360
> degrees).  
  
> NOTE  Entity adapted from **swept_area_solid** defined in ISO 10303-42.  
  
> HISTORY  New entity in IFC1.5  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The attribute _Position_ has been changed to OPTIONAL with
> upward compatibility for file-based exchange.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcsweptareasolid.htm)


Attribute definitions
---------------------
| Attribute   | Description   |
|-------------|---------------|
| SweptArea   |               |
| Position    |               |

