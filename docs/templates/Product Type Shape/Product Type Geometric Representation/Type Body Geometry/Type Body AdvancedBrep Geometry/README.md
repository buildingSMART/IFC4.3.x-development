Type Body AdvancedBrep Geometry
===============================



```
concept {
    IfcTypeProduct:RepresentationMaps -> IfcRepresentationMap
    IfcRepresentationMap:MappedRepresentation -> IfcShapeRepresentation
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement3D
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement2D
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcAdvancedBrep
    IfcAdvancedBrep:Outer -> IfcClosedShell
    IfcClosedShell:CfsFaces -> IfcAdvancedFace
    IfcAdvancedFace:Bounds -> IfcFaceOuterBound
    IfcAdvancedFace:FaceSurface -> IfcBSplineSurfaceWithKnots
    IfcFaceOuterBound:Bound -> IfcEdgeLoop
    IfcFaceOuterBound:Orientation -> IfcBoolean
    IfcEdgeLoop:EdgeList -> IfcOrientedEdge
    IfcOrientedEdge:EdgeElement -> IfcEdgeCurve
    IfcOrientedEdge:Orientation -> IfcBoolean
    IfcEdgeCurve:EdgeGeometry -> IfcBSplineCurveWithKnots
    IfcEdgeCurve:EdgeStart -> IfcVertexPoint
    IfcEdgeCurve:EdgeEnd -> IfcVertexPoint
    IfcEdgeCurve:SameSense -> IfcBoolean
    IfcBSplineCurveWithKnots:Degree -> IfcInteger
    IfcBSplineCurveWithKnots:ControlPointsList -> IfcCartesianPoint
    IfcBSplineCurveWithKnots:CurveForm -> IfcBSplineCurveForm
    IfcBSplineCurveWithKnots:ClosedCurve -> IfcLogical
    IfcBSplineCurveWithKnots:SelfIntersect -> IfcLogical
    IfcBSplineCurveWithKnots:KnotMultiplicities -> IfcInteger
    IfcBSplineCurveWithKnots:Knots -> IfcParameterValue
    IfcBSplineCurveWithKnots:KnotSpec -> IfcKnotType
    IfcVertexPoint:VertexGeometry -> IfcCartesianPoint
    IfcVertexPoint:VertexGeometry -> IfcCartesianPoint
    IfcVertexPoint:VertexGeometry -> IfcCartesianPoint
    IfcVertexPoint:VertexGeometry -> IfcCartesianPoint
    IfcBSplineSurfaceWithKnots:ControlPointsList -> IfcCartesianPoint
    IfcBSplineSurfaceWithKnots:UDegree -> IfcInteger
    IfcBSplineSurfaceWithKnots:VDegree -> IfcInteger
    IfcBSplineSurfaceWithKnots:SurfaceForm -> IfcBSplineSurfaceForm
    IfcBSplineSurfaceWithKnots:UClosed -> IfcLogical
    IfcBSplineSurfaceWithKnots:VClosed -> IfcLogical
    IfcBSplineSurfaceWithKnots:SelfIntersect -> IfcLogical
    IfcBSplineSurfaceWithKnots:UMultiplicities -> IfcInteger
    IfcBSplineSurfaceWithKnots:VMultiplicities -> IfcInteger
    IfcBSplineSurfaceWithKnots:UKnots -> IfcParameterValue
    IfcBSplineSurfaceWithKnots:VKnots -> IfcParameterValue
    IfcBSplineSurfaceWithKnots:KnotSpec -> IfcKnotType
    IfcShapeRepresentation:RepresentationType[binding="RepresentationType"]
    IfcShapeRepresentation:Items[binding="Geometry"]
}
```
