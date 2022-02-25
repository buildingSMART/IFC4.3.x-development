Actor Assignment
================

Actors may have assignments indicating objects for which they have responsibility. An example of such assignment is a work order assigned to an organization.

```
concept {
    IfcActor:IsActingUpon -> IfcRelAssignsToActor:RelatingActor
    IfcRelAssignsToActor:RelatedObjects -> IfcControl:HasAssignments
    IfcRelAssignsToActor:RelatedObjects -> IfcGroup:HasAssignments
    IfcRelAssignsToActor:RelatedObjects -> IfcProduct:HasAssignments
    IfcRelAssignsToActor:RelatedObjects -> IfcProcess:HasAssignments
    IfcRelAssignsToActor:RelatedObjects -> IfcResource:HasAssignments
    IfcRelAssignsToActor:RelatedObjects -> IfcContext:HasAssignments
    IfcRelAssignsToActor:RelatedObjects[binding="Type"]
}
```
