Topography Geometry
===================

Elements describing surface contours may provide a 'Topography' representation. This representation consists of _IfcCartesianPointList3D_ containing a set of points (in no particular order) having unique horizontal coordinates (X and Y axes), with potentially variable vertical coordinates (Z axis). This representation may also contain optional breaklines using _IfcIndexedPolyCurve_.

```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcCartesianPointList3D
    IfcShapeRepresentation:Items -> IfcIndexedPolyCurve
    IfcCartesianPointList3D:CoordList -> IfcLengthMeasure
    IfcIndexedPolyCurve:Points -> IfcCartesianPointList3D
    IfcIndexedPolyCurve:SelfIntersect -> IfcBoolean
    IfcIndexedPolyCurve:Segments -> IfcArcIndex
    IfcIndexedPolyCurve:Segments -> IfcLineIndex
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
}
```
