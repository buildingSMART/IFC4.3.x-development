Project Representation Context
==============================

A project representation context indicates the coordinate system orientation, direction of true north, precision, and other values that apply to all geometry within a project or project library. A main geometric representation context is created for 3D model, and 2D representations, both can be further refined using geometric representation sub contexts.

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
    IfcGeometricRepresentationSubContext:ContextIdentifier -> IfcLabel
    IfcGeometricRepresentationSubContext:ContextType -> IfcLabel
    IfcGeometricRepresentationSubContext:TargetScale -> IfcPositiveRatioMeasure
    IfcGeometricRepresentationSubContext:TargetView -> IfcGeometricProjectionEnum
    IfcGeometricRepresentationSubContext:UserDefinedTargetView -> IfcLabel
}
```
