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
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcAdvancedBrep
    IfcShapeRepresentation:Items -> IfcFacetedBrep
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Body"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=AdvancedBrep"]
    IfcAdvancedBrep -> Advanced_Brep_Geometry
    IfcFacetedBrep -> Faceted_Brep_Geometry
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
