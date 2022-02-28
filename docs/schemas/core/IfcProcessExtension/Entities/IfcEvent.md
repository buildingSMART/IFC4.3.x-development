# IfcEvent

An _IfcEvent_ is something that happens that triggers an action or response.

> HISTORY  New entity in IFC4

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

## Concepts

### Control Assignment

An IfcEvent may be assigned to an IfcWorkCalendar to indicate times when such event is active using IfcRelAssignsToControl; otherwise the effective calendar is determined by the nearest IfcProcess ancestor with a calendar assigned.

### Object Nesting

IfcEvent may be contained within an IfcTask using the IfcRelNests relationship. The event is considered active during the time period of the enclosing task (including any assigned IfcWorkCalendar); that is such event may be triggered within the task time period but not outside of it. As an IfcEvent is considered to be atomic, no use is anticipated for nesting processes inside the event.

### Object Typing

The IfcEvent defines the anticipated or actual occurrence of any event; common information about event types is handled by IfcEventType.

### Product Assignment

For building operation scenarios, IfcEvent may be assigned to a product (IfcElement subtype) using IfcRelAssignsToProduct to indicate a specific product occurrence that sources the event.

> EXAMPLE&nbsp; An IfcSensor for a motion sensor may have a "Motion Sensed" event. If the IfcEvent is defined by an IfcEventType and the IfcEventType is assigned to a product type (using IfcRelAssignsToProduct), then the IfcEvent must be assigned to one or more occurrences of the specified product type using IfcRelAssignsToProduct.

### Property Sets for Objects



### Sequential Connectivity

The relationship IfcRelSequence is used to indicate control flow. An IfcEvent as a predecessor (_IfcRelSequence.RelatingProcess_) indicates that the succeeding process (typically IfcProcedure or IfcTask) is triggered in response to the event. An IfcEvent as a successor (_IfcRelSequence.RelatedProcess_) indicates that the completion of the preceeding process causes the event to be triggered. As events have zero duration, the _IfcRelSequence.SequenceType_ attribute has no effect on an IfcEvent but still applies to the opposite end of the relationship if IfcTask is used.

