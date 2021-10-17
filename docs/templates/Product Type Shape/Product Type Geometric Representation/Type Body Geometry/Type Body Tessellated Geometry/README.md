Type Body Tessellated Geometry
==============================



```
concept {
    IfcElementType:RepresentationMaps -> IfcRepresentationMap
    IfcRepresentationMap:MappedRepresentation -> IfcShapeRepresentation
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement3D
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement2D
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcTriangulatedFaceSet
    IfcTriangulatedFaceSet:Coordinates -> IfcCartesianPointList3D
    IfcTriangulatedFaceSet:Normals -> IfcParameterValue
    IfcTriangulatedFaceSet:HasColours -> IfcIndexedColourMap
    IfcTriangulatedFaceSet:HasTextures -> IfcIndexedTriangleTextureMap
    IfcTriangulatedFaceSet:StyledByItem -> IfcStyledItem
    IfcCartesianPointList3D:CoordList -> IfcLengthMeasure
    IfcIndexedColourMap:Colours -> IfcColourRgbList
    IfcColourRgbList:ColourList -> IfcNormalisedRatioMeasure
    IfcIndexedTriangleTextureMap:Maps -> IfcImageTexture
    IfcStyledItem:Styles -> IfcSurfaceStyle
}
```
