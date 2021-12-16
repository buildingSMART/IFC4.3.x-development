Door Attributes
===============

Doors may be further described by their size and operation type.

```
concept {
    IfcDoor:Tag -> IfcIdentifier
    IfcDoor:OverallHeight -> IfcPositiveLengthMeasure_0
    IfcDoor:OverallWidth -> IfcPositiveLengthMeasure_1
    IfcDoor:OperationType -> IfcDoorTypeOperationEnum_0
    IfcDoor:UserDefinedOperationType -> IfcLabel_0
    IfcDoor:IsTypedBy -> IfcRelDefinesByType:RelatedObjects
    IfcRelDefinesByType:RelatingType -> IfcDoorType
    IfcDoorType:OperationType -> IfcDoorTypeOperationEnum_1
    IfcDoorType:UserDefinedOperationType -> IfcLabel_1
    IfcDoorType:HasPropertySets -> IfcDoorLiningProperties
    IfcDoorType:HasPropertySets -> IfcDoorPanelProperties
    IfcDoorPanelProperties:PanelDepth -> IfcPositiveLengthMeasure_2
    IfcDoorPanelProperties:PanelOperation -> IfcDoorPanelOperationEnum
    IfcDoorPanelProperties:PanelWidth -> IfcNormalisedRatioMeasure
    IfcDoorPanelProperties:PanelPosition -> IfcDoorPanelPositionEnum
    IfcDoor:OverallHeight[binding="OverallHeight"]
    IfcDoor:OverallWidth[binding="OverallWidth"]
    IfcDoor:OperationType[binding="OperationType"]
    IfcDoorType:OperationType[binding="TypeOperationType"]
}
```
