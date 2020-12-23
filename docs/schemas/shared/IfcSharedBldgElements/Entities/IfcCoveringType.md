# IfcCoveringType

The element type _IfcCoveringType_ defines commonly shared information for occurrences of coverings. The set of shared information may include:

* common properties within shared property sets
* common material (layer set) information
* common shape representations

It is used to define an covering specification or covering style (i.e. the specific product information, that is common to all occurrences of that product type). Covering types may be exchanged without being already assigned to occurrences.

The occurrences of the _IfcCoveringType_ are represented by instances of _IfcCovering_

> HISTORY&nbsp; New entity in IFC2x2.

{ .spec-head}
Informal Propositions:

1. The material assignment, if provided using the _IfcRelAssociatesMaterial_ relationship, shall not reference _IfcMaterialLayerSetUsage_ or _IfcMaterialProfileSetUsage_.

## Attributes

### PredefinedType
Predefined types to define the particular type of the covering. There may be property set definitions available for each predefined type.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
