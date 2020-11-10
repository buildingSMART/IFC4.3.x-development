IfcObjectPlacement
==================
_IfcObjectPlacement_ is an abstract supertype for the special types defining
the object coordinate system. The _IfcObjectPlacement_ has to be provided for
each product that has a shape representation.  
  
The object placement can be given:  
  
* absolute: by an axis2 placement, relative to the world coordinate system,  
* relative: by an axis2 placement, relative to the object placement of another product,  
* by grid reference: by the virtual intersection and reference direction given by two axes of a design grid,  
* linear placement: by distance along a curve, with possible offsets.  
  
In any case the object placement has to unambiguously define the object
coordinate system as either two-dimensional axis placement
(_IfcAxis2Placement2D_) or three-dimensional axis placement
(_IfcAxis2Placement3D_). The axis placement may have to be calculated.  
  
> HISTORY  New entity in IFC2x.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricconstraintresource/lexical/ifcobjectplacement.htm)


Attribute definitions
---------------------
| Attribute      | Description   |
|----------------|---------------|
| PlacementRelTo |               |
| PlacesObject   |               |

