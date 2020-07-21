IfcSlabStandardCase
===================
The standard slab, _IfcSlabStandardCase_, defines a slab with certain
constraints for the provision of material usage, parameters and with certain
constraints for the geometric representation. The _IfcSlabStandardCase_
handles all cases of slabs, that:  
  
* have a reference to the _IfcMaterialLayerSetUsage_ defining the material layers of the slab with thicknesses  
* are based on an extrusion of a planar surface as defined by the slab profile  
* have a constant thickness along the extrusion direction  
* are consistent in using the correct material layer set offset to the base planar surface in regard to the shape representation  
* are extruded either perpendicular or slanted to the plane surface  
  
The definitions of slab openings and niches are the same as given at the
supertype _IfcSlab_. The same agreements to the special types of slabs, as
defined in the _PredefinedType_ attribute apply as well.  
  
> NOTE  If the _IfcSlabStandardCase_ is of type Landing and is used within an
> _IfcStair_ or _IfcRamp_, the special agreements to handle stair and ramp
> geometry will also affect the geometric representation of the
> _IfcSlabStandardCase_.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedbldgelements/lexical/ifcslabstandardcase.htm)


Formal Propositions
-------------------
| Rule                     | Description   |
|--------------------------|---------------|
| HasMaterialLayerSetusage |               |

