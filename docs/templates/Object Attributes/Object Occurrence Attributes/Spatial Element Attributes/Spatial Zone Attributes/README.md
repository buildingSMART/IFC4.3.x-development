Spatial Zone Attributes
=======================



```
concept {
    IfcSpatialZone:Name -> IfcLabel_0
    IfcSpatialZone:LongName -> IfcLabel_1
    IfcSpatialZone:IsTypedBy -> IfcRelDefinesByType:RelatedObjects
    IfcRelDefinesByType:RelatingType -> IfcSpatialZoneType
    IfcSpatialZoneType:LongName -> IfcLabel_2
    IfcSpatialZone:Name[binding="Name"]
    IfcSpatialZone:LongName[binding="LongName"]
}
```
