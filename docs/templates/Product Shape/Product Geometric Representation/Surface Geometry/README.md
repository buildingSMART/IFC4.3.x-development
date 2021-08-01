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
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
}
```
