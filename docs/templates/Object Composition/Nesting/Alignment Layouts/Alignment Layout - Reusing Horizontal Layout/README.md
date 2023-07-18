Alignment Layout - Reusing Horizontal Layout
============================================



```
concept {
    IfcAlignment_0:IsNestedBy -> IfcRelNests_0:RelatingObject
    IfcAlignment_0 -> Parent
    IfcAlignment_0:IsDecomposedBy -> IfcRelAggregates_0:RelatingObject
    IfcRelAggregates_0:RelatedObjects -> IfcAlignment_1
    IfcRelAggregates_0:RelatedObjects -> IfcAlignment_2
    IfcRelNests_0:RelatedObjects -> IfcAlignmentHorizontal
    IfcAlignmentHorizontal:IsNestedBy -> IfcRelNests_1:RelatingObject
    IfcRelNests_1:RelatedObjects -> IfcAlignmentSegment_0
    IfcAlignmentSegment_0:DesignParameters -> IfcAlignmentHorizontalSegment
    IfcAlignment_1:IsNestedBy -> IfcRelNests_2:RelatingObject
    IfcAlignment_1 -> Child_1
    IfcRelNests_2:RelatedObjects -> IfcAlignmentVertical_1
    IfcAlignmentVertical_1:IsNestedBy -> IfcRelNests_3:RelatingObject
    IfcRelNests_3:RelatedObjects -> IfcAlignmentSegment_1
    IfcAlignmentSegment_1:DesignParameters -> IfcAlignmentVerticalSegment_1
    IfcAlignment_2:IsNestedBy -> IfcRelNests_4:RelatingObject
    IfcAlignment_2 -> Child_2
    IfcRelNests_4:RelatedObjects -> IfcAlignmentVertical_2
    IfcAlignmentVertical_2:IsNestedBy -> IfcRelNests_6:RelatingObject
    IfcRelNests_6:RelatedObjects -> IfcAlignmentSegment_3
    IfcAlignmentSegment_3:DesignParameters -> IfcAlignmentVerticalSegment_2
    IfcRelNests_4:RelatedObjects -> IfcAlignmentCant
    IfcAlignmentCant:IsNestedBy -> IfcRelNests_5:RelatingObject
    IfcRelNests_5:RelatedObjects -> IfcAlignmentSegment_2
    IfcAlignmentSegment_2:DesignParameters -> IfcAlignmentCantSegment
}
```
