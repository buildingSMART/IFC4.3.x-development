Box Geometry
============

Elements may have a simplified 'Box' representation describing the dimensions of the smallest box bounding the object. Such representation may be used for more efficient spatial indexing or hit-testing.

The representation identifier and type and the only allowed single representation item of the 'Box' representation are:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Box'
* _IfcShapeRepresentation_._RepresentationType_ : 'BoundingBox'
* _IfcShapeRepresentation_._Items_ = _IfcBoundingBox_

> NOTE&nbsp; The specification does not determine the method by which the bounding box has to be created. If such a method need to be prescribed the definition has to be established by model view definitions or implementer agreements.

```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcBoundingBox
}
```
