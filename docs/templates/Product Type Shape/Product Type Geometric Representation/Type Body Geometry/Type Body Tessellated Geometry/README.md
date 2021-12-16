Type Body Tessellated Geometry
==============================



```
concept {
    IfcElementType:RepresentationMaps -> IfcRepresentationMap
    IfcRepresentationMap:MappedRepresentation -> IfcShapeRepresentation
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement3D
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement2D
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcTriangulatedFaceSet
    IfcLabel_0 -> constraint_0
    constraint_0[label="='Surface'"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="='Tessellation'"]
    IfcTriangulatedFaceSet:Coordinates -> IfcCartesianPointList3D
    IfcTriangulatedFaceSet:Normals -> IfcParameterValue
    IfcTriangulatedFaceSet:HasColours -> IfcIndexedColourMap:MappedTo
    IfcTriangulatedFaceSet:HasTextures -> IfcIndexedTriangleTextureMap:MappedTo
    IfcTriangulatedFaceSet:StyledByItem -> IfcStyledItem:Item
    IfcCartesianPointList3D:CoordList -> IfcLengthMeasure
    IfcIndexedColourMap:Colours -> IfcColourRgbList
    IfcColourRgbList:ColourList -> IfcNormalisedRatioMeasure
    IfcIndexedTriangleTextureMap:Maps -> IfcImageTexture
    IfcImageTexture -> Image_Texture
    IfcStyledItem:Styles -> IfcSurfaceStyle
    IfcSurfaceStyle -> Surface_Color_Style
    IfcShapeRepresentation:Items[binding="Geometry"]
}
```
