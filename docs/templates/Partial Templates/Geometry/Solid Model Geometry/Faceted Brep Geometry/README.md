Faceted Brep Geometry
=====================



```
concept {
    IfcFacetedBrep:Outer -> IfcClosedShell
    IfcClosedShell:CfsFaces -> IfcFaceSurface
    IfcFaceSurface:Bounds -> IfcFaceBound
    IfcFaceSurface:Bounds -> IfcFaceOuterBound
    IfcFaceBound:Bound -> IfcPolyLoop_0
    IfcFaceBound:Orientation -> IfcBoolean_0
    IfcPolyLoop_0:Polygon -> IfcCartesianPoint_0
    IfcFaceOuterBound:Bound -> IfcPolyLoop_1
    IfcFaceOuterBound:Orientation -> IfcBoolean_1
    IfcPolyLoop_1:Polygon -> IfcCartesianPoint_1
}
```
