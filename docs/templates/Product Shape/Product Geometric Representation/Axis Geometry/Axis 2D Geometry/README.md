Axis 2D Geometry
================

The 'Axis' representation using 'Curve2D' representation type is predominately used to align material layer sets to geometric representations of standard walls.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Axis'
* _IfcShapeRepresentation_._RepresentationType_ : 'Curve2D'
* _IfcShapeRepresentation_._Items_ = _IfcBoundedCurve_

```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcBoundedCurve
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Axis"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=Curve2D"]
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
