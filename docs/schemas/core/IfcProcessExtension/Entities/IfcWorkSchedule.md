# IfcWorkSchedule

An _IfcWorkSchedule_ represents a task schedule of a work plan, which in turn can contain a set of schedules for different purposes.

> HISTORY&nbsp; New entity in IFC2.0.

{ .use-head}
Declaration Use Definition

_IfcWorkSchedule_ can reference a project (the single _IfcProject_ instance) via _IfcRelDeclares_.

Figure 1 shows the backbone structure of a work schedule that defines (1) a context through _IfcRelDeclares_ (not necessarily the project) and (2) controls tasks (typically the schedule summary task) and resources. Please note that a work calendar shall be assigned to the summary task and not the work schedule.

If an assigned _IfcTask_ is a root-level task, such task must be declared on the _IfcProject_ using the _IfcRelDeclares_ relationship.

!["work schedule instantiation diagram"](../../../../figures/ifcworkschedule_instantiation_diagram.png "Figure 1 &mdash; Work schedule relationships")

## Attributes

### PredefinedType
Identifies the predefined types of a work schedule from which 
    the type required may be set.

## Formal Propositions

### CorrectPredefinedType
The attribute ObjectType must be asserted when the value of the IfcWorkScheduleTypeEnum is set to USERDEFINED.
