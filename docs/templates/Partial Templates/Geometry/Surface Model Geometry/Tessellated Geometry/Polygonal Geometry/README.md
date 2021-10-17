Polygonal Geometry
==================



```
concept {
    IfcPolygonalFaceSet:Coordinates -> IfcCartesianPointList3D
    IfcPolygonalFaceSet:Closed -> IfcBoolean
    IfcPolygonalFaceSet:Faces -> IfcIndexedPolygonalFace
    IfcPolygonalFaceSet:Faces -> IfcIndexedPolygonalFaceWithVoids
    IfcPolygonalFaceSet:PnIndex -> IfcPositiveInteger
    IfcPolygonalFaceSet:HasColours -> IfcIndexedColourMap
    IfcCartesianPointList3D:CoordList -> IfcLengthMeasure
    IfcIndexedPolygonalFace:CoordIndex -> IfcPositiveInteger
    IfcIndexedPolygonalFaceWithVoids:CoordIndex -> IfcPositiveInteger
    IfcIndexedPolygonalFaceWithVoids:InnerCoordIndices -> IfcPositiveInteger
    IfcIndexedColourMap:Opacity -> IfcNormalisedRatioMeasure
    IfcIndexedColourMap:Colours -> IfcColourRgbList
    IfcIndexedColourMap:ColourIndex -> IfcPositiveInteger
    IfcColourRgbList:ColourList -> IfcNormalisedRatioMeasure
}
```
