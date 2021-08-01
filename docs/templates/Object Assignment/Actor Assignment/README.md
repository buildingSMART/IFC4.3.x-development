Actor Assignment
================

Actors may have assignments indicating objects for which they have responsibility. An example of such assignment is a work order assigned to an organization.

```
concept {
    IfcActor:IsActingUpon -> IfcRelAssignsToActor:RelatingActor
    IfcRelAssignsToActor:RelatedObjects -> IfcControl
    IfcRelAssignsToActor:RelatedObjects -> IfcGroup
    IfcRelAssignsToActor:RelatedObjects -> IfcProduct
    IfcRelAssignsToActor:RelatedObjects -> IfcProcess
    IfcRelAssignsToActor:RelatedObjects -> IfcResource
    IfcRelAssignsToActor:RelatedObjects -> IfcContext
}
```
