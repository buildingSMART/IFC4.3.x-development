Space Attributes
================

> NOTE: This template for attributes, like similar ones, originates from legacy requirements tied to mvdXML and an earlier era when MVD defined exchange information requirements. Such templates no longer add value to the specification, nor do they convey information beyond what is already defined in the schema. Additionally, some templates reference deprecated entities, potentially causing unnecessary confusion.
As part of a broader effort to clean up documentation, this and other non-essential templates will be removed in the next release.

Space may be further described by their elevation including floor coverings.

```
concept {
    IfcSpace:LongName -> IfcLabel_0
    IfcSpace:Name -> IfcLabel_1
    IfcSpace:CompositionType -> IfcElementCompositionEnum
    IfcSpace:ElevationWithFlooring -> IfcLengthMeasure
    IfcSpace:IsTypedBy -> IfcRelDefinesByType:RelatedObjects
    IfcRelDefinesByType:RelatingType -> IfcSpaceType
    IfcSpaceType:Name -> IfcLabel_2
    IfcSpaceType:LongName -> IfcLabel_3
    IfcSpace:LongName[binding="LongName"]
    IfcSpace:Name[binding="Name"]
    IfcSpaceType:Name[binding="TypeName"]
    IfcSpaceType:LongName[binding="TypeLongName"]
}
```
