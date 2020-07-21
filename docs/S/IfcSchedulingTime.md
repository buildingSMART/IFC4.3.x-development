IfcSchedulingTime
=================
_IfcSchedulingTime_ is the abstract supertype of entities that capture time-
related information of processes.  
  
> HISTORY  New entity in IFC4.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcdatetimeresource/lexical/ifcschedulingtime.htm)


Attribute definitions
---------------------
| Attribute             | Description                                                                                                                                           |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name                  | Optional name for the time definition.                                                                                                                |
| DataOrigin            | Specifies the origin of the scheduling time entity. It currently\X\0D differentiates between predicted, simulated, measured, and user defined values. |
| UserDefinedDataOrigin | Value of the data origin if DataOrigin attribute is USERDEFINED.                                                                                      |

