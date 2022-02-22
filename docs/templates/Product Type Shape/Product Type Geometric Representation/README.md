Product Type Geometric Representation
=====================================

Product types may have representations indicating shape representation for geometry, clearance, or other concepts.

The shape representation attached to a type is defined using the relationship _RepresentationMaps_ of data type _IfcRepresentationMap_. It provides the means to store several representation maps for different purposes. In order to utilze the representation map at each occurrence of the product type, the product occurrence has to use the concept 'Mapped Geometry'.

> NOTE  See _IfcTypeProduct_ for further information and figures/ explaning the concepts 'Product Type Representation' and 'Mapped Geometry'.

```
concept {
    IfcTypeProduct:RepresentationMaps -> IfcRepresentationMap
    IfcRepresentationMap:MappedRepresentation -> IfcShapeRepresentation
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement2D
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement3D
}
```
