IfcEvent
========
An _IfcEvent_ is something that happens that triggers an action or response.  
  
> HISTORY  New entity in IFC4  
  
{ .use-head}  
Use definitions  
  
_IfcEvent_ is used to capture information about particular things that happen
or that may happen. Particularly used in work plans (or process maps) they
identify e.g. a point at which a message containing information may be issued
or at which a rule or constraint is invoked.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcprocessextension/lexical/ifcevent.htm)


Attribute definitions
---------------------
| Attribute                   | Description                                                                                                                                       |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| EventOccurenceTime          |                                                                                                                                                   |
| PredefinedType              |                                                                                                                                                   |
| EventTriggerType            | Identifies the predefined types of event trigger from which \X\0D the type required may be set.                                                   |
| UserDefinedEventTriggerType | A user defined event trigger type, the value of which is \X\0D asserted when the value of an event trigger type is declared \X\0D as USERDEFINED. |

