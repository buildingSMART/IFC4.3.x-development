# IfcUnitaryControlElement

A unitary control element combines a number of control components into a single product, such as a thermostat or humidistat.

A unitary control element provides a housing for an aggregation of control or electrical distribution elements that, in combination, perform a singular (unitary) purpose. Each item in the aggregation may have its own geometric representation and location.

> HISTORY&nbsp; New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcUnitaryControlElementType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no unitary control element type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcUnitaryControlElementType_.

## Concepts

### Material


### Object Typing


### Port


### Property Sets for Objects


### Quantity Sets


