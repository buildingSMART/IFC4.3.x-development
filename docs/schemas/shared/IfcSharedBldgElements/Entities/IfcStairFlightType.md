# IfcStairFlightType

The building element type _IfcStairFlightType_ defines commonly shared information for occurrences of stair flights. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements

It is used to define a stair flight type specification indicating the specific product information that is common to all occurrences of that product type. The _IfcStairFlightType_ may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of _IfcStairFlightType_ are represented by instances of _IfcStairFlight_. Refer to the documentation at _IfcStairFlight_ for supported property sets, materials, and composition.

> HISTORY&nbsp; New entity in IFC2x2.

## Attributes

### PredefinedType
Identifies the predefined types of a stair flight element from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

## Concepts

### Body Geometry


