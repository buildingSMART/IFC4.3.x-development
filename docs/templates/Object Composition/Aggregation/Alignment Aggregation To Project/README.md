Alignment Aggregation To Project
================================

Every _IfcAlignment_ must be related to _IfcProject_ using the _IfcRelAggregates_ relationship - either directly or indirectly. The indirect case is when a child alignment is aggregated to a parent alignment. In this case, only the parent alignment must be related to _IfcProject_.

```
concept {
    IfcAlignment:Decomposes -> IfcRelAggregates:RelatedObjects
    IfcAlignment:Name -> IfcLabel
    IfcRelAggregates:RelatingObject -> IfcProject:IsDecomposedBy

    IfcRelAggregates:RelatedObjects[binding="RelatedObjects"]
    IfcAlignment:Name[binding="AlignmentName"]
}
```
