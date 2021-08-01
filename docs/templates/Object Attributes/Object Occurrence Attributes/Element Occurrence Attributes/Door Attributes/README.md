Door Attributes
===============

Doors may be further described by their size and operation type.

```
concept {
    IfcDoor:Tag -> IfcIdentifier
    IfcDoor:OverallHeight -> IfcPositiveLengthMeasure
    IfcDoor:OverallWidth -> IfcPositiveLengthMeasure
    IfcDoor:OperationType -> IfcDoorTypeOperationEnum
    IfcDoor:UserDefinedOperationType -> IfcLabel
    IfcDoor:IsTypedBy -> IfcRelDefinesByType
    IfcRelDefinesByType:RelatingType -> IfcDoorType
    IfcDoorType:OperationType -> IfcDoorTypeOperationEnum
    IfcDoorType:UserDefinedOperationType -> IfcLabel
    IfcDoorType:HasPropertySets -> IfcDoorLiningProperties
    IfcDoorType:HasPropertySets -> IfcDoorPanelProperties
    IfcDoorPanelProperties:PanelDepth -> IfcPositiveLengthMeasure
    IfcDoorPanelProperties:PanelOperation -> IfcDoorPanelOperationEnum
    IfcDoorPanelProperties:PanelWidth -> IfcNormalisedRatioMeasure
    IfcDoorPanelProperties:PanelPosition -> IfcDoorPanelPositionEnum
}
```
