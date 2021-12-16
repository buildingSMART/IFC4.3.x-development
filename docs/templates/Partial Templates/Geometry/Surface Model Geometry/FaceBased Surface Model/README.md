FaceBased Surface Model
=======================



```
concept {
    IfcFaceBasedSurfaceModel:FbsmFaces -> IfcConnectedFaceSet
    IfcFaceBasedSurfaceModel:StyledByItem -> IfcStyledItem:Item
    IfcConnectedFaceSet:CfsFaces -> IfcFaceSurface
    IfcFaceSurface:Bounds -> IfcFaceBound
    IfcFaceSurface:Bounds -> IfcFaceOuterBound
    IfcFaceSurface:SameSense -> IfcBoolean_1
    IfcFaceBound:Bound -> IfcPolyLoop
    IfcFaceBound:Orientation -> IfcBoolean_0
    IfcPolyLoop:Polygon -> IfcCartesianPoint
    IfcStyledItem:Name -> IfcLabel
    IfcStyledItem:Styles -> IfcSurfaceStyle
    IfcSurfaceStyle -> Surface_Color_Style
}
```
