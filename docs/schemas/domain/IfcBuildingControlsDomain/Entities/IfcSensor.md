# IfcSensor

A sensor is a device that measures a physical quantity and converts it into a signal which can be read by an observer or by an instrument.

> HISTORY  New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcSensorType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no sensor type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcSensorType_.

## Concepts

### Control Flow


### Material


### Object Typing


### Port


### Property Sets for Objects


### Quantity Sets


