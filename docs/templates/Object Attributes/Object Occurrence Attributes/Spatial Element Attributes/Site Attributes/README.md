Site Attributes
===============

> NOTE: This template for attributes, like similar ones, originates from legacy requirements tied to mvdXML and an earlier era when MVD defined exchange information requirements. Such templates no longer add value to the specification, nor do they convey information beyond what is already defined in the schema. Additionally, some templates reference deprecated entities, potentially causing unnecessary confusion.
As part of a broader effort to clean up documentation, this and other non-essential templates will be removed in the next release.

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
