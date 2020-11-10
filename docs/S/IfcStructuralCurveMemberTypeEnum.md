IfcStructuralCurveMemberTypeEnum
================================
This enumeration distinguishes between different types of structural ''curve''
members, such as cables.  
  
> HISTORY  New enumeration in IFC2x2.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Renamed from _IfcStructuralCurveTypeEnum_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralanalysisdomain/lexical/ifcstructuralcurvemembertypeenum.htm)


Attribute definitions
---------------------
| Attribute           | Description                                                                                                                                        |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| COMPRESSION_MEMBER  | A member without tensional stiffness.                                                                                                              |
| PIN_JOINED_MEMBER   | A member with capacity to carry axial loads only, i.e. a link. Typically used in trusses.                                                          |
| TENSION_MEMBER      | A member without compressional stiffness.                                                                                                          |
| CABLE               |                                                                                                                                                    |
| RIGID_JOINED_MEMBER | A member with capacity to carry transverse and axial loads, i.e. a beam. Its actual joints may be rigid or pinned. Typically used in rigid frames. |

