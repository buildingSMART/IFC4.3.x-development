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

```
concept {
    IfcAnnotation:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcAnnotationFillArea
    IfcShapeRepresentation:Items -> IfcIndexedPolyCurve
    IfcShapeRepresentation:Items -> IfcCartesianPoint
    IfcShapeRepresentation:Items -> IfcTextLiteral
    IfcAnnotationFillArea:OuterBoundary -> IfcIndexedPolyCurve
    IfcAnnotationFillArea:InnerBoundaries -> IfcIndexedPolyCurve
    IfcAnnotationFillArea:StyledByItem -> IfcStyledItem
    IfcIndexedPolyCurve:Points -> IfcCartesianPointList2D
    IfcIndexedPolyCurve:Points -> IfcCartesianPointList2D
    IfcIndexedPolyCurve:Points -> IfcCartesianPointList2D
    IfcIndexedPolyCurve:Segments -> IfcArcIndex
    IfcIndexedPolyCurve:Segments -> IfcLineIndex
    IfcIndexedPolyCurve:Segments -> IfcArcIndex
    IfcIndexedPolyCurve:Segments -> IfcLineIndex
    IfcIndexedPolyCurve:Points -> IfcCartesianPointList2D
    IfcIndexedPolyCurve:Points -> IfcCartesianPointList2D
    IfcIndexedPolyCurve:Points -> IfcCartesianPointList2D
    IfcIndexedPolyCurve:Segments -> IfcArcIndex
    IfcIndexedPolyCurve:Segments -> IfcLineIndex
    IfcIndexedPolyCurve:Segments -> IfcArcIndex
    IfcIndexedPolyCurve:Segments -> IfcLineIndex
    IfcIndexedPolyCurve:Points -> IfcCartesianPointList2D
    IfcIndexedPolyCurve:Points -> IfcCartesianPointList2D
    IfcIndexedPolyCurve:Points -> IfcCartesianPointList2D
    IfcIndexedPolyCurve:Segments -> IfcArcIndex
    IfcIndexedPolyCurve:Segments -> IfcLineIndex
    IfcIndexedPolyCurve:Segments -> IfcArcIndex
    IfcIndexedPolyCurve:Segments -> IfcLineIndex
    IfcIndexedPolyCurve:StyledByItem -> IfcStyledItem
    IfcStyledItem:Styles -> IfcFillAreaStyle
    IfcStyledItem:Styles -> IfcCurveStyle
    IfcStyledItem:Styles -> IfcTextStyle
    IfcStyledItem:Styles -> IfcFillAreaStyle
    IfcStyledItem:Styles -> IfcCurveStyle
    IfcStyledItem:Styles -> IfcTextStyle
    IfcStyledItem:Styles -> IfcFillAreaStyle
    IfcStyledItem:Styles -> IfcCurveStyle
    IfcStyledItem:Styles -> IfcTextStyle
    IfcCartesianPointList2D:CoordList -> IfcLengthMeasure
    IfcTextLiteral:Literal -> IfcPresentableText
    IfcTextLiteral:Placement -> IfcAxis2Placement2D
    IfcTextLiteral:Path -> IfcTextPath
    IfcTextLiteral:StyledByItem -> IfcStyledItem
}
```
