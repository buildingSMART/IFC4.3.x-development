Site Attributes
===============

A site may be located according to latitute, longitute, elevation, land title designation, and/or postal address.

```
concept {
    IfcSite:LongName -> IfcLabel
    IfcSite:Name -> IfcLabel
    IfcSite:CompositionType -> IfcElementCompositionEnum
    IfcSite:LandTitleNumber -> IfcLabel
    IfcSite:RefLatitude -> IfcCompoundPlaneAngleMeasure
    IfcSite:RefLongitude -> IfcCompoundPlaneAngleMeasure
    IfcSite:RefElevation -> IfcLengthMeasure
    IfcSite:SiteAddress -> IfcPostalAddress
    IfcPostalAddress:Purpose -> IfcAddressTypeEnum
    IfcPostalAddress:Description -> IfcText
    IfcPostalAddress:InternalLocation -> IfcLabel
    IfcPostalAddress:AddressLines -> IfcLabel
    IfcPostalAddress:PostalBox -> IfcLabel
    IfcPostalAddress:Town -> IfcLabel
    IfcPostalAddress:Region -> IfcLabel
    IfcPostalAddress:PostalCode -> IfcLabel
    IfcPostalAddress:Country -> IfcLabel
    IfcPostalAddress:UserDefinedPurpose -> IfcLabel
}
```
