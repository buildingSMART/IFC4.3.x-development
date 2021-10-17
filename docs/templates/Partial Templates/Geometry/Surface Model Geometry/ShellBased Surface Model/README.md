ShellBased Surface Model
========================



```
concept {
    IfcShellBasedSurfaceModel:SbsmBoundary -> IfcClosedShell
    IfcShellBasedSurfaceModel:SbsmBoundary -> IfcOpenShell
    IfcShellBasedSurfaceModel:StyledByItem -> IfcStyledItem
    IfcClosedShell:CfsFaces -> IfcFaceSurface
    IfcFaceSurface:Bounds -> IfcFaceBound
    IfcFaceSurface:Bounds -> IfcFaceOuterBound
    IfcFaceSurface:SameSense -> IfcBoolean
    IfcFaceBound:Bound -> IfcPolyLoop
    IfcFaceBound:Orientation -> IfcBoolean
    IfcPolyLoop:Polygon -> IfcCartesianPoint
    IfcStyledItem:Styles -> IfcSurfaceStyle
}
```
