Spatial Interference With Zones
===============================

The _Spatial Interference with Zone_ concept is an extension of the _Spatial Interference_ concept which defines the relationship of spatial elements, such as facilities (_IfcFacility_ & specialised subtypes) or facility parts (_IfcFacilityPart_ with domain specific predefined types) that interfere or interface with other spatial elements across discipline spatial hierarchy branches, and extends the dataset with a related interference _IfcSpatialZone_ via the _IfcRelInterferesElements.InterferenceSpace_ attribute. The realizing _IfcSpatialZone_ should always have the _PredefinedType_ value set to _INTERFERENCE_.

The addition of a realizing _IfcSpatialZone_ extends the functionality of this relationship with the following:

- The ability to attach property sets to the co-engineering (or interference) zone.
- Allows explicit definition of the shared footprint or body geometry representing the zone where the _IfcSpatialElement_ entities interfere, without impacting the footprint or body geometry of the interfering _IfcSpatialElement_ entities.
- Products are still positioned within the domain spatial structure and can use relative positioning.

The _Spatial Interference with Zone_ concept is defined to cover complex use cases where the interference results in co-engineering zones where multiple teams have to collaborate within the same spatial area while maintaining ownership and rights over their domain elements. A common example of this is a level crossing between a railway and a road. The road and railway hierarchies each have a segment that relates to the level crossing and an _IfcRelInterferesElements_ relationship is defined to encode this connection. The relationship is then extended with an _IfcSpatialZone_ that defines the co-engineering zone and specific overlapping footprint or body geometry. Property sets can then be attached to the _IfcSpatialZone_ and the explicit footprint or body geometry can be utilised for automated clash and cross domain approval/notification of model updates.

```
concept {
    IfcSpatialElement_0:InterferesElements -> IfcRelInterferesElements:RelatingElement
    IfcSpatialElement_0:Name -> IfcLabel_1
    IfcRelInterferesElements:RelatedElement -> IfcSpatialElement_1
    IfcRelInterferesElements:InterferenceType -> IfcIdentifier
    IfcRelInterferesElements:InterferenceSpace -> IfcSpatialZone
    IfcSpatialElement_1:Name -> IfcLabel_0
    IfcSpatialZone:PredefinedType -> IfcSpatialZoneTypeEnum
    IfcSpatialZoneTypeEnum -> constraint_0
    constraint_0[label="=INTERFERENCE"]
    IfcSpatialElement_0:InterferesElements[binding="InterferesSpatialElements"]
    IfcRelInterferesElements:RelatedElement[binding="RelatedSpatialElement"]
    IfcSpatialElement_1:Name[binding="RelatedSpatialElementName"]
    IfcRelInterferesElements:InterferenceType[binding="InterferenceType"]
    IfcRelInterferesElements:InterferenceSpace[binding="InteferenceZone"]
    IfcSpatialZone:PredefinedType[binding="SpatialZoneType"]
    IfcSpatialElement_0:Name[binding="SpatialElementName"]
}
```
