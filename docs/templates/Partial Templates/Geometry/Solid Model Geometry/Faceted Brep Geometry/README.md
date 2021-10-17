Faceted Brep Geometry
=====================



```
concept {
    IfcFacetedBrep:Outer -> IfcClosedShell
    IfcClosedShell:CfsFaces -> IfcFaceSurface
    IfcFaceSurface:Bounds -> IfcFaceBound
    IfcFaceSurface:Bounds -> IfcFaceOuterBound
    IfcFaceBound:Bound -> IfcPolyLoop
    IfcFaceBound:Orientation -> IfcBoolean
    IfcPolyLoop:Polygon -> IfcCartesianPoint
    IfcPolyLoop:Polygon -> IfcCartesianPoint
    IfcPolyLoop:Polygon -> IfcCartesianPoint
    IfcPolyLoop:Polygon -> IfcCartesianPoint
    IfcFaceOuterBound:Bound -> IfcPolyLoop
    IfcFaceOuterBound:Orientation -> IfcBoolean
}
```
