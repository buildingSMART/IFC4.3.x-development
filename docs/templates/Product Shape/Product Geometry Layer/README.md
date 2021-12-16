Product Geometry Layer
======================



```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:LayerAssignments -> IfcPresentationLayerAssignment:AssignedItems
    IfcPresentationLayerAssignment -> Layer
}
```
