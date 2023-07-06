Spatial Service Connectivity
============================

A system, such as a distribution system, services a particular spatial structure, either an entire facility (and its specific subtypes e.g. buildings, bridges, roads, or marine facilities), a facility part, a building storey, or any part of these structures.
The system (_IfcSystem_) in question should be human identifiable by its _Name_ attribute.
The use of _IfcRelReferencedInSpatialStructure_ in this template provides the relationship across spatial and functional hierarchies allowing the spatial coverage of functional systems.

```
concept {
    IfcSpatialElement:ReferencedInStructures -> IfcRelReferencedInSpatialStructure:RelatingStructure
    IfcRelReferencedInSpatialStructure:RelatedElements -> IfcSystem
    IfcSystem:Name -> IfcLabel
    IfcSpatialElement:ReferencedInStructures[binding="ReferencedInStructures"]
    IfcRelReferencedInSpatialStructure:RelatedElements[binding="RelatedSystems"]
    IfcSystem:Name[binding="SystemName"]
}
```
