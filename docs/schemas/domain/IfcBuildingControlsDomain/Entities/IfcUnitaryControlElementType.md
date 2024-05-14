# IfcUnitaryControlElementType

The distribution control element type **IfcUnitaryControlElementType** defines commonly shared information for occurrences of unitary control elements. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
* common ports
<!-- end of definition -->
It is used to define a unitary control element type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcUnitaryControlElementType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcUnitaryControlElementType** are represented by instances of _IfcUnitaryControlElement_. Refer to the documentation at _IfcUnitaryControlElement_ for supported property sets, materials, composition, and ports.

> HISTORY New entity in IFC4

## Attributes

### PredefinedType
Identifies the predefined types of unitary control element from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType

