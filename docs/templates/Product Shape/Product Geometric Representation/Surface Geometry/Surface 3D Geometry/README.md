Surface 3D Geometry
===================

The _Surface 3D Geometry_ is the standard surfacic represenation for elements having a 'Surface' representation describing the inner or outer surface of the object, e.g. for defining thermal boundaries idealized at the middle plane of an element.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Surface'
* _IfcShapeRepresentation_._RepresentationType_ = 'Surface3D'
* _IfcShapeRepresentation_._Items_ = _IfcBoundedSurface_, _IfcSweptSurface_

```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcBoundedSurface
    IfcShapeRepresentation:Items -> IfcSweptSurface
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Surface"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=Surface3D"]
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
