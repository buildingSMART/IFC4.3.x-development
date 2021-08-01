Door Type Attributes
====================

Door types may be further described by their operation type.

```
concept {
    IfcDoorType:OperationType -> IfcDoorTypeOperationEnum
    IfcDoorType:UserDefinedOperationType -> IfcLabel
    IfcDoorType:HasPropertySets -> IfcDoorLiningProperties
    IfcDoorType:HasPropertySets -> IfcDoorPanelProperties
}
```
