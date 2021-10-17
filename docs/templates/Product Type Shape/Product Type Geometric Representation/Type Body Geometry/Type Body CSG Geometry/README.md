Type Body CSG Geometry
======================



```
concept {
    IfcTypeProduct:RepresentationMaps -> IfcRepresentationMap
    IfcRepresentationMap:MappedRepresentation -> IfcShapeRepresentation
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement3D
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement2D
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel
    IfcShapeRepresentation:RepresentationType -> IfcLabel
    IfcShapeRepresentation:Items -> IfcCsgSolid
    IfcShapeRepresentation:Items -> IfcBlock
    IfcShapeRepresentation:Items -> IfcRectangularPyramid
    IfcShapeRepresentation:Items -> IfcRightCircularCone
    IfcShapeRepresentation:Items -> IfcRightCircularCylinder
    IfcShapeRepresentation:Items -> IfcSphere
    IfcCsgSolid:TreeRootExpression -> IfcBooleanResult
    IfcBooleanResult:Operator -> IfcBooleanOperator
    IfcBooleanResult:FirstOperand -> IfcBooleanOperand
    IfcBooleanResult:SecondOperand -> IfcBooleanOperand
}
```
