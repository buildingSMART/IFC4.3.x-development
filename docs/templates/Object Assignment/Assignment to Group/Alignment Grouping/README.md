Alignment Grouping
==================



```
concept {
    IfcAlignment:HasAssignments -> IfcRelAssignsToGroup:RelatedObjects
    IfcRelAssignsToGroup:RelatingGroup -> IfcGroup:IsGroupedBy
    IfcAlignment:Name -> IfcLabel
    IfcAlignment:HasAssignments[binding="IsAssigned"]
    IfcGroup:Name[binding="GroupName"]
}
```
