Product Span Positioning
========================

An _IfcProduct_ can be placed relative to two _IfcReferent_s, which indicate the start and end positions of the product along a linear section.

```
concept {
    IfcProduct:PositionedRelativeTo -> IfcRelPositions_0:RelatedProducts
    IfcProduct:PositionedRelativeTo -> IfcRelPositions_1:RelatedProducts
    IfcRelPositions_0:RelatingPositioningElement -> IfcReferent_0
    IfcRelPositions_0:Name -> IfcLabel_0
    IfcReferent_0:PredefinedType -> IfcReferentTypeEnum_0
    IfcRelPositions_1:RelatingPositioningElement -> IfcReferent_1
    IfcRelPositions_1:Name -> IfcLabel_1
    IfcReferent_1:PredefinedType -> IfcReferentTypeEnum_1
    IfcProduct:PositionedRelativeTo[binding="EndPositionedRelativeTo"]
    IfcReferent_0:PredefinedType[binding="StartPositionType"]
    IfcRelPositions_0:Name[binding="StartPositionName"]
    IfcReferent_1:PredefinedType[binding="EndPositionType"]
    IfcRelPositions_1:Name[binding="EndPositionName"]
}
```
