# IfcOutlet

An outlet is a device installed at a point to receive one or more inserted plugs for electrical power or communications.

Power outlets are commonly connected within a junction box; data outlets may be directly connected to a wall. For power outlets sharing the same circuit within a junction box, the ports should indicate the logical wiring relationship to the enclosing junction box, even though they may be physically connected to a cable going to another outlet, switch, or fixture.

> HISTORY&nbsp; New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcOutletType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no outlet type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcOutletType_.

## Concepts

### Material


### Object Typing


### Port


### Property Sets for Objects


### Quantity Sets


