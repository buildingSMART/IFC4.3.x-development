# IfcElectricGenerator

An electric generator is an engine that is a machine for converting mechanical energy into electrical energy.

> HISTORY  New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcElectricGeneratorType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no electric generator type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcElectricGeneratorType_.

## Concepts

### Composition


### Material


### Object Typing


### Port


### Property Sets for Objects


### Quantity Sets


