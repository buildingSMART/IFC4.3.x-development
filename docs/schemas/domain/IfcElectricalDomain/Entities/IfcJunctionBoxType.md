# IfcJunctionBoxType

The flow fitting type **IfcJunctionBoxType** defines commonly shared information for occurrences of junction boxes. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
* common ports
<!-- end of definition -->
It is used to define a junction box type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcJunctionBoxType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcJunctionBoxType** are represented by instances of _IfcJunctionBox_. Refer to the documentation at _IfcJunctionBox_ for supported property sets, materials, composition, and ports.

## Attributes

### PredefinedType
Identifies the predefined types of junction boxes from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType

