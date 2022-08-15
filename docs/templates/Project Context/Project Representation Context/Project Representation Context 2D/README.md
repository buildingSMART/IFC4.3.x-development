Project Representation Context 2D
=================================

The main geometric representation context that is created for 2D representations, it can be further refined using geometric representation sub contexts for specific 2D contexts.

> NOTE  The 2D shape representations with the representation identifier "FootPrint" are linked to the 2D geometric representation subset with context identifier "FootPrint" and context type "Plan".

```
concept {
    IfcContext:RepresentationContexts -> IfcGeometricRepresentationContext
    IfcContext:Phase -> IfcLabel_5
    IfcContext:ObjectType -> IfcLabel_6
    IfcContext:LongName -> IfcLabel_7
    IfcGeometricRepresentationContext:ContextIdentifier -> IfcLabel_0
    IfcGeometricRepresentationContext:ContextType -> IfcLabel_1
    IfcGeometricRepresentationContext:CoordinateSpaceDimension -> IfcDimensionCount
    IfcGeometricRepresentationContext:WorldCoordinateSystem -> IfcAxis2Placement3D
    IfcGeometricRepresentationContext:TrueNorth -> IfcDirection_2
    IfcGeometricRepresentationContext:HasSubContexts -> IfcGeometricRepresentationSubContext:ParentContext
    IfcDimensionCount -> constraint_0
    constraint_0[label="=2"]
    IfcAxis2Placement3D:Location -> IfcCartesianPoint
    IfcAxis2Placement3D:Axis -> IfcDirection_0
    IfcAxis2Placement3D:RefDirection -> IfcDirection_1
    IfcGeometricRepresentationSubContext:TargetScale -> IfcPositiveRatioMeasure
    IfcGeometricRepresentationSubContext:TargetView -> IfcGeometricProjectionEnum
    IfcGeometricRepresentationSubContext:UserDefinedTargetView -> IfcLabel_2
    IfcGeometricRepresentationSubContext:ContextIdentifier -> IfcLabel_3
    IfcGeometricRepresentationSubContext:ContextType -> IfcLabel_4
    IfcGeometricRepresentationContext:ContextIdentifier[binding="ContextIdentifier"]
    IfcGeometricRepresentationContext:ContextType[binding="ContextType"]
    IfcGeometricRepresentationSubContext:ContextIdentifier[binding="SubContextIdentifier"]
    IfcGeometricRepresentationSubContext:ContextType[binding="SubContextType"]
}
```
