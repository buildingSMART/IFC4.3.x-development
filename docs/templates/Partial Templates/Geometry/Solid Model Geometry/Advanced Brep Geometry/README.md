Advanced Brep Geometry
======================



```
concept {
    IfcAdvancedBrep:Outer -> IfcClosedShell
    IfcClosedShell:CfsFaces -> IfcAdvancedFace
    IfcAdvancedFace:Bounds -> IfcFaceOuterBound
    IfcAdvancedFace:FaceSurface -> IfcRationalBSplineSurfaceWithKnots
    IfcAdvancedFace:FaceSurface -> IfcCylindricalSurface
    IfcAdvancedFace:FaceSurface -> IfcSphericalSurface
    IfcAdvancedFace:FaceSurface -> IfcToroidalSurface
    IfcAdvancedFace:FaceSurface -> IfcPlane
    IfcFaceOuterBound:Orientation -> IfcBoolean
    IfcFaceOuterBound:Bound -> IfcEdgeLoop
    IfcEdgeLoop:EdgeList -> IfcOrientedEdge
    IfcOrientedEdge:EdgeElement -> IfcEdgeCurve
    IfcEdgeCurve:EdgeStart -> IfcVertexPoint
    IfcEdgeCurve:EdgeEnd -> IfcVertexPoint
    IfcEdgeCurve:EdgeGeometry -> IfcRationalBSplineCurveWithKnots
    IfcEdgeCurve:EdgeGeometry -> IfcPolyline
    IfcEdgeCurve:SameSense -> IfcBoolean
    IfcRationalBSplineCurveWithKnots:Degree -> IfcInteger
    IfcRationalBSplineCurveWithKnots:ControlPointsList -> IfcCartesianPoint
    IfcRationalBSplineCurveWithKnots:CurveForm -> IfcBSplineCurveForm
    IfcRationalBSplineCurveWithKnots:ClosedCurve -> IfcLogical
    IfcRationalBSplineCurveWithKnots:SelfIntersect -> IfcLogical
    IfcRationalBSplineCurveWithKnots:KnotMultiplicities -> IfcInteger
    IfcRationalBSplineCurveWithKnots:Knots -> IfcParameterValue
    IfcRationalBSplineCurveWithKnots:KnotSpec -> IfcKnotType
    IfcRationalBSplineCurveWithKnots:WeightsData -> IfcReal
    IfcPolyline:Points -> IfcCartesianPoint
    IfcRationalBSplineSurfaceWithKnots:UDegree -> IfcInteger
    IfcRationalBSplineSurfaceWithKnots:VDegree -> IfcInteger
    IfcRationalBSplineSurfaceWithKnots:ControlPointsList -> IfcCartesianPoint
    IfcRationalBSplineSurfaceWithKnots:UClosed -> IfcLogical
    IfcRationalBSplineSurfaceWithKnots:VClosed -> IfcLogical
    IfcRationalBSplineSurfaceWithKnots:UMultiplicities -> IfcInteger
    IfcRationalBSplineSurfaceWithKnots:VMultiplicities -> IfcInteger
    IfcRationalBSplineSurfaceWithKnots:UKnots -> IfcParameterValue
    IfcRationalBSplineSurfaceWithKnots:VKnots -> IfcParameterValue
    IfcRationalBSplineSurfaceWithKnots:KnotSpec -> IfcKnotType
    IfcRationalBSplineSurfaceWithKnots:WeightsData -> IfcReal
    IfcCylindricalSurface:Position -> IfcAxis2Placement3D
    IfcCylindricalSurface:Radius -> IfcPositiveLengthMeasure
    IfcToroidalSurface:Position -> IfcAxis2Placement3D
    IfcToroidalSurface:MajorRadius -> IfcPositiveLengthMeasure
    IfcToroidalSurface:MinorRadius -> IfcPositiveLengthMeasure
    IfcPlane:Position -> IfcAxis2Placement3D
}
```
