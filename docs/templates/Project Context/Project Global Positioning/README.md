Project Global Positioning
==========================

Adding a geospatial coordinate reference to the geometric representation context using a recognized coordinate reference system (CRS). This allows to position the project coordinate system on Earth (normally using eastings, northings, elevation above horizontal and vertical datums, and orientation).

> HISTORY  New concept template enabled by schema enhancements in IFC4.

```
concept {
    IfcContext:RepresentationContexts -> IfcGeometricRepresentationContext
    IfcContext:Phase -> IfcLabel_1
    IfcContext:ObjectType -> IfcLabel_2
    IfcContext:LongName -> IfcLabel_3
    IfcGeometricRepresentationContext:HasCoordinateOperation -> IfcMapConversion:SourceCRS
    IfcMapConversion:Eastings -> IfcLengthMeasure_0
    IfcMapConversion:Northings -> IfcLengthMeasure_1
    IfcMapConversion:OrthogonalHeight -> IfcLengthMeasure_2
    IfcMapConversion:XAxisAbscissa -> IfcReal_0
    IfcMapConversion:XAxisOrdinate -> IfcReal_1
    IfcMapConversion:Scale -> IfcReal_2
    IfcMapConversion:TargetCRS -> IfcProjectedCRS
    IfcProjectedCRS:Name -> IfcLabel_0
    IfcProjectedCRS:Description -> IfcText
    IfcProjectedCRS:GeodeticDatum -> IfcIdentifier_0
    IfcProjectedCRS:VerticalDatum -> IfcIdentifier_1
    IfcProjectedCRS:MapProjection -> IfcIdentifier_2
    IfcProjectedCRS:MapZone -> IfcIdentifier_3
    IfcGeometricRepresentationContext:HasCoordinateOperation[binding="HasGlobalPosition"]
    IfcMapConversion:Eastings[binding="Eastings"]
    IfcMapConversion:Northings[binding="Northings"]
    IfcMapConversion:OrthogonalHeight[binding="OrthogonalHeight"]
    IfcMapConversion:XAxisAbscissa[binding="XAxisAbscissa"]
    IfcMapConversion:XAxisOrdinate[binding="XAxisOrdinate"]
    IfcProjectedCRS:Name[binding="CRSName"]
}
```
