Space Boundaries 2nd Level
==========================



```
concept {
    IfcSpace:BoundedBy -> IfcRelSpaceBoundary2ndLevel:RelatingSpace
    IfcRelSpaceBoundary2ndLevel:RelatedBuildingElement -> IfcElement
    IfcRelSpaceBoundary2ndLevel:ConnectionGeometry -> IfcConnectionSurfaceGeometry
    IfcRelSpaceBoundary2ndLevel:PhysicalOrVirtualBoundary -> IfcPhysicalOrVirtualEnum
    IfcRelSpaceBoundary2ndLevel:InternalOrExternalBoundary -> IfcInternalOrExternalEnum
    IfcRelSpaceBoundary2ndLevel:ParentBoundary -> IfcRelSpaceBoundary2ndLevel
    IfcRelSpaceBoundary2ndLevel:CorrespondingBoundary -> IfcRelSpaceBoundary2ndLevel
    IfcConnectionSurfaceGeometry:SurfaceOnRelatingElement -> IfcCurveBoundedPlane
    IfcConnectionSurfaceGeometry:SurfaceOnRelatingElement -> IfcFaceBasedSurfaceModel
    IfcCurveBoundedPlane:BasisSurface -> IfcPlane
    IfcCurveBoundedPlane:OuterBoundary -> IfcIndexedPolyCurve
    IfcPlane:Position -> IfcAxis2Placement3D
    IfcFaceBasedSurfaceModel:FbsmFaces -> IfcOpenShell
    IfcOpenShell:CfsFaces -> IfcFace
    IfcFace:Bounds -> IfcFaceOuterBound
}
```
