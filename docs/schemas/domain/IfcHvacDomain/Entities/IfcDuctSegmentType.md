# IfcDuctSegmentType

The flow segment type **IfcDuctSegmentType** defines commonly shared information for occurrences of duct segments. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
* common ports

It is used to define a duct segment type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcDuctSegmentType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcDuctSegmentType** are represented by instances of _IfcDuctSegment_. Refer to the documentation at _IfcDuctSegment_ for supported property sets, materials, composition, and ports.

## Attributes

### PredefinedType
The type of duct segment.

## WhereRules

### CorrectPredefinedType

