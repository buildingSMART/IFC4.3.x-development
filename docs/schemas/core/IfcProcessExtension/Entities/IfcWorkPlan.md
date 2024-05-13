# IfcWorkPlan

An _IfcWorkPlan_ represents work plans in a construction or a facilities management project.<!-- end of definition -->

> HISTORY  New entity in IFC2.0

A work plan contains a set of work schedules for different purposes (including construction and facilities management). Contained work schedules are defined through the _IfcRelAggregates_ relationship. Through inheritance from _IfcWorkControl_ it is also possible to define references to activities (for example, _IfcTask_) and resources used in the work plan.

A work plan has information such as start date, finish date, total free float, and so on. _IfcWorkPlan_ can also refer to the construction project represented by the single _IfcProject_ instance (please also check the definition of _IfcWorkControl_).

Figure PROJECTDECLARATION shows the backbone structure of a work plan that defines (1) contained work schedules through _IfcRelAggregates_ and (2), if not assigned otherwise to contained work schedules, assigned tasks and resources through _IfcRelAssignsToControl_.

If an assigned _IfcTask_ is a root-level task, such task must be declared on the _IfcProject_ using the _IfcRelDeclares_ relationship.

```
digraph dot_neato {
	IfcProject[pos="0,0!"];
	IfcRelDeclares[pos="0,-70!"];
        IfcWorkPlan[pos="0,-140!"];
        IfcRelAggregates[pos="-100,-210!"];
        IfcRelAssignsToControl[pos="100,-210!"];
	IfcWorkSchedule[pos="-100,-280!"];
	IfcTask[pos="100,-280!"];

	IfcProject -> IfcRelDeclares [label="RelatingContext"];
        IfcWorkPlan -> IfcRelAggregates [label="RelatingObject"]
        IfcWorkPlan -> IfcRelAssignsToControl [label="RelatingControl"]
        IfcRelDeclares -> IfcWorkPlan [label="RelatedDefinitions"]
	IfcRelAggregates -> IfcWorkSchedule [label="RelatedObjects"]
	IfcRelAssignsToControl -> IfcTask [label="RelatedObjects"]
}
```

Figure 1 — How projects can declare work plans, which in turn contain tasks or schedules

## Attributes

### PredefinedType
Identifies the predefined types of a work plan from which
    the type required may be set.

## Formal Propositions

### CorrectPredefinedType
The attribute ObjectType must be asserted when the value of the IfcWorkPlanTypeEnum is set to USERDEFINED.

## Concepts

### Property Sets for Objects



