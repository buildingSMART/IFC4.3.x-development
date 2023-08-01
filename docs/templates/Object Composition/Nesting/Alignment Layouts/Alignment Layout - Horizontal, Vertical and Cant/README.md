Alignment Layout - Horizontal, Vertical and Cant
================================================

Nesting relationships between _IfcAlignment_ and the three layouts, with respective segments, that may define it (i.e., _IfcAlignmentHorizontal_, _IfcAlignmentVerticalSegment_, _IfcAlignmentCant_).

When defining the list of segments for the business logic (i.e., _IfcAlignmentHorizontalSegment_, _IfcAlignmentVerticalSegment_, _IfcAlignmentCantSegment_):

1. A **zero-length segment** shall be added, at the end of the list of segments for _IfcAlignmentSegment.DesignParameters_.
2. If the geometry definition is also present, then each of the zero-length segments shall have a _IfcCurveSegment_ counterpart - of length zero.

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
