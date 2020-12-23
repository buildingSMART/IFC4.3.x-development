# IfcFilterType

The flow treatment device type **IfcFilterType** defines commonly shared information for occurrences of filters. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
* common ports

It is used to define a filter type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcFilterType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcFilterType** are represented by instances of _IfcFilter_. Refer to the documentation at _IfcFilter_ for supported property sets, materials, composition, and ports.

## Attributes

### PredefinedType
The type of air filter.

## WhereRules

### CorrectPredefinedType

