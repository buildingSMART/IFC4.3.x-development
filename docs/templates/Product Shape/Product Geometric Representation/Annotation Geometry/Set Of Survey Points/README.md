Set Of Survey Points
====================

Geometry representation of a set of survey points. They can be 2D points or 3D points. The set of points may not form a closed surface or a survey line.

> NOTE  When a single _IfcAnnotation_ is represented by multiple survey points, it is not possible to associate properties to the single geometrical points of the set, but only to the whole annotation. 

```
concept {
    IfcAnnotation:Representation -> IfcProductDefinitionShape
    IfcAnnotation:PredefinedType -> SURVEY
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcCartesianPointList2D
    IfcShapeRepresentation:Items -> IfcCartesianPointList3D
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Annotation"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=Point"]
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```