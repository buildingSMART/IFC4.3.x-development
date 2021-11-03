Surface Tessellation Geometry
=============================



```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcTriangulatedFaceSet
    IfcTriangulatedFaceSet:Coordinates -> IfcCartesianPointList3D
    IfcTriangulatedFaceSet:Normals -> IfcParameterValue
    IfcTriangulatedFaceSet:LayerAssignment -> IfcPresentationLayerAssignment
    IfcTriangulatedFaceSet:StyledByItem -> IfcStyledItem
    IfcCartesianPointList3D:CoordList -> IfcLengthMeasure
    IfcStyledItem:Styles -> IfcSurfaceStyle
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
