Spatial Interference
====================

The _Spatial Interference_ concept defines the relationship of spatial elements, such as facilities (_IfcFacility_ & specialised subtypes) or facility parts (_IfcFacilityPart_ with domain specific predefined types) that interfere or interface with other spatial elements across discipline spatial hierarchy branches. The _IfcSpatialElement_ entities should be identifiable by their _IfcSpatialElement.Name_ attribute and an optional _IfcRelInterferesElements.InterferenceType_ should be included to describe the nature of the interface or interference.

A simple example is a project that contains a road or railway development that includes a bridge section. _IfcRelInterferesElements_ is used to semantically link the spatial segments of the road or railway that pass over the bridge or bridge segments with the relevant interference type specified. This semantic relationship provides an easily queryable connection to identify the spatial elements that require consideration across disciplines such as the road design team and bridge design team. How the spatial hierarchy is organised is up to the user and project in question.

```
concept {
    IfcSpatialElement_0:InterferesElements -> IfcRelInterferesElements:RelatingElement
    IfcSpatialElement_0:Name -> IfcLabel_1
    IfcRelInterferesElements:RelatedElement -> IfcSpatialElement_1
    IfcRelInterferesElements:InterferenceType -> IfcIdentifier
    IfcSpatialElement_1:Name -> IfcLabel_0
    IfcSpatialElement_0:InterferesElements[binding="InterferesSpatialElements"]
    IfcRelInterferesElements:RelatedElement[binding="RelatedSpatialElement"]
    IfcSpatialElement_1:Name[binding="RelatedSpatialElementName"]
    IfcRelInterferesElements:InterferenceType[binding="InterferenceType"]
    IfcSpatialElement_0:Name[binding="SpatialElementName"]
}
```
