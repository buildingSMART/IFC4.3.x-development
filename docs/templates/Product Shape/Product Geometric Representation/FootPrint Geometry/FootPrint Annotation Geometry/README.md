FootPrint Annotation Geometry
=============================

The 'FootPrint Annotation Geometry' is the representation for the floor plan projection of the geometric representation of elements, comprising of mainly 2D curves, hatches and additional annotations such as a tag number or similar.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

*  _IfcShapeRepresentation_._RepresentationIdentifier_ : 'FootPrint' 
*  _IfcShapeRepresentation_._RepresentationType_ : 'Annotation2D' 
* _IfcShapeRepresentation_._Items_ : 
    * subtypes of _IfcPoint_ and _IfcCurve_ being two-dimensional and within an _IfcGeometricCurveSet_ 
    * subtypes of _IfcAnnotationFillArea_ for hatches 
    * subtypes of _IfcTextLiteral_ for text

```
concept {
    IfcProduct:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcGeometricCurveSet
    IfcShapeRepresentation:Items -> IfcAnnotationFillArea
    IfcShapeRepresentation:Items -> IfcTextLiteral
}
```
