IfcFooting
==========
A footing is a part of the foundation of a structure that spreads and
transmits the load to the soil. A footing is also characterized as shallow
foundation, where the loads are transfered to the ground near the surface.  
  
{ .extDef}  
> NOTE  Definition according to ISO 6707-1: stepped construction that spreads
> the load at the foot of a wall or column.  
  
> HISTORY  New entity in IFC2x2.  
  
> NOTE  Slab foundations, also called slab-on-grade, are not instantiated as
> _IfcFooting_ but as _IfcSlab_ or as its subtype _IfcSlabStandardCase_,
> _IfcSlabElementedCase_ with a predefined type of _IfcSlabTypeEnum_.BASESLAB.
> Deep foundations, which transfer the loads to subsurface layers, are
> represented by _IfcDeepFoundation_ and its subtypes _IfcCaissonFoundation_
> and _IfcPile_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralelementsdomain/lexical/ifcfooting.htm)


Formal Propositions
-------------------
| Rule                  | Description   |
|-----------------------|---------------|
| CorrectPredefinedType |               |
| CorrectTypeAssigned   |               |

Associations
------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

