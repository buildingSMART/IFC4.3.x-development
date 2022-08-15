Port to Distribution System
===========================

The _Port to Distribution System_ assignment

```
concept {
    IfcDistributionPort:HasAssignments -> IfcRelAssignsToGroup:RelatedObjects
    IfcRelAssignsToGroup:RelatingGroup -> IfcDistributionSystem:IsGroupedBy
    IfcDistributionSystem:Name -> IfcLabel
    IfcDistributionPort:HasAssignments[binding="IsAssigned"]
    IfcDistributionSystem:Name[binding="SystemName"]
}
```
