IfcControllerTypeEnum
=====================
The _IfcControllerTypeEnum_ defines the range of different types of controller
that can be specified.  
  
> HISTORY  New enumeration in IFC2.0.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  PROPORTIONALINTEGRAL and PROPORTIONALINTEGRALDERIVATIVE values
> deleted (property set enumeration now used). MULTIPOSITION added.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcbuildingcontrolsdomain/lexical/ifccontrollertypeenum.htm)


Attribute definitions
---------------------
| Attribute     | Description                                                                              |
|---------------|------------------------------------------------------------------------------------------|
| FLOATING      | Output increases or decreases at a constant or accelerating rate.                        |
| PROPORTIONAL  | Output is proportional to the control error and optionally time integral and derivative. |
| PROGRAMMABLE  | Output is programmable such as Discrete Digital Control (DDC).                           |
| TWOPOSITION   | Output can be either on or off.                                                          |
| MULTIPOSITION | Output is discrete value, can be one of three or more values.                            |

