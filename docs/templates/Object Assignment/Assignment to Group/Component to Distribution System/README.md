Component to Distribution System
================================

The _Component to Distribution System_ assignment

```
concept {
    IfcDistributionElement:HasAssignments -> IfcRelAssignsToGroup
    IfcRelAssignsToGroup:RelatingGroup -> IfcDistributionSystem
    IfcDistributionSystem:Name -> IfcLabel
}
```
