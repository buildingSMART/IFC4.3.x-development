# IfcPileType

The building element type **IfcPileType** defines commonly shared information for occurrences of piles. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
<!-- end of short definition -->

It is used to define a pile type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcPileType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcPileType** are represented by instances of _IfcPile_. Refer to the documentation at _IfcPile_ for supported property sets, materials, and composition.

> HISTORY New entity in IFC4.

## Attributes

### PredefinedType
Subtype of pile.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided if the _PredefinedType_ is set to USERDEFINED.
