Process Type Assignment
=======================

Process types may have assignments indicating re-usable resource types for which occurrences may be consumed or occupied by occurrences of the process type. An example of such assignment is a concrete mixer resource type for delivering concrete.

```
concept {
    IfcTypeProcess:OperatesOn -> IfcRelAssignsToProcess:RelatingProcess
    IfcRelAssignsToProcess:RelatedObjects -> IfcTypeResource
}
```
