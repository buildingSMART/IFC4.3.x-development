Alignment Geometry Cant
=======================



```
concept {
    IfcAlignment:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcSegmentedReferenceCurve
    IfcSegmentedReferenceCurve:BaseCurve -> IfcGradientCurve
    IfcSegmentedReferenceCurve:Segments -> IfcCurveSegment
    IfcSegmentedReferenceCurve:EndPoint -> IfcPlacement
}
```
