Single Survey Point
===================

Geometry representation of a single survey point.

```
concept {
    IfcAnnotation:Representation -> IfcProductDefinitionShape
    IfcAnnotation:PredefinedType -> IfcAnnotationTypeEnum
    IfcAnnotationTypeEnum -> constraint_2
    constraint_2[label="=SURVEY"]
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcCartesianPoint
    IfcLabel_0 -> constraint_0
    constraint_0[label="='Annotation'"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="='Point'"]
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```