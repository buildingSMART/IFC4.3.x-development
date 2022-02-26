Site Attributes
===============

A site may be located according to latitude, longitude, elevation, land title designation, and/or postal address.

```
concept {
    IfcSite:LongName -> IfcLabel_0
    IfcSite:Name -> IfcLabel_1
    IfcSite:CompositionType -> IfcElementCompositionEnum
    IfcSite:LandTitleNumber -> IfcLabel_2
    IfcSite:RefLatitude -> IfcCompoundPlaneAngleMeasure_0
    IfcSite:RefLongitude -> IfcCompoundPlaneAngleMeasure_1
    IfcSite:RefElevation -> IfcLengthMeasure
    IfcSite:SiteAddress -> IfcPostalAddress
    IfcPostalAddress:Purpose -> IfcAddressTypeEnum
    IfcPostalAddress:Description -> IfcText
    IfcPostalAddress:InternalLocation -> IfcLabel_3
    IfcPostalAddress:AddressLines -> IfcLabel_4
    IfcPostalAddress:PostalBox -> IfcLabel_5
    IfcPostalAddress:Town -> IfcLabel_6
    IfcPostalAddress:Region -> IfcLabel_7
    IfcPostalAddress:PostalCode -> IfcLabel_8
    IfcPostalAddress:Country -> IfcLabel_9
    IfcPostalAddress:UserDefinedPurpose -> IfcLabel_10
    IfcSite:LongName[binding="LongName"]
    IfcSite:Name[binding="Name"]
    IfcSite:RefLatitude[binding="Latitude"]
    IfcSite:RefLongitude[binding="Longitude"]
    IfcSite:RefElevation[binding="Elevation"]
    IfcSite:SiteAddress[binding="HasAddress"]
}
```
