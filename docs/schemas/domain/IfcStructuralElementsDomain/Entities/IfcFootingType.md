# IfcFootingType

The building element type **IfcFootingType** defines commonly shared information for occurrences of footings. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements

It is used to define a footing type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcFootingType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcFootingType** are represented by instances of _IfcFooting_. Refer to the documentation at _IfcFooting_ for supported property sets, materials, and composition.

> HISTORY&nbsp; New entity in IFC4.

## Attributes

### PredefinedType
Subtype of footing.

## WhereRules

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided if the _PredefinedType_ is set to USERDEFINED.
