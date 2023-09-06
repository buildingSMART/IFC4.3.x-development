Single Survey Line
==================

Geometry representation of a single survey line. It can be a 2D or a 3D line, therefore using _IfcPolyline_, or _IfcIndexedPolyCurve_, or _IfcGradientCurve_, or _IfcCompositeCurve_

```
concept {
    IfcAnnotation:Representation -> IfcProductDefinitionShape
    IfcAnnotation:PredefinedType -> constraint_2
    constraint_2[label="=.SURVEY."]
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcPolyline
    IfcShapeRepresentation:Items -> IfcIndexedPolyCurve
    IfcShapeRepresentation:Items -> IfcGradientCurve 
    IfcShapeRepresentation:Items -> IfcCompositeCurve 
    IfcLabel_0 -> constraint_0
    constraint_0[label="='Annotation'"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="='Curve'"]
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```