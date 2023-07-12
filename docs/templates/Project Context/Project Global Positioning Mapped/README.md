Project Global Positioning Mapped
=================================

```
concept {
    IfcProject:RepresentationContexts -> IfcGeometricRepresentationContext
    IfcProject:ObjectType -> IfcLabel_1
    IfcProject:LongName -> IfcLabel_2
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
