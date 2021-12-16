Surface Geometry
================

Elements may have a 'Surface' representation describing the outer surface of the object. Such representation may be used for hit-testing objects having part composition such as framed walls, or for defining thermal boundaries idealized at the middle plane of an element.

The representation identifier of the surface representation is:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Surface'

```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Surface"]
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
