Project Representation Context 3D
=================================

The main geometric representation context that is created for 3D representations, it can be further refined using geometric representation sub contexts for specific 3D contexts.

> NOTE&nbsp; The 3D shape representations with the representation identifier "Body" are linked to the 3D geometric representation subset with context identifier "Body" and context type "Model".

```
concept {
    IfcContext:RepresentationContexts -> IfcGeometricRepresentationContext
    IfcContext:Phase -> IfcLabel
    IfcContext:ObjectType -> IfcLabel
    IfcContext:LongName -> IfcLabel
    IfcGeometricRepresentationContext:ContextIdentifier -> IfcLabel
    IfcGeometricRepresentationContext:ContextType -> IfcLabel
    IfcGeometricRepresentationContext:CoordinateSpaceDimension -> IfcDimensionCount
    IfcGeometricRepresentationContext:WorldCoordinateSystem -> IfcAxis2Placement3D
    IfcGeometricRepresentationContext:TrueNorth -> IfcDirection
    IfcGeometricRepresentationContext:HasSubContexts -> IfcGeometricRepresentationSubContext:ParentContext
    IfcGeometricRepresentationContext:HasSubContexts -> IfcGeometricRepresentationSubContext:ParentContext
    IfcAxis2Placement3D:Location -> IfcCartesianPoint
    IfcAxis2Placement3D:Axis -> IfcDirection
    IfcAxis2Placement3D:RefDirection -> IfcDirection
    IfcGeometricRepresentationSubContext:TargetScale -> IfcPositiveRatioMeasure
    IfcGeometricRepresentationSubContext:TargetView -> IfcGeometricProjectionEnum
    IfcGeometricRepresentationSubContext:UserDefinedTargetView -> IfcLabel
    IfcGeometricRepresentationSubContext:ContextIdentifier -> IfcLabel
    IfcGeometricRepresentationSubContext:ContextType -> IfcLabel
}
```
