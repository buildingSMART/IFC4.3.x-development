FaceBased Surface Model
=======================



```
concept {
    IfcFaceBasedSurfaceModel:FbsmFaces -> IfcConnectedFaceSet
    IfcFaceBasedSurfaceModel:StyledByItem -> IfcStyledItem
    IfcConnectedFaceSet:CfsFaces -> IfcFaceSurface
    IfcFaceSurface:Bounds -> IfcFaceBound
    IfcFaceSurface:Bounds -> IfcFaceOuterBound
    IfcFaceSurface:SameSense -> IfcBoolean
    IfcFaceBound:Bound -> IfcPolyLoop
    IfcFaceBound:Orientation -> IfcBoolean
    IfcPolyLoop:Polygon -> IfcCartesianPoint
    IfcStyledItem:Name -> IfcLabel
    IfcStyledItem:Styles -> IfcSurfaceStyle
}
```
