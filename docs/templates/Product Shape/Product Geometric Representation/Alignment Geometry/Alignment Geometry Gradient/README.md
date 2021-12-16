Alignment Geometry Gradient
===========================



```
concept {
    IfcAlignment:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcGradientCurve
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Axis"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=Curve3D"]
    IfcGradientCurve -> Gradient_Curve
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
}
```
