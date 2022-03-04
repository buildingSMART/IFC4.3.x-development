Project Representation Context 3D
=================================

The main geometric representation context that is created for 3D representations, it can be further refined using geometric representation sub contexts for specific 3D contexts.

> NOTE  The 3D shape representations with the representation identifier "Body" are linked to the 3D geometric representation subset with context identifier "Body" and context type "Model".

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
    IfcGeometricRepresentationContext:HasSubContexts -> IfcGeometricRepresentationSubContext_0:ParentContext
    IfcGeometricRepresentationContext:HasSubContexts -> IfcGeometricRepresentationSubContext_1:ParentContext
    IfcDimensionCount -> constraint_0
    constraint_0[label="=3"]
    IfcAxis2Placement3D:Location -> IfcCartesianPoint
    IfcAxis2Placement3D:Axis -> IfcDirection_0
    IfcAxis2Placement3D:RefDirection -> IfcDirection_1
    IfcGeometricRepresentationSubContext_0:TargetScale -> IfcPositiveRatioMeasure
    IfcGeometricRepresentationSubContext_0:TargetView -> IfcGeometricProjectionEnum
    IfcGeometricRepresentationSubContext_0:UserDefinedTargetView -> IfcLabel_2
    IfcGeometricRepresentationSubContext_0:ContextIdentifier -> IfcLabel_3
    IfcGeometricRepresentationSubContext_0:ContextType -> IfcLabel_4
    IfcGeometricRepresentationContext:ContextIdentifier[binding="ContextIdentifier"]
    IfcGeometricRepresentationContext:ContextType[binding="ContextType"]
    IfcGeometricRepresentationSubContext_0:ContextIdentifier[binding="SubContextIdentifier"]
    IfcGeometricRepresentationSubContext_0:ContextType[binding="SubContextType"]
}
```
