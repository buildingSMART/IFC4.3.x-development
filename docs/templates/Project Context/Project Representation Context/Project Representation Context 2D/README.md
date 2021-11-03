Project Representation Context 2D
=================================

The main geometric representation context that is created for 2D representations, it can be further refined using geometric representation sub contexts for specific 2D contexts.

> NOTE&nbsp; The 2D shape representations with the representation identifier "FootPrint" are linked to the 2D geometric representation subset with context identifier "FootPrint" and context type "Plan".

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
    IfcAxis2Placement3D:Location -> IfcCartesianPoint
    IfcAxis2Placement3D:Axis -> IfcDirection
    IfcAxis2Placement3D:RefDirection -> IfcDirection
    IfcGeometricRepresentationSubContext:TargetScale -> IfcPositiveRatioMeasure
    IfcGeometricRepresentationSubContext:TargetView -> IfcGeometricProjectionEnum
    IfcGeometricRepresentationSubContext:UserDefinedTargetView -> IfcLabel
    IfcGeometricRepresentationSubContext:ContextIdentifier -> IfcLabel
    IfcGeometricRepresentationSubContext:ContextType -> IfcLabel
    IfcGeometricRepresentationContext:ContextIdentifier[binding="ContextIdentifier"]
    IfcGeometricRepresentationContext:ContextType[binding="ContextType"]
    IfcGeometricRepresentationSubContext:ContextIdentifier[binding="SubContextIdentifier"]
    IfcGeometricRepresentationSubContext:ContextType[binding="SubContextType"]
}
```
