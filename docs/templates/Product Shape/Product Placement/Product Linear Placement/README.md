Product Linear Placement
========================

A Product Linear Placement takes into account the ISO 19148 Linear referencing standard. Linear placement is defined by a position relative to a _IfcLinearPositioningElement_ (distance along and optionally lateral, vertical and longitudinal offsets), a horizontal reference direction, and a vertical axis direction. Each product placed with Product Linear Placement has an absolute placement on the _IfcLinearPositioningElement_._Representation_ where the _IfcLinearPositioningElement_  is typically instantiated as an IfcAlignment. Therefore, similarly to how _IfcSpatialElement_._ObjectPlacement_ sets the context for all contained elements, the _IfcLinearPositioningElement_._ObjectPlacement_ sets the context for all elements positioned on it. Consequently, each product placement that uses Product Linear Placement references the _IfcObjectPlacement_ of the _IfcLinearPositioningElement_ through _IfcLinearPlacement_._PlacementRelTo_.

```
concept {
    IfcProduct:ObjectPlacement -> IfcLinearPlacement
    IfcLinearPlacement:RelativePlacement -> IfcAxis2PlacementLinear
    IfcLinearPlacement:PlacementRelTo -> IfcLocalPlacement
    IfcLocalPlacement:PlacesObject -> IfcLinearPositioningElement:ObjectPlacement
    IfcLinearPositioningElement:Name -> IfcLabel
    IfcProduct:ObjectPlacement[binding="HasPlacement"]
    IfcLinearPlacement:RelativePlacement[binding="RelativePlacement"]
    IfcLocalPlacement:PlacesObject[binding="RelativeToElement"]
    IfcLinearPositioningElement:Name[binding="LinearPositioningElementName"]
}
```
