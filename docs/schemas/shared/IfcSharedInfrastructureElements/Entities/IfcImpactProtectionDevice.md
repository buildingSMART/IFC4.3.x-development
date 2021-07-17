# IfcImpactProtectionDevice

A impact protection device is a component used to protect other built elements from kinetic damage. impact protection devices currently come in 3 different varieties:
* A vibration damper used to minimize the effects of vibration in a structure by dissipating kinetic energy. The damper may be passive (elastic, frictional, inertia) or active (in a system using sensors and actuators).
* A vibration isolator is a device used to minimize the effects of vibration transmissibility in a structure.
* Impact devices that dissipate kinetic energy from impacting elements (such as vehicles) by deformation or elastic mechanics.

## Attributes

### PredefinedType
Identifies the predefined type of a impact device. This type may associate additional specific property sets.
NOTE  The PredefinedType shall only be used, if no IfcImpactProtectionDeviceType is assigned, providing its own IfcImpactProtectionDeviceType .PredefinedType.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset(e.g. because an _IfcImpactProtectionDeviceType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcImpactProtectionDeviceType_.
