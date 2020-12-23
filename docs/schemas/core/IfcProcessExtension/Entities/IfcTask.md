# IfcTask

An _IfcTask_ is an identifiable unit of work to be carried out in a construction project.

A task is typically used to describe an activity for the construction or installation of products, but is not limited to these types. For example it might be used to describe design processes, move operations and other design, construction and operation related activities as well.

Quantities of resources consumed by the task are dealt with by defining the _IfcElementQuantity_ for the resource and not at the instance of _IfcTask_.

> HISTORY&nbsp; New entity in IFC1.0. Renamed from _IfcWorkTask_ in IFC2x.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Attributes _TaskTime_ and _PredefinedType_ added. IfcMove and IfcOrderRequest has been removed in IFC4 and are now represented by _IfcTask_. IfcRelAssignsTasks relationship has been removed as well.

{ .use-head}
Attribute use definition

Each occurrence of _IfcTask_ is given a name that is indicative of its content (_IfcRoot.Name_). A textual description of the task may be provided and this may be further elaborated by a narrative long description (_IfcProcess.LongDescription_). A work method may be declared for the method of work used in carrying out a task. A task is identified as being either a milestone task or not. A milestone task is defined by the marker _IsMilestone_. and has no duration. A status and priority for each task may also be set.

{ .use-head}
Time and duration use definition

Compared to previous IFC releases, basic task time information (scheduled start time, scheduled finish time, duration) is now directly attached to _IfcTask_ through the _TaskTime_ attribute. Regular tasks are defined through _IfcTaskTime_. Recurring tasks are defined through _IfcTaskTimeRecurring_. In case a regular task is derived from a recurring task both tasks should be linked together through a _IfcRelNests_ relationship, where _IfcRelNests.IsNestedBy_ points to the recurring task and _IfcRelNests.Nests_ points to all regular tasks that have been derived from the recurring task.

{ .use-head}
Representation of other activities

The use definitions for _IfcTask_ have been generalised to represent other activities as well, including activities that had been defined by own entities in previous IFC releases. This includes

* Order actions
* Move operations

_IfcTask_ represents an order that might be carried out by a Helpdesk acting the role of interface for the organization between the facility user and the functional requirement of fulfilling their needs. The actual task represented by the _IfcTask_ entity is turning a request into an order and initiating the action that will enable the order to be completed. The _IfcProjectOrder_ or one of its subtypes including maintenance work order, is related to the _IfcTask_ using _IfcRelAssignsToControl_.

_IfcTask_ can also be used to describe an activity that moves people, groups within an organization or complete organizations together with their associated furniture and equipment from one place to another. It thus replaces the previous IFC entity IfcMove. The functionality is represented in _IfcTask_ as follows:

* Move from: The place from which actors and their associated equipment are moving.   Use _IfcRelAssignsToProcess_ where _RelatingProcess_ points to the task and _RelatedObjects_ holds the location(s) from which to move.
* Move to: The place to which actors and their associated equipment are moving.   Use _IfcRelAssignsToProduct_ where _RelatedObjects_ points to the task(s) and _RelatingProduct_ points to the location to which to move.
* Punch list: A list of points concerning a move that require attention.   Use _LongDescription_ or else identify sub-tasks to track punch list items individually via _IfcRelNests_.

## Attributes

### Status
Current status of the task.
    
> NOTE&nbsp; Particular values for status are not specified, these should be determined and agreed by local usage. Examples of possible status values include 'Not Yet Started', 'Started', 'Completed'.

### WorkMethod
The method of work used in carrying out a task.
    
> NOTE&nbsp; This attribute should not be used if the work method is specified for the _IfcTaskType_

### IsMilestone
Identifies whether a task is a milestone task (=TRUE) or not
    (= FALSE).
    
> NOTE&nbsp; In small project planning applications, a milestone task may be understood to be a task having no duration. As such, it represents a singular point in time.

### Priority
A value that indicates the relative priority of the task (in
    comparison to the priorities of other tasks).

### TaskTime
Time related information for the task.
    
{ .change-ifc2x4}
> IFC4 CHANGE Attribute added

### PredefinedType
Identifies the predefined types of a task from which 
    the type required may be set.
    
{ .change-ifc2x4}
> IFC4 CHANGE Attribute added

## WhereRules

### HasName
The Name attribute should be inserted to describe the task name.

### CorrectPredefinedType
The attribute ObjectType must be asserted when the value of PredefinedType is set to USERDEFINED.
