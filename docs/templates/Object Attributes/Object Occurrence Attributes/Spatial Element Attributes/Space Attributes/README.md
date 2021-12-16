Space Attributes
================

Space may be further described by their elevation including floor coverings.

```
concept {
    IfcSpace:LongName -> IfcLabel_0
    IfcSpace:Name -> IfcLabel_1
    IfcSpace:CompositionType -> IfcElementCompositionEnum
    IfcSpace:ElevationWithFlooring -> IfcLengthMeasure
    IfcSpace:IsTypedBy -> IfcRelDefinesByType:RelatedObjects
    IfcRelDefinesByType:RelatingType -> IfcSpaceType
    IfcSpaceType:Name -> IfcLabel_2
    IfcSpaceType:LongName -> IfcLabel_3
    IfcSpace:LongName[binding="LongName"]
    IfcSpace:Name[binding="Name"]
    IfcSpaceType:Name[binding="TypeName"]
    IfcSpaceType:LongName[binding="TypeLongName"]
}
```
