Space Boundaries 2nd Level
==========================



```
concept {
    IfcSpace:BoundedBy -> IfcRelSpaceBoundary2ndLevel_0:RelatingSpace
    IfcRelSpaceBoundary2ndLevel_0:RelatedBuildingElement -> IfcElement
    IfcRelSpaceBoundary2ndLevel_0:ConnectionGeometry -> IfcConnectionSurfaceGeometry
    IfcRelSpaceBoundary2ndLevel_0:PhysicalOrVirtualBoundary -> IfcPhysicalOrVirtualEnum
    IfcRelSpaceBoundary2ndLevel_0:InternalOrExternalBoundary -> IfcInternalOrExternalEnum
    IfcRelSpaceBoundary2ndLevel_0:ParentBoundary -> IfcRelSpaceBoundary2ndLevel_1
    IfcRelSpaceBoundary2ndLevel_0:CorrespondingBoundary -> IfcRelSpaceBoundary2ndLevel_2
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
