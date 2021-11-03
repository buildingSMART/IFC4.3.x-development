Type Body Brep Geometry
=======================



```
concept {
    IfcTypeProduct:RepresentationMaps -> IfcRepresentationMap
    IfcRepresentationMap:MappedRepresentation -> IfcShapeRepresentation
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement3D
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement2D
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcFacetedBrep
    IfcFacetedBrep:Outer -> IfcClosedShell
    IfcClosedShell:CfsFaces -> IfcFace
    IfcFace:Bounds -> IfcFaceOuterBound
    IfcFaceOuterBound:Bound -> IfcPolyLoop
    IfcFaceOuterBound:Orientation -> IfcBoolean
    IfcPolyLoop:Polygon -> IfcCartesianPoint
    IfcShapeRepresentation:RepresentationType[binding="RepresentationType"]
    IfcShapeRepresentation:Items[binding="Geometry"]
}
```
