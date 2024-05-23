The flow terminal type **IfcLampType** defines commonly shared information for occurrences of lamps. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
* common ports


<!-- end of short definition -->

It is used to define a lamp type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcLampType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcLampType** are represented by instances of _IfcLamp_. Refer to the documentation at _IfcLamp_ for supported property sets, materials, composition, and ports.

## Attributes

### PredefinedType
Identifies the predefined types of lamp from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType

