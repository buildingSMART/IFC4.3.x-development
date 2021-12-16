Body SurfaceOrSolidModel Geometry
=================================

The _Body SurfaceOrSolidModel Geometry_ is the representation of the 3D shape of a product by surface or solid models and allows for a mixed representation.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Body'
* _IfcShapeRepresentation_._RepresentationType_ = 'SurfaceOrSolidModel'
* _IfcShapeRepresentation_._Items_ = _IfcTessellateditem_, _IfcShellBasedSurfaceModel_, _IfcFaceBasedSurfaceModel_, _IfcSolidModel_

```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcSolidModel
    IfcShapeRepresentation:Items -> IfcTessellatedFaceSet
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Body"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=SurfaceOrSolidModel"]
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
