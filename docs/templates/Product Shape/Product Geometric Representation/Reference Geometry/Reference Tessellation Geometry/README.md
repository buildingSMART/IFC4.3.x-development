Reference Tessellation Geometry
===============================

The _Reference Tessellation Geometry_ is the reference representation of the 3D shape of a product by using tessellated models. Being a reference representation it is normally not displayed and it is not used in a voiding relationship.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Reference'
* _IfcShapeRepresentation_._RepresentationType_ = 'Tessellation'
* _IfcShapeRepresentation_._Items_ = _IfcTessellatedFaceSet_

```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcTriangulatedFaceSet
    IfcShapeRepresentation:Items -> IfcPolygonalFaceSet
}
```
