# IfcRoofType

The building element type _IfcRoofType_ defines commonly shared information for occurrences of roofs. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements

<!-- end of short definition -->

It is used to define a roof type specification indicating the specific product information that is common to all occurrences of that product type. The _IfcRoofType_ may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of _IfcRoofType_ are represented by instances of _IfcRoof_. Refer to the documentation at _IfcRoof_ for supported property sets, materials, and composition.

> HISTORY New entity in IFC4.

## Attributes

### PredefinedType
Identifies the predefined types of a roof element from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

## Concepts

### Type Body Geometry



