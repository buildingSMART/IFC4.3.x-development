Triangulated Geometry With Textures
===================================



```
concept {
    IfcTriangulatedFaceSet:Coordinates -> IfcCartesianPointList3D
    IfcTriangulatedFaceSet:Normals -> IfcParameterValue
    IfcTriangulatedFaceSet:Closed -> IfcBoolean
    IfcTriangulatedFaceSet:CoordIndex -> IfcPositiveInteger
    IfcTriangulatedFaceSet:HasColours -> IfcIndexedColourMap
    IfcTriangulatedFaceSet:HasTextures -> IfcIndexedTriangleTextureMap
    IfcTriangulatedFaceSet:PnIndex -> IfcPositiveInteger
    IfcCartesianPointList3D:CoordList -> IfcLengthMeasure
    IfcIndexedColourMap:Colours -> IfcColourRgbList
    IfcIndexedColourMap:ColourIndex -> IfcPositiveInteger
    IfcIndexedColourMap:Opacity -> IfcNormalisedRatioMeasure
    IfcIndexedColourMap:Opacity -> IfcNormalisedRatioMeasure
    IfcColourRgbList:ColourList -> IfcNormalisedRatioMeasure
}
```
