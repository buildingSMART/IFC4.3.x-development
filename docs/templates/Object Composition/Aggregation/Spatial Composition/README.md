Spatial Composition
===================

Provision of a spatial structure of the project by aggregating spatial elements. The spatial structure is a hierarchical tree of spatial elements ultimately assigned to the project. Composition refers to the relationship to a higher level element (e.g. this storey is part of a building or this road segment is part of a road).

> NOTE&nbsp; The link between the highest level spatial element(s) and the project is provided by this concept through _IfcRelAggregates_ and not through declaration using _IfcRelDeclares_. This is a known anomaly introduced to maintain compatibility with earlier versions of this standard.

The project spatial structure may be made up of a selection of different spatial structure elements with the most generic and simplest form from high to low level as follows: _IfcProject_, _IfcSite_, _IfcFacility_ (or any of its subtypes), _IfcFacilityPart_ (or _IfcBuildingStorey in the case of buildings), and _IfcSpace_ with _IfcSite_, _FacilityPart_ and _IfcSpace_ being optional levels. Therefore a spatial structure element should only be part of an element at the same or higher level, with the exception of _IfcFacility_ which can be part of an _IfcFacilityPart_ to allow for the regional or longitudinal division of a higjh level facility in to sections which can then contain one or more smaller functional facilities.

Where possible the relevant subtype of _IfcFacility_ should be used to describe the spatial structure element in question. When a adequate subtype of _IfcFacility_ with predefined or user defined type is not available the higher level, generic _IfcFacility_ entity can be instantiated with the relevant and agreed typing identifier defined in _IfcFacility.ObjectType_. This allows for nearly full coverage of built environment domains and/or scenarios that have yet to be addressed with specific extensions.

In addition to the identified spatial structure elements _IfcSpatialZone_ can be used to provide cross domain or functional zones within a project, these elements are included into the hierarchy using the _Spatial Containment_ concept (_IfcRelContainedInSpatialStructure_) and can be aggregated into a functional hierarchy in the same manner as other spatial structure elements with the constraint that an _IfcSpatialZone_ can only composed under another _IfcSpatialZone_.

```
concept {
    IfcSpatialElement_0:Decomposes -> IfcRelAggregates:RelatedObjects
    IfcRelAggregates:RelatingObject -> IfcProject
    IfcRelAggregates:RelatingObject -> IfcSpatialElement_1
    IfcProject:Name -> IfcLabel_0
    IfcSpatialElement_1:Name -> IfcLabel_1
    IfcRelAggregates:RelatingObject[binding="RelatingObject"]
    IfcProject:Name[binding="ProjectName"]
    IfcSpatialElement_1:Name[binding="SpatialElementName"]
}
```
