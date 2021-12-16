Storey Attributes
=================

A building storey may be indicate the elevation of the top surface of the floor slab, excluding any floor coverings. For storeys with raised or sunken areas, the elevation should reflect the largest area of the slab. For split-level buildings, each level should have it's own _IfcBuildingStorey_.

```
concept {
    IfcBuildingStorey:LongName -> IfcLabel_0
    IfcBuildingStorey:Name -> IfcLabel_1
    IfcBuildingStorey:CompositionType -> IfcElementCompositionEnum
    IfcBuildingStorey:Elevation -> IfcLengthMeasure
    IfcBuildingStorey:LongName[binding="LongName"]
    IfcBuildingStorey:Name[binding="Name"]
    IfcBuildingStorey:Elevation[binding="Elevation"]
}
```
