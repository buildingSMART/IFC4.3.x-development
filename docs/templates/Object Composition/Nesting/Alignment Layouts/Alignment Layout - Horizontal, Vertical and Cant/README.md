Alignment Layout - Horizontal, Vertical and Cant
================================================



```
concept {
    IfcAlignment:IsNestedBy -> IfcRelNests_0:RelatingObject
    IfcRelNests_0:RelatedObjects -> IfcAlignmentHorizontal
    IfcRelNests_0:RelatedObjects -> IfcAlignmentVertical
    IfcRelNests_0:RelatedObjects -> IfcAlignmentCant
    IfcAlignmentHorizontal:IsNestedBy -> IfcRelNests_1:RelatingObject
    IfcRelNests_1:RelatedObjects -> IfcAlignmentSegment_0
    IfcAlignmentSegment_0:DesignParameters -> IfcAlignmentHorizontalSegment
    IfcAlignmentVertical:IsNestedBy -> IfcRelNests_2:RelatingObject
    IfcRelNests_2:RelatedObjects -> IfcAlignmentSegment_1
    IfcAlignmentSegment_1:DesignParameters -> IfcAlignmentVerticalSegment
    IfcAlignmentCant:IsNestedBy -> IfcRelNests_3:RelatingObject
    IfcRelNests_3:RelatedObjects -> IfcAlignmentSegment_2
    IfcAlignmentSegment_2:DesignParameters -> IfcAlignmentCantSegment
}
```
