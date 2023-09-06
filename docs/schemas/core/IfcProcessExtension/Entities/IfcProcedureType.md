# IfcProcedureType

> HISTORY  New entity in IFC4

An _IfcProcedureType_ provides for all forms of types of procedure that may be specified.

Usage of _IfcProcedureType_ defines the parameters for one or more occurrences of _IfcProcedure_. Parameters may be specified through property sets that may be enumerated in the _IfcProcedureTypeEnum_ data type or through explicit attributes of _IfcProcedure_. Procedure occurrences (_IfcProcedure_ entities) are linked to the procedure type through the _IfcRelDefinesByType_ relationship.

## Attributes

### PredefinedType
Identifies the predefined types of a procedure from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
The attribute _ProcessType_ must be asserted when the value of _PredefinedType_ is set to _USERDEFINED_.
