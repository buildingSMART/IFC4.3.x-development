# IfcMarineFacility

A marine facility represents any major structure or entity that is specific to the ports and waterways domain. examples of this include quays, jetties, shipyards, breakwaters etc.

## Attributes

### PredefinedType
Identifies the predefined type of a marine facility. This type may associate additional specific property sets.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset, or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
