Coordinate Reference System in WKT
==================================

```
concept {
    IfcCoordinateReferenceSystem:WellKnownText -> IfcWellKnownText:CoordinateReferenceSystem
    IfcCoordinateReferenceSystem:Name -> IfcLabel_0
    IfcLabel_0 -> constraint_0
    constraint_0[label="='WKT'"]
    IfcWellKnownText:WellKnownText -> IfcWellKnownTextLiteral_0
    IfcCoordinateReferenceSystem:Name[binding="CRSName"]
    IfcCoordinateReferenceSystem:WellKnownText[binding="HasWKTDescription"]
    IfcWellKnownText:WellKnownText[binding="WKTLiteral"]
}
```
