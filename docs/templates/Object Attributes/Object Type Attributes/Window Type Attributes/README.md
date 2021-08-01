Window Type Attributes
======================

Window types may be further described by their partitioning type.

```
concept {
    IfcWindowType:PartitioningType -> IfcWindowTypePartitioningEnum
    IfcWindowType:UserDefinedPartitioningType -> IfcLabel
    IfcWindowType:HasPropertySets -> IfcWindowLiningProperties
    IfcWindowType:HasPropertySets -> IfcWindowPanelProperties
}
```
