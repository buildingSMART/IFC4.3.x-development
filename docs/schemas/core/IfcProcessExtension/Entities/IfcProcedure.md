# IfcProcedure

An _IfcProcedure_ is a logical set of actions to be taken in response to an event or to cause an event to occur.

> HISTORY&nbsp; New entity in IFC2x2

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; _ProcedureType_ renamed to _PredefinedType_ and made optional (upward compatible). Where rules WR1 and WR2 have been removed.

{ .use-head}
Use definitions

_IfcProcedure_ is used to capture information about stepped processes such as calibration, start/stop procedures for equipment items, designated actions to take in the event of an emergency etc. A procedure is not a task, but may describe a set of tasks and their order of occurrence in response to or to cause an event.

As shown in Figure 11, _IfcProcedure_ does not restrict anything but describes specific steps of how something should happen. While a procedure does control/restrict in the sense of indicating "this is how the task should be performed" by nature of describing inner detail, this is not different than parts of a product indicating "this is how the parts should be assembled". Consequently, it doesn't restrict the outer item as a whole but provides inner detail of the item.

!["procedure example"](../../../../../../figures/ifcprocedure_example.png "Figure 1 &mdash; Procedure relationships")

## Attributes

### PredefinedType
Identifies the predefined types of a procedure from which 
    the type required may be set.

## WhereRules

### HasName
The Name attribute should be inserted to describe the task name.

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset, or the inherited attribute _ObjectType_ must be asserted when the value of _PredefinedType_ is set to _USERDEFINED_.
