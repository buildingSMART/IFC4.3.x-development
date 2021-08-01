Product Relative Positioning
============================

An _IfcProduct_ can be placed relative to a positioning element such as _IfcAlignment_, _IfcGrid_ or _IfcReferent_.

```
concept {
    IfcProduct:PositionedRelativeTo -> IfcRelPositions:RelatedProducts
    IfcRelPositions:RelatingPositioningElement -> IfcPositioningElement
}
```
