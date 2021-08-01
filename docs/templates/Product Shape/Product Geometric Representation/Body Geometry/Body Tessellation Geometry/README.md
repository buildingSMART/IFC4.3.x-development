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
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcTriangulatedFaceSet
    IfcShapeRepresentation:Items -> IfcPolygonalFaceSet
}
```
