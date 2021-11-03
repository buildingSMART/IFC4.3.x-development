Spatial Service Connectivity
============================

A system, such as a distribution system, services a particular spatial structure, either a total building, a building section, or a storey, or any part of these structures.

```
concept {
    IfcSpatialElement:ServicedBySystems -> IfcRelServicesBuildings:RelatedBuildings
    IfcRelServicesBuildings:RelatingSystem -> IfcSystem
    IfcSystem:Name -> IfcLabel
    IfcSpatialElement:ServicedBySystems[binding="ServicedBySystems"]
    IfcRelServicesBuildings:RelatingSystem[binding="RelatedSystem"]
    IfcSystem:Name[binding="SystemName"]
}
```
