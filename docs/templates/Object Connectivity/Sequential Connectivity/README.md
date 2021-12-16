Sequential Connectivity
=======================

Processes that occur in time use this relationship to indicate the order of occurrence, such as for tasks, procedures, and events.

```
concept {
    IfcProcess_0:IsPredecessorTo -> IfcRelSequence_0:RelatingProcess
    IfcProcess_0:IsSuccessorFrom -> IfcRelSequence_1:RelatedProcess
    IfcRelSequence_0:RelatedProcess -> IfcProcess_1
    IfcRelSequence_1:RelatingProcess -> IfcProcess_3
}
```
