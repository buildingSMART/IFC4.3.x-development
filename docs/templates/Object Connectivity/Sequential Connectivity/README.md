Sequential Connectivity
=======================

Processes that occur in time use this relationship to indicate the order of occurrence, such as for tasks, procedures, and events.

```
concept {
    IfcProcess:IsPredecessorTo -> IfcRelSequence:RelatingProcess
    IfcProcess:IsSuccessorFrom -> IfcRelSequence:RelatedProcess
    IfcRelSequence:RelatedProcess -> IfcProcess
    IfcRelSequence:RelatingProcess -> IfcProcess
}
```
