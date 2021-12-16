Component to Distribution System
================================

The _Component to Distribution System_ assignment

```
concept {
    IfcDistributionElement:HasAssignments -> IfcRelAssignsToGroup:RelatedObjects
    IfcRelAssignsToGroup:RelatingGroup -> IfcDistributionSystem
    IfcDistributionSystem:Name -> IfcLabel
    IfcDistributionElement:HasAssignments[binding="IsAssigned"]
    IfcDistributionSystem:Name[binding="SystemName"]
}
```
