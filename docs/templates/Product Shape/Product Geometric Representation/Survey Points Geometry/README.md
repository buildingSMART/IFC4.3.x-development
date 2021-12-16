Survey Points Geometry
======================

Elements may provide a 'SurveyPoints' representation for defining a contour such as for _IfcSite_. It contains the survey points as a set of Cartesian points and optionally breaklines.

The representation identifier and type and the only allowed single representation item of the 'SurveyPoints' representation are:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'SurveyPoints'
* _IfcShapeRepresentation_._RepresentationType_ : 'GeometricCurveSet'
* _IfcShapeRepresentation_._Items_ = _IfcGeometricCurveSet_

```
concept {
    IfcSite:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcGeometricCurveSet
    IfcLabel_0 -> constraint_0
    constraint_0[label="=SurveyPoints"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=GeometricCurveSet"]
    IfcGeometricCurveSet:Elements -> IfcCartesianPoint
    IfcGeometricCurveSet:Elements -> IfcPolyline
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
