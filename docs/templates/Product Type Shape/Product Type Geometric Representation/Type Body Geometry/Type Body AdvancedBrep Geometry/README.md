Type Body AdvancedBrep Geometry
===============================



```
concept {
    IfcTypeProduct:RepresentationMaps -> IfcRepresentationMap
    IfcRepresentationMap:MappedRepresentation -> IfcShapeRepresentation
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement3D
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement2D
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcAdvancedBrep
    IfcAdvancedBrep:Outer -> IfcClosedShell
    IfcClosedShell:CfsFaces -> IfcAdvancedFace
    IfcAdvancedFace:Bounds -> IfcFaceOuterBound
    IfcAdvancedFace:FaceSurface -> IfcBSplineSurfaceWithKnots
    IfcFaceOuterBound:Bound -> IfcEdgeLoop
    IfcFaceOuterBound:Orientation -> IfcBoolean_2
    IfcEdgeLoop:EdgeList -> IfcOrientedEdge
    IfcOrientedEdge:EdgeElement -> IfcEdgeCurve
    IfcOrientedEdge:Orientation -> IfcBoolean_1
    IfcEdgeCurve:EdgeGeometry -> IfcBSplineCurveWithKnots
    IfcEdgeCurve:EdgeStart -> IfcVertexPoint_0
    IfcEdgeCurve:EdgeEnd -> IfcVertexPoint_1
    IfcEdgeCurve:SameSense -> IfcBoolean_0
    IfcBSplineCurveWithKnots:Degree -> IfcInteger_0
    IfcBSplineCurveWithKnots:ControlPointsList -> IfcCartesianPoint_0
    IfcBSplineCurveWithKnots:CurveForm -> IfcBSplineCurveForm
    IfcBSplineCurveWithKnots:ClosedCurve -> IfcLogical_0
    IfcBSplineCurveWithKnots:SelfIntersect -> IfcLogical_1
    IfcBSplineCurveWithKnots:KnotMultiplicities -> IfcInteger_1
    IfcBSplineCurveWithKnots:Knots -> IfcParameterValue_0
    IfcBSplineCurveWithKnots:KnotSpec -> IfcKnotType_0
    IfcVertexPoint_0:VertexGeometry -> IfcCartesianPoint_1
    IfcVertexPoint_1:VertexGeometry -> IfcCartesianPoint_2
    IfcBSplineSurfaceWithKnots:ControlPointsList -> IfcCartesianPoint_3
    IfcBSplineSurfaceWithKnots:UDegree -> IfcInteger_2
    IfcBSplineSurfaceWithKnots:VDegree -> IfcInteger_3
    IfcBSplineSurfaceWithKnots:SurfaceForm -> IfcBSplineSurfaceForm
    IfcBSplineSurfaceWithKnots:UClosed -> IfcLogical_2
    IfcBSplineSurfaceWithKnots:VClosed -> IfcLogical_3
    IfcBSplineSurfaceWithKnots:SelfIntersect -> IfcLogical_4
    IfcBSplineSurfaceWithKnots:UMultiplicities -> IfcInteger_4
    IfcBSplineSurfaceWithKnots:VMultiplicities -> IfcInteger_5
    IfcBSplineSurfaceWithKnots:UKnots -> IfcParameterValue_1
    IfcBSplineSurfaceWithKnots:VKnots -> IfcParameterValue_2
    IfcBSplineSurfaceWithKnots:KnotSpec -> IfcKnotType_1
    IfcShapeRepresentation:RepresentationType[binding="RepresentationType"]
    IfcShapeRepresentation:Items[binding="Geometry"]
}
```
