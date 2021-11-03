FootPrint GeomSet Geometry
==========================

The 'FootPrint GeomSet Geometry' is the standard representation for the floor plan projection of the geometric representation of elements, comprising of mainly 2D curves

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation are used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ : 'FootPrint'
* _IfcShapeRepresentation_._RepresentationType_ : 'GeometricCurveSet'
* _IfcShapeRepresentation_._Items_ : _IfcGeometricCurveSet_

```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcGeometricCurveSet
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
