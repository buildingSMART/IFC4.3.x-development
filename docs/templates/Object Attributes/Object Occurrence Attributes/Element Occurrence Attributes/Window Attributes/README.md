Window Attributes
=================

Windows may be further described by their size and partitioning type.

```
concept {
    IfcWindow:Tag -> IfcIdentifier
    IfcWindow:OverallHeight -> IfcPositiveLengthMeasure
    IfcWindow:OverallWidth -> IfcPositiveLengthMeasure
    IfcWindow:PartitioningType -> IfcWindowTypePartitioningEnum
    IfcWindow:UserDefinedPartitioningType -> IfcLabel
    IfcWindow:IsTypedBy -> IfcRelDefinesByType
    IfcRelDefinesByType:RelatingType -> IfcWindowType
    IfcWindowType:PartitioningType -> IfcWindowTypePartitioningEnum
    IfcWindowType:UserDefinedPartitioningType -> IfcLabel
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
