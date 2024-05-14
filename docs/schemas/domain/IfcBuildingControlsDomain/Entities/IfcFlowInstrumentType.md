# IfcFlowInstrumentType

The distribution control element type **IfcFlowInstrumentType** defines commonly shared information for occurrences of flow instruments. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
* common ports
<!-- end of definition -->
It is used to define a flow instrument type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcFlowInstrumentType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcFlowInstrumentType** are represented by instances of _IfcFlowInstrument_. Refer to the documentation at _IfcFlowInstrument_ for supported property sets, materials, composition, and ports.

> HISTORY New entity in IFC2x2

## Attributes

### PredefinedType
Identifies the predefined types of flow instrument from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType

