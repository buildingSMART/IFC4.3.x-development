# IfcCableSegmentType

The flow segment type **IfcCableSegmentType** defines commonly shared information for occurrences of cable segments. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
* common ports
<!-- end of definition -->
It is used to define a cable segment type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcCableSegmentType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcCableSegmentType** are represented by instances of _IfcCableSegment_. Refer to the documentation at _IfcCableSegment_ for supported property sets, materials, composition, and ports.

## Attributes

### PredefinedType
Identifies the predefined types of cable segment from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType

