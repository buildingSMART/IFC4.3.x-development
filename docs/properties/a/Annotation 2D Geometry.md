Annotation 2D Geometry
======================

The 'Annotation 2D Geometry' is used, when the representation of an annotation includes specific drafting representation elements, in particular areas for hatching and text.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ : 'Annotation' 
*  _IfcShapeRepresentation_._RepresentationType_ : 'Annotation2D' 
* _IfcShapeRepresentation_._Items_ : 
    * subtypes of _IfcPoint_ and _IfcCurve_ being two-dimensional and within an _IfcGeometricCurveSet_ 
    * subtypes of _IfcAnnotationFillArea_ for hatches 
    * subtypes of _IfcTextLiteral_ for text
