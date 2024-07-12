# IfcEarthworksCut

The resulting void from modification of existing terrain or road structure by excavation or by other means of removing material.
<!-- end of short definition -->

> NOTE Definition from ISO 6707-1: void that results from bulk excavation of material.

> NOTE The material excavated and either used as fill or discarded as waste is not modelled as Cut, but may be handled as a different concept (Resource) in the future.

## Attributes

### PredefinedType
Identifies the predefined type of a earthworks cut elements. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset, or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
