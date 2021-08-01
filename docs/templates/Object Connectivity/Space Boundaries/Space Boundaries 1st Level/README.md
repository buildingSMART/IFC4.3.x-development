Space Boundaries 1st Level
==========================

Spaces may have boundaries defined by building elements such as walls, slabs, doors, and windows. Such information may be used to determine heat transmission through surrounding materials.

```
concept {
    IfcSpace:BoundedBy -> IfcRelSpaceBoundary1stLevel:RelatingSpace
    IfcRelSpaceBoundary1stLevel:RelatedBuildingElement -> IfcElement
    IfcRelSpaceBoundary1stLevel:ConnectionGeometry -> IfcConnectionSurfaceGeometry
    IfcRelSpaceBoundary1stLevel:ParentBoundary -> IfcRelSpaceBoundary1stLevel
    IfcRelSpaceBoundary1stLevel:PhysicalOrVirtualBoundary -> IfcPhysicalOrVirtualEnum
    IfcRelSpaceBoundary1stLevel:InternalOrExternalBoundary -> IfcInternalOrExternalEnum
    IfcConnectionSurfaceGeometry:SurfaceOnRelatingElement -> IfcSurfaceOfLinearExtrusion
    IfcConnectionSurfaceGeometry:SurfaceOnRelatingElement -> IfcCurveBoundedPlane
    IfcConnectionSurfaceGeometry:SurfaceOnRelatingElement -> IfcCurveBoundedSurface
    IfcConnectionSurfaceGeometry:SurfaceOnRelatingElement -> IfcFaceBasedSurfaceModel
    IfcSurfaceOfLinearExtrusion:SweptCurve -> IfcArbitraryOpenProfileDef
    IfcArbitraryOpenProfileDef:Curve -> IfcIndexedPolyCurve
    IfcIndexedPolyCurve:Points -> IfcCartesianPointList2D
    IfcIndexedPolyCurve:Segments -> IfcArcIndex
    IfcIndexedPolyCurve:Segments -> IfcLineIndex
    IfcIndexedPolyCurve:SelfIntersect -> IfcBoolean
    IfcCartesianPointList2D:CoordList -> IfcLengthMeasure
    IfcBoolean:RelatedOpeningElement -> IfcVoidingFeature
    IfcCurveBoundedPlane:BasisSurface -> IfcPlane
    IfcPlane:Position -> IfcAxis2Placement3D
    IfcCurveBoundedSurface:BasisSurface -> IfcCylindricalSurface
    IfcCurveBoundedSurface:Boundaries -> IfcOuterBoundaryCurve
    IfcCurveBoundedSurface:ImplicitOuter -> IfcBoolean
    IfcCylindricalSurface:Position -> IfcAxis2Placement3D
    IfcOuterBoundaryCurve:Segments -> IfcCompositeCurveSegment
    IfcFaceBasedSurfaceModel:FbsmFaces -> IfcOpenShell
    IfcOpenShell:CfsFaces -> IfcFace
    IfcFace:Bounds -> IfcFaceOuterBound
}
```
