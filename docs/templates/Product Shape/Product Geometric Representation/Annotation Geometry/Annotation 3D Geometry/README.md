Annotation 3D Geometry
======================

The 'Annotation 3D Geometry' is used, when the representation of the annotation does includes surfaces and is not restricted to two-dimensional representation items.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

*  _IfcShapeRepresentation_._RepresentationIdentifier_ : 'Annotation' 
*  _IfcShapeRepresentation_._RepresentationType_ : 'GeometricSet' 
* _IfcShapeRepresentation_._Items_ : 
    * subtypes of _IfcPoint_ and _IfcCurve_ being three-dimensional and within an _IfcGeometricSet_
    * subtypes of _IfcSurface_ being three-dimensional and within an _IfcGeometricSet_

```
concept {
    IfcAnnotation:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcPoint
    IfcShapeRepresentation:Items -> IfcCurve
    IfcShapeRepresentation:Items -> IfcSurface
}
```
