Body AdvancedBrep Geometry
==========================

The _Body Brep Geometry_ is the representation of the 3D shape of a product by boundary representation models, including NURBS.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Body'
* _IfcShapeRepresentation_._RepresentationType_ = 'AdvancedBrep'
* _IfcShapeRepresentation_._Items_ = _IfcAdvancedBrep_, _IfcFacetedBrep_

```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcAdvancedBrep
    IfcShapeRepresentation:Items -> IfcFacetedBrep
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
