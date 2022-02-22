# IfcRelInterferesElements

The _IfcRelInterferesElements_ objectified relationship indicates that two elements interfere.
It is a 1 to 1 relationship, and the concept of two elements interfering physically or logically is described independently of the elements.

The interference may be related to the shape representation of the entities by providing an interference geometry or zone:
* when the interference is between two physical products, the _InterferenceGeometry_ attribute is used to define the physical interference shape, it can be part of the shape of one of the elements used in the relationship or define the interface between the two shapes using a _IfcConnectionGeometry_.
* when the interference is between two spatial objects, the _InterferenceSpace_ attribute is used to define the interference space between the two footprints associated to the spatial objects, expressed by a specific _IfcSpatialZone_ of predefined type _IfcSpatialZoneTypeEnum_ INTERFERENCE.

If the interference geometry and Zone are omitted then the interference is provided as a logical relationship. Under this circumstance, the connection point, curve, surface, or solid has to be recalculated by the receiving application.
Both _InterferenceGeometry_ and _InterferenceSpace_ should not be set together.

The _RelatingElement_ and _RelatedElement_ define the two elements in the relationship, that may have different roles.
The relation orientation may be required by certain _InterferenceType_ values or _InterferenceGeometry_ calculation, this is done by setting the attribute _ImpliedOrder_ accordingly:
* _ImpliedOrder_=TRUE The _RelatingElement_ constitutes the primary element of the interference relationship that is oriented from _RelatingElement_ (source) to _RelatedElement_ (target). If the interference is to be resolved by subtracting the overlapping part, it should be subtracted from the _RelatingElement_. The net result would be the _RelatingElement_ subtracted by the _InterferenceGeometry_. This would be the case in interference relationships where the _RelatedElement_ creates a void in the _RelatingElement_ dynamically.
* _ImpliedOrder_=FALSE The _RelatingElement_ and _RelatedElement_ have no priority among each other. If the interference is to be resolved then no information about whether the _InterferenceGeometry_ should be subtracted from the _RelatingElement_ or the _RelatedElement_ can be traced. This would be the case for clash detection results.
* _ImpliedOrder_=UNKNOWN No information about the priorities is provided.

The _InterferenceType_ property optionally specifies the type of interference between the two elements, two set of default types are provided:
* **Oriented interferences types** imply usage of _ImpliedOrder_ set to TRUE and specific choice of _RelatingElement_ and _RelatedElement_ to be meaningful:
  * Crosses: the _RelatingElement_ is crossing the _RelatedElement_ (e.g. Railway crossing a road)
  * PassesThrough: the _RelatingElement_ is passing through the _RelatedElement_ (e.g. a Road passing inside a tunnel)
  * PassesOver: the _RelatingElement_ is passing over the _RelatedElement_ (e.g a bridge passing over a water canal)
  * PassesUnder: the _RelatingElement_ is passing under the _RelatedElement_ (e.g a Tunnel passing under a road)
* **Non oriented interferences types** do not imply specific values of _ImpliedOrder_ (but can still be set to detail shape interference calculation)
  * Clash: The _RelatingElement_ and _RelatedElement_ have a spatial or shape-based clash
  * Along: The _RelatingElement_ and _RelatedElement_ have a common frontier/surface

> HISTORY  New entity in IFC4.

## Attributes

### RelatingElement


### RelatedElement


### InterferenceGeometry


### InterferenceSpace
Optional attribute that expresses the interfering space for _IfcSpatialElement_ occurrences.

### InterferenceType
Optional identifier that describes the nature of the interference.

### ImpliedOrder
Logical value indicating if the _RelatingElement_ is considered a source and the _RelatedElement_ a target (giving a formal orientation to the relation). It shall be provided in regards to _InterferenceGeometry_ usage and _InterferenceType_ declaration.

## Formal Propositions

### NoSelfReference
The instance of the _RelatingElement_ shall not be the same instance as the _RelatedElement_.
