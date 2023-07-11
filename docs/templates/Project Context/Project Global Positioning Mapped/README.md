Project Global Positioning Mapped
=================================

```
concept {
    IfcContext:RepresentationContexts -> IfcGeometricRepresentationContext
    IfcContext:Phase -> IfcLabel_1
    IfcContext:ObjectType -> IfcLabel_2
    IfcContext:LongName -> IfcLabel_3
    IfcGeometricRepresentationContext:HasCoordinateOperation -> IfcRigidOperation:SourceCRS
    IfcRigidOperation:FirstCoordinate -> IfcLengthMeasure_1
    IfcRigidOperation:SecondCoordinate -> IfcLengthMeasure_2
    IfcRigidOperation:Height -> IfcLengthMeasure_3
    IfcRigidOperation:TargetCRS -> IfcProjectedCRS
    IfcProjectedCRS:Name -> IfcLabel_0
    IfcGeometricRepresentationContext:HasCoordinateOperation[binding="HasGlobalPosition"]
    IfcRigidOperation:FirstCoordinate[binding="FirstCoordinate"]
    IfcRigidOperation:SecondCoordinate[binding="SecondCoordinate"]
    IfcRigidOperation:Height[binding="Height"]
    IfcProjectedCRS:Name[binding="CRSName"]
}
```
