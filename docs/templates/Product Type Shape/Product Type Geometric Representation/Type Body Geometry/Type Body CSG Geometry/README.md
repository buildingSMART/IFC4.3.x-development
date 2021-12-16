Type Body CSG Geometry
======================



```
concept {
    IfcTypeProduct:RepresentationMaps -> IfcRepresentationMap
    IfcRepresentationMap:MappedRepresentation -> IfcShapeRepresentation
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement3D
    IfcRepresentationMap:MappingOrigin -> IfcAxis2Placement2D
    IfcShapeRepresentation:ContextOfItems -> IfcGeometricRepresentationContext
    IfcShapeRepresentation:RepresentationIdentifier -> IfcLabel_0
    IfcShapeRepresentation:RepresentationType -> IfcLabel_1
    IfcShapeRepresentation:Items -> IfcCsgSolid
    IfcShapeRepresentation:Items -> IfcBlock
    IfcShapeRepresentation:Items -> IfcRectangularPyramid
    IfcShapeRepresentation:Items -> IfcRightCircularCone
    IfcShapeRepresentation:Items -> IfcRightCircularCylinder
    IfcShapeRepresentation:Items -> IfcSphere
    IfcCsgSolid:TreeRootExpression -> IfcBooleanResult
    IfcBooleanResult:Operator -> IfcBooleanOperator
    IfcBooleanResult:FirstOperand -> IfcBooleanOperand_0
    IfcBooleanResult:SecondOperand -> IfcBooleanOperand_1
    IfcShapeRepresentation:RepresentationType[binding="RepresentationType"]
    IfcShapeRepresentation:Items[binding="Geometry"]
}
```
