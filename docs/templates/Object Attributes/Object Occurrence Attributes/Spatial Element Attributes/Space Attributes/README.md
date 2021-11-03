Space Attributes
================

Space may be further described by their elevation including floor coverings.

```
concept {
    IfcSpace:LongName -> IfcLabel
    IfcSpace:Name -> IfcLabel
    IfcSpace:CompositionType -> IfcElementCompositionEnum
    IfcSpace:ElevationWithFlooring -> IfcLengthMeasure
    IfcSpace:IsTypedBy -> IfcRelDefinesByType
    IfcRelDefinesByType:RelatingType -> IfcSpaceType
    IfcSpaceType:Name -> IfcLabel
    IfcSpaceType:LongName -> IfcLabel
    IfcSpace:LongName[binding="LongName"]
    IfcSpace:Name[binding="Name"]
    IfcSpaceType:Name[binding="TypeName"]
    IfcSpaceType:LongName[binding="TypeLongName"]
}
```
