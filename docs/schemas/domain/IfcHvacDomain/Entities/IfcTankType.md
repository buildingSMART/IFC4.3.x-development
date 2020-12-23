# IfcTankType

The flow storage device type **IfcTankType** defines commonly shared information for occurrences of tanks. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
* common ports

It is used to define a tank type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcTankType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcTankType** are represented by instances of _IfcTank_. Refer to the documentation at _IfcTank_ for supported property sets, materials, composition, and ports.

## Attributes

### PredefinedType
Defines the type of tank.

## WhereRules

### CorrectPredefinedType

