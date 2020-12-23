# IfcEvent

An _IfcEvent_ is something that happens that triggers an action or response.

> HISTORY&nbsp; New entity in IFC4

{ .use-head}
Use definitions

_IfcEvent_ is used to capture information about particular things that happen or that may happen. Particularly used in work plans (or process maps) they identify e.g. a point at which a message containing information may be issued or at which a rule or constraint is invoked.

## Attributes

### PredefinedType
Identifies the predefined types of an event from which 
    the type required may be set.

### EventTriggerType
Identifies the predefined types of event trigger from which 
    the type required may be set.

### UserDefinedEventTriggerType
A user defined event trigger type, the value of which is 
    asserted when the value of an event trigger type is declared 
    as USERDEFINED.

### EventOccurenceTime
The date and/or time at which an event occurs.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset, or the inherited attribute _ObjectType_ must be asserted when the value of _PredefinedType_ is set to _USERDEFINED_.

### CorrectTypeAssigned
Either the _EventTriggerType_ attribute is unset, or the attribute _UserDefinedEventTriggerType_ must be asserted when the value of _EventTriggerType_ is set to _USERDEFINED_.
