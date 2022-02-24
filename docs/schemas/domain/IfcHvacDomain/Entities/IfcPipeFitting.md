# IfcPipeFitting

A pipe fitting is a junction or transition in a piping flow distribution system used to connect pipe segments, resulting in changes in flow characteristics to the fluid such as direction or flow rate.

Pipe fittings include elbows, junctions, manifolds, and plumbing boxes.

> HISTORY  New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcPipeFittingType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no pipe fitting type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcPipeFittingType_.

## Concepts

### Material


### Object Typing


### Port


### Property Sets for Objects


### Quantity Sets


