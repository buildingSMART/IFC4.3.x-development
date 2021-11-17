# IfcCoolingTower

A cooling tower is a device which rejects heat to ambient air by circulating a fluid such as water through it to reduce its temperature by partial evaporation.

> HISTORY&nbsp; New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCoolingTowerType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no cooling tower type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCoolingTowerType_.

## Concepts

### Composition


### Material


### Object Typing


### Port


### Property Sets for Objects


### Quantity Sets


