Body Clipping Geometry
======================

The _Body Clipping Geometry_ is the representation of the 3D shape of a product by using Constructive Solid Geometry models with difference operations involving half space solids only.

The following attribute values for the _IfcShapeRepresentation_ holding this geometric representation shall be used:

* _IfcShapeRepresentation_._RepresentationIdentifier_ = 'Body'
* _IfcShapeRepresentation_._RepresentationType_ = 'Clipping'
* _IfcShapeRepresentation_._Items_ = _IfcBooleanClippingResult_

> NOTE&nbsp; This representation type is predominately used for compatibility with previous releases of the standard.

```
concept {
    IfcElement:Representation -> IfcProductDefinitionShape
    IfcProductDefinitionShape:Representations -> IfcShapeRepresentation
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcBooleanClippingResult_0
    IfcLabel_0 -> constraint_0
    constraint_0[label="=Body"]
    IfcLabel_1 -> constraint_1
    constraint_1[label="=Clipping"]
    IfcBooleanClippingResult_0:Operator -> IfcBooleanOperator
    IfcBooleanClippingResult_0:FirstOperand -> IfcCsgPrimitive3D
    IfcBooleanClippingResult_0:FirstOperand -> IfcSolidModel
    IfcBooleanClippingResult_0:FirstOperand -> IfcBooleanClippingResult_1
    IfcBooleanClippingResult_0:SecondOperand -> IfcHalfSpaceSolid
    IfcBooleanClippingResult_0:SecondOperand -> IfcPolygonalBoundedHalfSpace
    IfcPolygonalBoundedHalfSpace:BaseSurface -> IfcPlane
    IfcPolygonalBoundedHalfSpace:AgreementFlag -> IfcBoolean
    IfcPolygonalBoundedHalfSpace:Position -> IfcAxis2Placement3D
    IfcPolygonalBoundedHalfSpace:PolygonalBoundary -> IfcIndexedPolyCurve
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
