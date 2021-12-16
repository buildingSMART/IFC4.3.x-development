ShellBased Surface Model
========================



```
concept {
    IfcShellBasedSurfaceModel:SbsmBoundary -> IfcClosedShell
    IfcShellBasedSurfaceModel:SbsmBoundary -> IfcOpenShell
    IfcShellBasedSurfaceModel:StyledByItem -> IfcStyledItem:Item
    IfcClosedShell:CfsFaces -> IfcFaceSurface
    IfcFaceSurface:Bounds -> IfcFaceBound
    IfcFaceSurface:Bounds -> IfcFaceOuterBound
    IfcFaceSurface:SameSense -> IfcBoolean_1
    IfcFaceBound:Bound -> IfcPolyLoop
    IfcFaceBound:Orientation -> IfcBoolean_0
    IfcPolyLoop:Polygon -> IfcCartesianPoint
    IfcStyledItem:Styles -> IfcSurfaceStyle
    IfcSurfaceStyle -> Surface_Color_Style
}
```
