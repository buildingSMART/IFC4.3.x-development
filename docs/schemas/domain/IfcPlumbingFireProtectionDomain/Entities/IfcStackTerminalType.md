# IfcStackTerminalType

The flow terminal type **IfcStackTerminalType** defines commonly shared information for occurrences of stack terminals. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
* common ports

It is used to define a stack terminal type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcStackTerminalType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcStackTerminalType** are represented by instances of _IfcStackTerminal_. Refer to the documentation at _IfcStackTerminal_ for supported property sets, materials, composition, and ports.

## Attributes

### PredefinedType
Identifies the predefined types of stack terminal from which the type required may be set.

## WhereRules

### CorrectPredefinedType

