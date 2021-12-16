Building Attributes
===================

A building may be located according to a postal address, and may indicate a baseline elevation and land elevation.

```
concept {
    IfcBuilding:LongName -> IfcLabel_0
    IfcBuilding:Name -> IfcLabel_1
    IfcBuilding:CompositionType -> IfcElementCompositionEnum
    IfcBuilding:ElevationOfRefHeight -> IfcLengthMeasure_0
    IfcBuilding:ElevationOfTerrain -> IfcLengthMeasure_1
    IfcBuilding:BuildingAddress -> IfcPostalAddress
    IfcPostalAddress:Purpose -> IfcAddressTypeEnum
    IfcPostalAddress:Description -> IfcText
    IfcPostalAddress:UserDefinedPurpose -> IfcLabel_2
    IfcPostalAddress:InternalLocation -> IfcLabel_3
    IfcPostalAddress:AddressLines -> IfcLabel_4
    IfcPostalAddress:PostalBox -> IfcLabel_5
    IfcPostalAddress:Town -> IfcLabel_6
    IfcPostalAddress:Region -> IfcLabel_7
    IfcPostalAddress:PostalCode -> IfcLabel_8
    IfcPostalAddress:Country -> IfcLabel_9
    IfcBuilding:LongName[binding="LongName"]
    IfcBuilding:Name[binding="Name"]
    IfcBuilding:BuildingAddress[binding="HasAddress"]
    IfcPostalAddress:AddressLines[binding="AddressLines"]
    IfcPostalAddress:Town[binding="Town"]
    IfcPostalAddress:PostalCode[binding="PostalCode"]
    IfcPostalAddress:Country[binding="Country"]
}
```
