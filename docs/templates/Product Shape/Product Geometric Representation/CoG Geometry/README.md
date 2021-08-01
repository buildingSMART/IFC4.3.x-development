CoG Geometry
============

Elements may have a 'CoG' representation describing the Center of Gravity as a point. Such representation may be used for allowing validation checks to verify, that the CoG after import of the 'Body' shape representation matches this explicit value created during export, taking acceptable numeric tolerances into account.

The representation identifier and type and the only allowed single representation item of the 'CoG' representation are:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'CoG'
* _IfcShapeRepresentation_._RepresentationType_ : 'BoundingBox'
* _IfcShapeRepresentation_._Items_ = _IfcCartesianPoint_

```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcCartesianPoint
}
```
