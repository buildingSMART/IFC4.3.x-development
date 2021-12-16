FootPrint GeomSet PolyCurve Geometry
====================================

This specialization of the footprint representation uses indexed curves to represent boundaries.

```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcGeometricCurveSet
    IfcLabel_0 -> constraint_0
    constraint_0[label="=FootPrint"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=GeometricCurveSet"]
    IfcGeometricCurveSet:Elements -> IfcIndexedPolyCurve
    IfcIndexedPolyCurve:Points -> IfcCartesianPointList2D
    IfcIndexedPolyCurve:Segments -> IfcArcIndex
    IfcIndexedPolyCurve:Segments -> IfcLineIndex
    IfcIndexedPolyCurve:SelfIntersect -> IfcBoolean
    IfcCartesianPointList2D:CoordList -> IfcLengthMeasure
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
