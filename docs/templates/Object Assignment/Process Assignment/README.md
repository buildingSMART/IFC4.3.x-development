Process Assignment
==================

Processes may have assignments indicating resources consumed or occupied by the process. An example of such assignment is a carpenter labor resource building a wall.

```
concept {
    IfcProcess:OperatesOn -> IfcRelAssignsToProcess:RelatingProcess
    IfcRelAssignsToProcess:RelatedObjects -> IfcResource:HasAssignments
    IfcRelAssignsToProcess:RelatedObjects[binding="Type"]
}
```
