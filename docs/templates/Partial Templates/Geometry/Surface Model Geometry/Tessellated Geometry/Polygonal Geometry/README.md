Polygonal Geometry
==================



```
concept {
    IfcPolygonalFaceSet:Coordinates -> IfcCartesianPointList3D
    IfcPolygonalFaceSet:Closed -> IfcBoolean
    IfcPolygonalFaceSet:Faces -> IfcIndexedPolygonalFace
    IfcPolygonalFaceSet:Faces -> IfcIndexedPolygonalFaceWithVoids
    IfcPolygonalFaceSet:PnIndex -> IfcPositiveInteger_3
    IfcPolygonalFaceSet:HasColours -> IfcIndexedColourMap:MappedTo
    IfcCartesianPointList3D:CoordList -> IfcLengthMeasure
    IfcIndexedPolygonalFace:CoordIndex -> IfcPositiveInteger_0
    IfcIndexedPolygonalFaceWithVoids:CoordIndex -> IfcPositiveInteger_1
    IfcIndexedPolygonalFaceWithVoids:InnerCoordIndices -> IfcPositiveInteger_2
    IfcIndexedColourMap:Opacity -> IfcNormalisedRatioMeasure_0
    IfcIndexedColourMap:Colours -> IfcColourRgbList
    IfcIndexedColourMap:ColourIndex -> IfcPositiveInteger_4
    IfcColourRgbList:ColourList -> IfcNormalisedRatioMeasure_1
}
```
