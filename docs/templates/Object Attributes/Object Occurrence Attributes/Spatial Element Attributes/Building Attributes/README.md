Building Attributes
===================

A building may be located according to a postal address, and may indicate a baseline elevation and land elevation.

```
concept {
    IfcBuilding:LongName -> IfcLabel
    IfcBuilding:Name -> IfcLabel
    IfcBuilding:CompositionType -> IfcElementCompositionEnum
    IfcBuilding:ElevationOfRefHeight -> IfcLengthMeasure
    IfcBuilding:ElevationOfTerrain -> IfcLengthMeasure
    IfcBuilding:BuildingAddress -> IfcPostalAddress
    IfcPostalAddress:Purpose -> IfcAddressTypeEnum
    IfcPostalAddress:Description -> IfcText
    IfcPostalAddress:UserDefinedPurpose -> IfcLabel
    IfcPostalAddress:InternalLocation -> IfcLabel
    IfcPostalAddress:AddressLines -> IfcLabel
    IfcPostalAddress:PostalBox -> IfcLabel
    IfcPostalAddress:Town -> IfcLabel
    IfcPostalAddress:Region -> IfcLabel
    IfcPostalAddress:PostalCode -> IfcLabel
    IfcPostalAddress:Country -> IfcLabel
    IfcBuilding:LongName[binding="LongName"]
    IfcBuilding:Name[binding="Name"]
    IfcBuilding:BuildingAddress[binding="HasAddress"]
    IfcPostalAddress:AddressLines[binding="AddressLines"]
    IfcPostalAddress:Town[binding="Town"]
    IfcPostalAddress:PostalCode[binding="PostalCode"]
    IfcPostalAddress:Country[binding="Country"]
}
```
