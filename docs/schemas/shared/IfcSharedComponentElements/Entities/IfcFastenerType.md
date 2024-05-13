# IfcFastenerType

The element component type **IfcFastenerType** defines commonly shared information for occurrences of fasteners. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
<!-- end of definition -->
It is used to define a fastener type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcFastenerType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcFastenerType** are represented by instances of _IfcFastener_.

> HISTORY  New entity in IFC2x2.

## Attributes

### PredefinedType
Subtype of fastener

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided if the _PredefinedType_ is set to USERDEFINED.
