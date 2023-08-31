Group Spatial Connectivity
==========================

The concept of Group Spatial Connectivity allows for the association of a _IfcGroup_ (and its relevant subtypes) representing a grouping of objects to a particular spatial structure, either an entire facility (and its specific subtypes e.g. buildings, bridges, roads, or marine facilities), a facility part, a building storey, or any part of these structures.

The group (_IfcGroup_) in question should be human identifiable by its _Name_ attribute.

The relationship (_IfcRelReferencedInSpatialStructure_) in question can provide context of the connection through the _Name_ and _Description_ attributes.

The use of _IfcRelReferencedInSpatialStructure_ in this template provides the relationship across spatial and functional hierarchies allowing the spatial coverage of functional groups.

It is permissible for an _IfcGroup_ not to be related to any spatial structure element. When the _IfcGroup_ is **not** connected to the spatial structure it must be declared to the _IfcProject_ using the _Project declaration template_ via the IfcRelDeclares relationship, or have a parent _IfcGroup_ (or its relevant subtypes) through the use of composition, with said parent _IfcGroup_ either connected to the spatial structure using _Group Spatial Connectivity_ or declared to the _IfcProject_ using the _Project declaration template_.

> NOTE IfcRelReferencedInSpatialStructure is also used in the template _Spatial Service Connectivity_ to relate IfcSystem (subtype of IfcGroup) and can also be used for referencing IfcProduct as part of its _RelatedElements_.

```
concept {
    IfcSpatialElement:ReferencesElements -> IfcRelReferencedInSpatialStructure:RelatingStructure
    IfcRelReferencedInSpatialStructure:RelatedElements -> IfcGroup:ReferencedInStructures
    IfcRelReferencedInSpatialStructure:Name -> IfcLabel_1
    IfcGroup:Name -> IfcLabel_0
    IfcSpatialElement:ReferencesElements[binding="ReferencedElements"]
    IfcRelReferencedInSpatialStructure:RelatedElements[binding="RelatedGroups"]
    IfcGroup:Name[binding="GroupName"]
    IfcRelReferencedInSpatialStructure:Name[binding="ReferenceContext"]
}
```
