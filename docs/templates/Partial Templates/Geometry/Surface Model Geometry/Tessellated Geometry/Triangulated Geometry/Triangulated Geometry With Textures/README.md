Triangulated Geometry With Textures
===================================



```
concept {
    IfcTriangulatedFaceSet:Coordinates -> IfcCartesianPointList3D
    IfcTriangulatedFaceSet:Normals -> IfcParameterValue
    IfcTriangulatedFaceSet:Closed -> IfcBoolean
    IfcTriangulatedFaceSet:CoordIndex -> IfcPositiveInteger_0
    IfcTriangulatedFaceSet:HasColours -> IfcIndexedColourMap:MappedTo
    IfcTriangulatedFaceSet:HasTextures -> IfcIndexedTriangleTextureMap:MappedTo
    IfcTriangulatedFaceSet:PnIndex -> IfcPositiveInteger_2
    IfcCartesianPointList3D:CoordList -> IfcLengthMeasure
    IfcIndexedColourMap:Colours -> IfcColourRgbList
    IfcIndexedColourMap:ColourIndex -> IfcPositiveInteger_1
    IfcIndexedColourMap:Opacity -> IfcNormalisedRatioMeasure_1
    IfcIndexedColourMap:Opacity -> IfcNormalisedRatioMeasure_2
    IfcColourRgbList:ColourList -> IfcNormalisedRatioMeasure_0
    IfcIndexedTriangleTextureMap -> Indexed_Texture_Map
}
```
