# IfcValve

A valve is used in a building services piping distribution system to control or modulate the flow of the fluid.

> HISTORY&nbsp; New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcValveType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no valve type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcValveType_.

## Concepts

### Connection


### Material


### Object Typing


### Port


### Property Sets for Objects


### Quantity Sets


