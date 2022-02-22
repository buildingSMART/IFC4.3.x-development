# IfcCableFitting

A cable fitting is a fitting that is placed at a junction, transition or termination in a cable system.

> HISTORY  New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType
Identifies the predefined types of cable fitting from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCableFittingType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no cable fitting type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCableFittingType_.

## Concepts

### Connection


### Material


### Object Typing


### Port


### Property Sets for Objects


### Quantity Sets


