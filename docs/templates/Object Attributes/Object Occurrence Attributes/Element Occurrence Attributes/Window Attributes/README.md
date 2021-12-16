Window Attributes
=================

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
