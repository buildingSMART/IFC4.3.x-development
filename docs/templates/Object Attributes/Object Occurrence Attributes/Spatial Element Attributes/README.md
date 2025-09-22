Spatial Element Attributes
==========================

> NOTE: This template for attributes, like similar ones, originates from legacy requirements tied to mvdXML and an earlier era when MVD defined exchange information requirements. Such templates no longer add value to the specification, nor do they convey information beyond what is already defined in the schema. Additionally, some templates reference deprecated entities, potentially causing unnecessary confusion.
As part of a broader effort to clean up documentation, this and other non-essential templates will be removed in the next release.

Spatial objects may be further identified via the _LongName_ attribute. This value should generally correspond to building signage describing floor levels or rooms. While the _Name_ attribute generally provides a coded or abbreviated identifier, the _LongName_ provides a functional name for the location such as "Reception Area".

```
concept {
    IfcSpatialElement:Name -> IfcLabel_0
    IfcSpatialElement:LongName -> IfcLabel_1
    IfcSpatialElement:Name[binding="Name"]
    IfcSpatialElement:LongName[binding="LongName"]
}
```
