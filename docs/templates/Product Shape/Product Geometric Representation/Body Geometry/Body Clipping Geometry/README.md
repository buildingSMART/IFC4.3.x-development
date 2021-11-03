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
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcBooleanClippingResult
    IfcBooleanClippingResult:Operator -> IfcBooleanOperator
    IfcBooleanClippingResult:FirstOperand -> IfcCsgPrimitive3D
    IfcBooleanClippingResult:FirstOperand -> IfcSolidModel
    IfcBooleanClippingResult:FirstOperand -> IfcBooleanClippingResult
    IfcBooleanClippingResult:SecondOperand -> IfcHalfSpaceSolid
    IfcBooleanClippingResult:SecondOperand -> IfcPolygonalBoundedHalfSpace
    IfcPolygonalBoundedHalfSpace:BaseSurface -> IfcPlane
    IfcPolygonalBoundedHalfSpace:AgreementFlag -> IfcBoolean
    IfcPolygonalBoundedHalfSpace:Position -> IfcAxis2Placement3D
    IfcPolygonalBoundedHalfSpace:PolygonalBoundary -> IfcIndexedPolyCurve
    IfcShapeRepresentation:RepresentationIdentifier[binding="Identifier"]
    IfcShapeRepresentation:RepresentationType[binding="Type"]
    IfcShapeRepresentation:Items[binding="Items"]
}
```
