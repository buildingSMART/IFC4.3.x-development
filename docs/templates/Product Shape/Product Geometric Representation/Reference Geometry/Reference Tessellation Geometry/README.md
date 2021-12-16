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
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcTriangulatedFaceSet
    IfcShapeRepresentation:Items -> IfcPolygonalFaceSet
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Reference"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=Tessellation"]
    IfcTriangulatedFaceSet -> Triangulated_Geometry
    IfcPolygonalFaceSet -> Polygonal_Geometry
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
}
```
