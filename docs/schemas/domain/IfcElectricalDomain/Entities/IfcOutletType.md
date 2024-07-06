The flow terminal type **IfcOutletType** defines commonly shared information for occurrences of outlets. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
* common ports


<!-- end of short definition -->

It is used to define a outlet type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcOutletType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcOutletType** are represented by instances of _IfcOutlet_. Refer to the documentation at _IfcOutlet_ for supported property sets, materials, composition, and ports.

## Attributes

### PredefinedType
Identifies the predefined types of outlet from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType

