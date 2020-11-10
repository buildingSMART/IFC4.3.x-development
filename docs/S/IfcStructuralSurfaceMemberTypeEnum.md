IfcStructuralSurfaceMemberTypeEnum
==================================
This enumeration distinguishes between different types of structural surface
members, such as the typical mechanical function of walls, slabs and shells.  
  
> HISTORY  New enumeration in IFC2x2.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Renamed from _IfcStructuralSurfaceTypeEnum_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralanalysisdomain/lexical/ifcstructuralsurfacemembertypeenum.htm)


Attribute definitions
---------------------
| Attribute        | Description                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------|
| BENDING_ELEMENT  | A member with capacity to carry out-of-plane loads, i.e. a plate.                                                            |
| SHELL            | A member with capacity to carry in-plane and out-of-plane loads, i.e. a combination of bending element and membrane element. |
| MEMBRANE_ELEMENT | A member with capacity to carry in-plane loads, for example a shear wall.                                                    |

