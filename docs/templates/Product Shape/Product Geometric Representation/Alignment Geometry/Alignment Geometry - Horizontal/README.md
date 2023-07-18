Alignment Geometry - Horizontal
===============================

This concept template applies to alignments defined only by an horizontal layout.

* _RepresentationIdentifier_ = 'Axis'
* _RepresentationType_ = 'Curve2D'

```
concept {
    IfcAlignment:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation_0
    IfcShapeRepresentation_0:RepresentationIdentifier -> IfcLabel_2
    IfcShapeRepresentation_0:RepresentationType -> IfcLabel_3
    IfcShapeRepresentation_0:Items -> IfcCompositeCurve
    IfcLabel_2 -> constraint_2
    constraint_2[label="=Axis"]
    IfcLabel_3 -> constraint_3
    constraint_3[label="=Curve2D"]
    IfcCompositeCurve:Segments -> IfcCurveSegment_0

}
```