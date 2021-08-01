Port to Distribution System
===========================

The _Port to Distribution System_ assignment

```
concept {
    IfcDistributionPort:HasAssignments -> IfcRelAssignsToGroup
    IfcRelAssignsToGroup:RelatingGroup -> IfcDistributionSystem
    IfcDistributionSystem:Name -> IfcLabel
}
```
