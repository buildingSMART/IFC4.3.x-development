Body AdvancedSwept Directrix Geometry
=====================================



```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcSurfaceCurveSweptAreaSolid
    IfcShapeRepresentation:Items -> IfcFixedReferenceSweptAreaSolid
}
```
