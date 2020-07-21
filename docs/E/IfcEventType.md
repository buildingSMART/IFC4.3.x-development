IfcEventType
============
An _IfcEventType_ defines a particular type of event that may be specified.  
  
> HISTORY  New entity in IFC4  
  
An _IfcEventType_ provides for all forms of types of event that may be
specified.  
  
Usage of _IfcEventType_ defines the parameters for one or more occurrences of
_IfcEvent_. Parameters may be specified through property sets that may be
enumerated in the _IfcEventTypeEnum_ data type or through explicit attributes
of _IfcEvent_. Event occurrences (_IfcEvent_ entities) are linked to the event
type through the _IfcRelDefinesByType_ relationship.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcprocessextension/lexical/ifceventtype.htm)


Attribute definitions
---------------------
| Attribute                   | Description                                                                                                                                       |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| EventTriggerType            | Identifies the predefined types of event trigger from which \X\0D the type required may be set.                                                   |
| UserDefinedEventTriggerType | A user defined event trigger type, the value of which \X\0D is asserted when the value of an event trigger type is \X\0D declared as USERDEFINED. |

Formal Propositions
-------------------
| Rule                    | Description   |
|-------------------------|---------------|
| CorrectPredefinedType   |               |
| CorrectEventTriggerType |               |

Associations
------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

