Alignment Spatial Reference
===========================

```
concept {
    IfcAlignment:ReferencedInStructures -> IfcRelReferencedInSpatialStructure:RelatedElements
    IfcAlignment:Name -> IfcLabel_0
    IfcRelReferencedInSpatialStructure:RelatingStructure -> IfcSpatialElement:ReferencesElements

    IfcSpatialElement:ReferencesElements[binding="ReferencedElements"]
    IfcRelReferencedInSpatialStructure:RelatingStructure[binding="RelatingStructure"]
    IfcAlignment:Name[binding="AlignmentName"]
}
```
