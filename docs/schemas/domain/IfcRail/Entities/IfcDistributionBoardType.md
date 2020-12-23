# IfcDistributionBoardType

The flow controller type \*\*IfcDistributionBoardType\*\* defines commonly shared information for occurrences of distribution boards. The set of shared information may include:

\* common properties with shared property sets
\* common representations
\* common materials
\* common composition of elements
\* common ports

It is used to define a distribution board type specification indicating the specific product information that is common to all occurrences of that product type. The \*\*IfcDistributionBoardType\*\* may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of \*\*IfcDistributionBoardType\*\* are represented by instances of _IfcDistributionBoard_. Refer to the documentation at _IfcDistributionBoard_ for supported property sets, materials, composition, and ports.

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
