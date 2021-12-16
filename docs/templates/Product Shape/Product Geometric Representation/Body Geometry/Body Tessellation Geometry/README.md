Body Tessellation Geometry
==========================

The _Body Tessellation Geometry_ is the representation of the 3D shape of a product by tessellated surface models.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Body'
* _IfcShapeRepresentation_._RepresentationType_ = 'Tessellation'
* _IfcShapeRepresentation_._Items_ = _IfcTessellatedFaceSet_

```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcTriangulatedFaceSet
    IfcShapeRepresentation:Items -> IfcPolygonalFaceSet
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Body"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=Tessellation"]
    IfcTriangulatedFaceSet -> Triangulated_Geometry_With_Textures
    IfcPolygonalFaceSet -> Polygonal_Geometry
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
