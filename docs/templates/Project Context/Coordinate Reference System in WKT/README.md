Coordinate Reference System in WKT
==================================

```
concept {
    IfcContext:RepresentationContexts -> IfcGeometricRepresentationContext
    IfcContext:Phase -> IfcLabel_1
    IfcContext:ObjectType -> IfcLabel_2
    IfcContext:LongName -> IfcLabel_3
    IfcGeometricRepresentationContext:HasCoordinateOperation -> IfcCoordinateOperation:SourceCRS
    IfcCoordinateOperation:TargetCRS -> IfcCoordinateReferenceSystem
    IfcCoordinateReferenceSystem:WellKnownText -> IfcWellKnownText:CoordinateReferenceSystem
    IfcCoordinateReferenceSystem:Name -> IfcLabel_0
    IfcWellKnownText:WellKnownText -> IfcWellKnownTextLiteral_0
    IfcGeometricRepresentationContext:HasCoordinateOperation[binding="HasGlobalPosition"]
    IfcCoordinateReferenceSystem:Name[binding="CRSName"]
    IfcCoordinateReferenceSystem:WellKnownText[binding="HasWKTDescription"]
    IfcWellKnownText:WellKnownText[binding="WKTLiteral"]
}
```
