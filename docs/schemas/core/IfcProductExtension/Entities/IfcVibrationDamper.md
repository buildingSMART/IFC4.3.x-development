# IfcVibrationDamper

A vibration damper is a device used to minimize the effects of vibration in a structure by dissipating kinetic energy. The damper may be passive (elastic, frictional, inertia) or active (in a system using sensors and actuators).

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcVibrationDamperType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
If this occurrence is defined by a type object, the latter has to be an _IfcVibrationDamperType_.
