Spatial Zone Attributes
=======================

> NOTE: This template for attributes, like similar ones, originates from legacy requirements tied to mvdXML and an earlier era when MVD defined exchange information requirements. Such templates no longer add value to the specification, nor do they convey information beyond what is already defined in the schema. Additionally, some templates reference deprecated entities, potentially causing unnecessary confusion.
As part of a broader effort to clean up documentation, this and other non-essential templates will be removed in the next release.

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
