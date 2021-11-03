Spatial Zone Attributes
=======================



```
concept {
    IfcSpatialZone:Name -> IfcLabel
    IfcSpatialZone:LongName -> IfcLabel
    IfcSpatialZone:IsTypedBy -> IfcRelDefinesByType
    IfcRelDefinesByType:RelatingType -> IfcSpatialZoneType
    IfcSpatialZoneType:LongName -> IfcLabel
    IfcSpatialZone:Name[binding="Name"]
    IfcSpatialZone:LongName[binding="LongName"]
}
```
