Type Lighting Geometry
======================

For elements that emit light such as lamps or light fixtures, this represents the light emission of the item having _IfcShapeRepresentation.RepresentationType_ of 'LightSource' and containing one or more _IfcLightSource_ subtypes.

```
concept {
    IfcDistributionElementType:RepresentationMaps -> IfcRepresentationMap
    IfcRepresentationMap:MappedRepresentation -> IfcShapeRepresentation
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement3D
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement2D
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcLightSource
}
```
