# IfcEarthworksFill

A type of earthworks element created by earthwork activities to build subgrade or to raise the level of the ground in general.
<!-- end of short definition -->


## Attributes

### PredefinedType
Identifies the predefined type of a earthworks fill elements. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset, or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
