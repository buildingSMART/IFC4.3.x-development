Project Global Positioning Geodetic
===================================

```
concept {
    IfcProject:RepresentationContexts -> IfcGeometricRepresentationContext
    IfcProject:ObjectType -> IfcLabel_1
    IfcProject:LongName -> IfcLabel_2
    IfcGeometricRepresentationContext:HasCoordinateOperation -> IfcRigidOperation:SourceCRS
    IfcRigidOperation:FirstCoordinate -> IfcPlaneAngleMeasure_1
    IfcRigidOperation:SecondCoordinate -> IfcPlaneAngleMeasure_2
    IfcRigidOperation:Height -> IfcLengthMeasure_1
    IfcRigidOperation:TargetCRS -> IfcGeographicCRS
    IfcGeographicCRS:Name -> IfcLabel_0
    IfcGeometricRepresentationContext:HasCoordinateOperation[binding="HasGlobalPosition"]
    IfcRigidOperation:FirstCoordinate[binding="FirstCoordinate"]
    IfcRigidOperation:SecondCoordinate[binding="SecondCoordinate"]
    IfcRigidOperation:Height[binding="Height"]
    IfcGeographicCRS:Name[binding="CRSName"]
}
```
