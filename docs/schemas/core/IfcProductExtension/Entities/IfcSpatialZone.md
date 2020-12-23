# IfcSpatialZone

A spatial zone is a non-hierarchical and potentially overlapping decomposition of the project under some functional consideration. A spatial zone might be used to represent a thermal zone, a construction zone, a lighting zone, a usable area zone. A spatial zone might have its independent placement and shape representation.

The _IfcSpatialZone_ inherits and declares these attributes that shall have the following meaning:

* _Name_: A number or designator provided by the user or system for the spatial element, e.g. a space number "1-003", could also be a running number provided by default by the application
* _LongName_: Name of the spatial element provided by the user, e.g. a space name "Office".
* _Description_: Any additional description provided by the user, e.g. a space description "Corner office with habour view".
* _ObjectType_: reserved for typing of spatial elements in case of _PredefinedType_ = .USERDEFINED., restrictions on applicable values might be published in view definitions or implementer agreements.

Physical elements that are referenced by this spatial zone are related using the _IfcRelReferencedInSpatialStructure_ relationship as it is a non-hierarchical assignment in addition to the hierarchical spatial containment within a subtype of _IfcSpatialStructureElement_. Also spaces, that referenced by this spatial zone are related using the _IfcRelReferencedInSpatialStructure_ relationship. The _IfcSpatialZone_ itself can also be referenced by another spatial element using _IfcRelReferencedInSpatialStructure_.

> NOTE&nbsp; The _IfcSpatialZone_ is different to the _IfcZone_ entity by allowing an own placement and shape representation, whereas _IfcZone_ is only a grouping of _IfcSpace_'s.

> HISTORY&nbsp; New entity in IFC4.

## Attributes

### PredefinedType
Predefined types to define the particular type of the spatial zone. There may be property set definitions available for each predefined type.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcSpatialZoneType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no spatial zone type object associated, then the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcSpatialZoneType_.
