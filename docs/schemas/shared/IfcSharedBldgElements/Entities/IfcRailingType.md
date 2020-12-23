# IfcRailingType

The building element type **IfcRailingType** defines commonly shared information for occurrences of railings. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements

It is used to define a railing type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcRailingType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcRailingType** are represented by instances of _IfcRailing_. Refer to the documentation at _IfcRailing_ for supported property sets, materials, and composition.

> HISTORY&nbsp; New entity in IFC2x2.

## Attributes

### PredefinedType
Identifies the predefined types of a railing element from which the type required may be set.

## WhereRules

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
