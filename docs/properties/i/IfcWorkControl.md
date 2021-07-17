IfcWorkControl
==============

An _IfcWorkControl_ is an abstract supertype which captures information that is common to both _IfcWorkPlan_ and _IfcWorkSchedule_.

> HISTORY&nbsp; New entity in IFC2x

{ .change-ifc2x4}
> CHANGE IFC4&nbsp; Corrected assignment of resources to work control in documentation. Assignment of tasks to work control updated based on changes of task time definitions and the introduction of a summary task. Identifier has been renamed (now Identification) and promoted to supertype _IfcControl_

A work control may have resources assigned to it. This is handled by the _IfcRelAssignsToControl_ relationship. A work control should also define a context that gives further information about its usage. If no special context information is required then the _IfcProject_ instance as a global context should be used instead. An explicit link between the work control and the _IfcProject_ via _IfcRelDeclares_ should then be provided.

The attribute _IfcWorkControl.Purpose_ is used to define the purpose of either a work schedule or a work plan. In the case of _IfcWorkPlan_, the purpose attribute can be used to determine if the work plan is for cost estimating, task scheduling or some other defined purpose.
