Sequential Connectivity
=======================

Processes that occur in time use this relationship to indicate the order of occurrence, such as for tasks, procedures, and events.

```
concept {
    IfcProcess_0:IsPredecessorTo -> IfcRelSequence_0:RelatingProcess
    IfcRelSequence_0:RelatedProcess -> IfcProcess_1:IsSuccessorFrom
}
```
