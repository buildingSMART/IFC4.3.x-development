Alignment Decomposition
=======================



```
concept {
    IfcAlignment:IsNestedBy -> IfcRelNests
    IfcRelNests:RelatedObjects -> IfcAlignmentHorizontal
    IfcRelNests:RelatedObjects -> IfcAlignmentSegment
    IfcRelNests:RelatedObjects -> IfcAlignmentVertical
    IfcRelNests:RelatedObjects -> IfcAlignmentSegment
    IfcRelNests:RelatedObjects -> IfcAlignmentCant
    IfcRelNests:RelatedObjects -> IfcAlignmentSegment
    IfcRelNests:RelatedObjects -> IfcAlignmentHorizontal
    IfcRelNests:RelatedObjects -> IfcAlignmentSegment
    IfcRelNests:RelatedObjects -> IfcAlignmentVertical
    IfcRelNests:RelatedObjects -> IfcAlignmentSegment
    IfcRelNests:RelatedObjects -> IfcAlignmentCant
    IfcRelNests:RelatedObjects -> IfcAlignmentSegment
    IfcRelNests:RelatedObjects -> IfcAlignmentHorizontal
    IfcRelNests:RelatedObjects -> IfcAlignmentSegment
    IfcRelNests:RelatedObjects -> IfcAlignmentVertical
    IfcRelNests:RelatedObjects -> IfcAlignmentSegment
    IfcRelNests:RelatedObjects -> IfcAlignmentCant
    IfcRelNests:RelatedObjects -> IfcAlignmentSegment
    IfcRelNests:RelatedObjects -> IfcAlignmentHorizontal
    IfcRelNests:RelatedObjects -> IfcAlignmentSegment
    IfcRelNests:RelatedObjects -> IfcAlignmentVertical
    IfcRelNests:RelatedObjects -> IfcAlignmentSegment
    IfcRelNests:RelatedObjects -> IfcAlignmentCant
    IfcRelNests:RelatedObjects -> IfcAlignmentSegment
    IfcAlignmentHorizontal:IsNestedBy -> IfcRelNests
    IfcAlignmentSegment:DesignParameters -> IfcAlignmentHorizontalSegment
    IfcAlignmentSegment:DesignParameters -> IfcAlignmentVerticalSegment
    IfcAlignmentSegment:DesignParameters -> IfcAlignmentCantSegment
    IfcAlignmentSegment:DesignParameters -> IfcAlignmentHorizontalSegment
    IfcAlignmentSegment:DesignParameters -> IfcAlignmentVerticalSegment
    IfcAlignmentSegment:DesignParameters -> IfcAlignmentCantSegment
    IfcAlignmentSegment:DesignParameters -> IfcAlignmentHorizontalSegment
    IfcAlignmentSegment:DesignParameters -> IfcAlignmentVerticalSegment
    IfcAlignmentSegment:DesignParameters -> IfcAlignmentCantSegment
    IfcAlignmentVertical:IsNestedBy -> IfcRelNests
    IfcAlignmentCant:IsNestedBy -> IfcRelNests
}
```
