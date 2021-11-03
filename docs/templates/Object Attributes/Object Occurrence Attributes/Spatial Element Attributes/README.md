Spatial Element Attributes
==========================

Spatial objects may be further identified via the _LongName_ attribute. This value should generally correspond to building signage describing floor levels or rooms. While the _Name_ attribute generally provides a coded or abbreviated identifier, the _LongName_ provides a functional name for the location such as "Reception Area".

```
concept {
    IfcSpatialElement:Name -> IfcLabel
    IfcSpatialElement:LongName -> IfcLabel
    IfcSpatialElement:Name[binding="Name"]
    IfcSpatialElement:LongName[binding="LongName"]
}
```
