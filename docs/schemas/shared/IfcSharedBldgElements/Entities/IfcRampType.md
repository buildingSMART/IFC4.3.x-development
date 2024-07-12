# IfcRampType

The building element type _IfcRampType_ defines commonly shared information for occurrences of ramps. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
<!-- end of short definition -->

It is used to define a ramp type specification indicating the specific product information that is common to all occurrences of that product type. The _IfcRampType_ may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of _IfcRampType_ are represented by instances of _IfcRamp_. Refer to the documentation at _IfcRamp_ for supported property sets, materials, and composition.

> HISTORY New entity in IFC4.

## Attributes

### PredefinedType
Identifies the predefined types of a ramp element from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

## Concepts

### Type Body Geometry



