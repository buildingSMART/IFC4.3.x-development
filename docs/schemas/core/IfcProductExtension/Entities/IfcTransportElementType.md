# IfcTransportElementType

The element type _IfcTransportElementType_ defines commonly shared information for occurrences of transport elements. The set of shared information may include:

* common properties within shared property sets
* common material information
* common shape representations


It is used to define a transport element specification (i.e. the specific product information that is common to all occurrences of that transport element type). Transport element types (or the instantiable subtypes) may be exchanged without being already assigned to occurrences.
The occurrences of the _IfcTransportElementType_ are represented by instances of _IfcTransportElement_ (or its subtypes).

> HISTORY  New entity in IFC2x2.

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
