Window Attributes
=================

> NOTE: This template for attributes, like similar ones, originates from legacy requirements tied to mvdXML and an earlier era when MVD defined exchange information requirements. Such templates no longer add value to the specification, nor do they convey information beyond what is already defined in the schema. Additionally, some templates reference deprecated entities, potentially causing unnecessary confusion.
As part of a broader effort to clean up documentation, this and other non-essential templates will be removed in the next release.

Windows may be further described by their size and partitioning type.

```
concept {
    IfcWindow:Tag -> IfcIdentifier
    IfcWindow:OverallHeight -> IfcPositiveLengthMeasure_0
    IfcWindow:OverallWidth -> IfcPositiveLengthMeasure_1
    IfcWindow:PartitioningType -> IfcWindowTypePartitioningEnum_0
    IfcWindow:UserDefinedPartitioningType -> IfcLabel_0
    IfcWindow:IsTypedBy -> IfcRelDefinesByType:RelatedObjects
    IfcRelDefinesByType:RelatingType -> IfcWindowType
    IfcWindowType:PartitioningType -> IfcWindowTypePartitioningEnum_1
    IfcWindowType:UserDefinedPartitioningType -> IfcLabel_1
    IfcWindowType:HasPropertySets -> IfcWindowLiningProperties
    IfcWindowType:HasPropertySets -> IfcWindowPanelProperties
    IfcWindowPanelProperties:OperationType -> IfcWindowPanelOperationEnum
    IfcWindowPanelProperties:PanelPosition -> IfcWindowPanelPositionEnum
    IfcWindow:OverallHeight[binding="OverallHeight"]
    IfcWindow:OverallWidth[binding="OverallWidth"]
    IfcWindow:PartitioningType[binding="PartitioningType"]
    IfcWindowType:PartitioningType[binding="TypePartitioningType"]
}
```
