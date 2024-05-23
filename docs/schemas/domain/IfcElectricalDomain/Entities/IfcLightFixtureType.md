The flow terminal type **IfcLightFixtureType** defines commonly shared information for occurrences of light fixtures. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
* common ports


<!-- end of short definition -->

It is used to define a light fixture type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcLightFixtureType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcLightFixtureType** are represented by instances of _IfcLightFixture_. Refer to the documentation at _IfcLightFixture_ for supported property sets, materials, composition, and ports.

## Attributes

### PredefinedType
Identifies the predefined types of light fixture from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType

