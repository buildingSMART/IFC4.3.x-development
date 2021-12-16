Project Representation Context
==============================

A project representation context indicates the coordinate system orientation, direction of true north, precision, and other values that apply to all geometry within a project or project library. A main geometric representation context is created for 3D model, and 2D representations, both can be further refined using geometric representation sub contexts.

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
    IfcAxis2Placement3D:Location -> IfcCartesianPoint
    IfcAxis2Placement3D:Axis -> IfcDirection_0
    IfcAxis2Placement3D:RefDirection -> IfcDirection_1
    IfcGeometricRepresentationSubContext:ContextIdentifier -> IfcLabel_2
    IfcGeometricRepresentationSubContext:ContextType -> IfcLabel_3
    IfcGeometricRepresentationSubContext:TargetScale -> IfcPositiveRatioMeasure
    IfcGeometricRepresentationSubContext:TargetView -> IfcGeometricProjectionEnum
    IfcGeometricRepresentationSubContext:UserDefinedTargetView -> IfcLabel_4
    IfcGeometricRepresentationContext:ContextIdentifier[binding="ContextIdentifier"]
    IfcGeometricRepresentationContext:ContextType[binding="ContextType"]
    IfcGeometricRepresentationSubContext:ContextIdentifier[binding="SubContextIdentifier"]
    IfcGeometricRepresentationSubContext:ContextType[binding="SubContextType"]
}
```
