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
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcBoundedCurve
}
```
