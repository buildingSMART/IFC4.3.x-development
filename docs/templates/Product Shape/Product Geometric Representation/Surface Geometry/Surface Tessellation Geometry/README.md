Surface Tessellation Geometry
=============================



```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcTriangulatedFaceSet
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Surface"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=Tessellation"]
    IfcTriangulatedFaceSet:Coordinates -> IfcCartesianPointList3D
    IfcTriangulatedFaceSet:Normals -> IfcParameterValue
    IfcTriangulatedFaceSet:LayerAssignment -> IfcPresentationLayerAssignment:AssignedItems
    IfcTriangulatedFaceSet:StyledByItem -> IfcStyledItem:Item
    IfcCartesianPointList3D:CoordList -> IfcLengthMeasure
    IfcPresentationLayerAssignment -> Layer
    IfcStyledItem:Styles -> IfcSurfaceStyle
    IfcSurfaceStyle -> Surface_Color_Style
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
