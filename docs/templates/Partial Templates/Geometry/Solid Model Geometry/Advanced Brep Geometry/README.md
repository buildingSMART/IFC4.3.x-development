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
    IfcFaceOuterBound:Orientation -> IfcBoolean_0
    IfcFaceOuterBound:Bound -> IfcEdgeLoop
    IfcEdgeLoop:EdgeList -> IfcOrientedEdge
    IfcOrientedEdge:EdgeElement -> IfcEdgeCurve
    IfcEdgeCurve:EdgeStart -> IfcVertexPoint_0
    IfcEdgeCurve:EdgeEnd -> IfcVertexPoint_1
    IfcEdgeCurve:EdgeGeometry -> IfcRationalBSplineCurveWithKnots
    IfcEdgeCurve:EdgeGeometry -> IfcPolyline
    IfcEdgeCurve:SameSense -> IfcBoolean_1
    IfcRationalBSplineCurveWithKnots:Degree -> IfcInteger_0
    IfcRationalBSplineCurveWithKnots:ControlPointsList -> IfcCartesianPoint_0
    IfcRationalBSplineCurveWithKnots:CurveForm -> IfcBSplineCurveForm
    IfcRationalBSplineCurveWithKnots:ClosedCurve -> IfcLogical_0
    IfcRationalBSplineCurveWithKnots:SelfIntersect -> IfcLogical_1
    IfcRationalBSplineCurveWithKnots:KnotMultiplicities -> IfcInteger_1
    IfcRationalBSplineCurveWithKnots:Knots -> IfcParameterValue_0
    IfcRationalBSplineCurveWithKnots:KnotSpec -> IfcKnotType_0
    IfcRationalBSplineCurveWithKnots:WeightsData -> IfcReal_0
    IfcPolyline:Points -> IfcCartesianPoint_1
    IfcRationalBSplineSurfaceWithKnots:UDegree -> IfcInteger_2
    IfcRationalBSplineSurfaceWithKnots:VDegree -> IfcInteger_3
    IfcRationalBSplineSurfaceWithKnots:ControlPointsList -> IfcCartesianPoint_2
    IfcRationalBSplineSurfaceWithKnots:UClosed -> IfcLogical_2
    IfcRationalBSplineSurfaceWithKnots:VClosed -> IfcLogical_3
    IfcRationalBSplineSurfaceWithKnots:UMultiplicities -> IfcInteger_4
    IfcRationalBSplineSurfaceWithKnots:VMultiplicities -> IfcInteger_5
    IfcRationalBSplineSurfaceWithKnots:UKnots -> IfcParameterValue_1
    IfcRationalBSplineSurfaceWithKnots:VKnots -> IfcParameterValue_2
    IfcRationalBSplineSurfaceWithKnots:KnotSpec -> IfcKnotType_1
    IfcRationalBSplineSurfaceWithKnots:WeightsData -> IfcReal_1
    IfcCylindricalSurface:Position -> IfcAxis2Placement3D_0
    IfcCylindricalSurface:Radius -> IfcPositiveLengthMeasure_0
    IfcToroidalSurface:Position -> IfcAxis2Placement3D_1
    IfcToroidalSurface:MajorRadius -> IfcPositiveLengthMeasure_1
    IfcToroidalSurface:MinorRadius -> IfcPositiveLengthMeasure_2
    IfcPlane:Position -> IfcAxis2Placement3D_2
}
```
