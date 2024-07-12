# IfcEventType

><!-- end of definition --> HISTORY New entity in IFC4

An _IfcEventType_ provides for all forms of types of event that may be specified.

Usage of _IfcEventType_ defines the parameters for one or more occurrences of _IfcEvent_. Parameters may be specified through property sets that may be enumerated in the _IfcEventTypeEnum_ data type or through explicit attributes of _IfcEvent_. Event occurrences (_IfcEvent_ entities) are linked to the event type through the _IfcRelDefinesByType_ relationship.

## Attributes

### PredefinedType
Identifies the predefined types of an event from which the type required may be set.

### EventTriggerType
Identifies the predefined types of event trigger from which the type required may be set.

### UserDefinedEventTriggerType
A user defined event trigger type, the value of which is asserted when the value of an event trigger type is declared as _USERDEFINED_.

## Formal Propositions

### CorrectPredefinedType
The attribute _ProcessType_ must be asserted when the value of _PredefinedType_ is set to _USERDEFINED_.

### CorrectEventTriggerType
The attribute _UserDefinedEventTriggerType_ must be asserted when the value of _EventTriggerType_ is set to _USERDEFINED_.
