Project Global Positioning
==========================

Adding a geospatial coordinate reference, using an recognized coordinate reference system, to the geometric representation context. It allows to position the project coordinate system on earth (normally using eastings, northings, elevation about datum, and orientation).

> HISTORY&nbsp; New concept template enabled by schema enhancements in IFC4.

```
concept {
    IfcContext:RepresentationContexts -> IfcGeometricRepresentationContext
    IfcContext:Phase -> IfcLabel
    IfcContext:ObjectType -> IfcLabel
    IfcContext:LongName -> IfcLabel
    IfcGeometricRepresentationContext:HasCoordinateOperation -> IfcMapConversion:SourceCRS
    IfcMapConversion:Eastings -> IfcLengthMeasure
    IfcMapConversion:Northings -> IfcLengthMeasure
    IfcMapConversion:OrthogonalHeight -> IfcLengthMeasure
    IfcMapConversion:XAxisAbscissa -> IfcReal
    IfcMapConversion:XAxisOrdinate -> IfcReal
    IfcMapConversion:Scale -> IfcReal
    IfcMapConversion:TargetCRS -> IfcProjectedCRS
    IfcProjectedCRS:Name -> IfcLabel
    IfcProjectedCRS:Description -> IfcText
    IfcProjectedCRS:GeodeticDatum -> IfcIdentifier
    IfcProjectedCRS:VerticalDatum -> IfcIdentifier
    IfcProjectedCRS:MapProjection -> IfcIdentifier
    IfcProjectedCRS:MapZone -> IfcIdentifier
    IfcGeometricRepresentationContext:HasCoordinateOperation[binding="HasGlobalPosition"]
    IfcMapConversion:Eastings[binding="Eastings"]
    IfcMapConversion:Northings[binding="Northings"]
    IfcMapConversion:OrthogonalHeight[binding="OrthogonalHeight"]
    IfcMapConversion:XAxisAbscissa[binding="XAxisAbscissa"]
    IfcMapConversion:XAxisOrdinate[binding="XAxisOrdinate"]
    IfcProjectedCRS:Name[binding="CRSName"]
}
```
