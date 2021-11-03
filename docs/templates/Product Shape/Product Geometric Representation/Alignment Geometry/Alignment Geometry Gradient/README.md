Alignment Geometry Gradient
===========================



```
concept {
    IfcAlignment:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcGradientCurve
    IfcGradientCurve:BaseCurve -> IfcCompositeCurve
    IfcGradientCurve:Segments -> IfcCurveSegment
    IfcCompositeCurve:Segments -> IfcCurveSegment
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
}
```
