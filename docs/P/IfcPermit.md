IfcPermit
=========
A permit is a permission to perform work in places and on artifacts where
regulatory, security or other access restrictions apply.  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Attribute _PermitID_ renamed to _Identification_ and promoted
> to supertype _IfcControl_, attributes _PredefinedType_, _Status_, and
> _LongDescription_ added.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcsharedmgmtelements/lexical/ifcpermit.htm)


Attribute definitions
---------------------
| Attribute       | Description                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| Status          | The status currently assigned to the permit.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE The attribute has been added. |
| LongDescription | Detailed description of the request.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE The attribute has been added.         |

Associations
------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

