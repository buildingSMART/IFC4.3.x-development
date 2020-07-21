IfcImpactProtectionDevice
=========================
A impact protection device is a component used to protect other built elements
from kinetic damage. impact protection devices currently come in 3 different
varieties:  

  

  * A vibration damper used to minimize the effects of vibration in a structure by dissipating kinetic energy. The damper may be passive (elastic, frictional, inertia) or active (in a system using sensors and actuators).
  

  * A vibration isolator is a device used to minimize the effects of vibration transmissibility in a structure.
  

  * Impact devices that dissipate kinetic energy from impacting elements (such as vehicles) by deformation or elastic mechanics.
  


Attribute definitions
---------------------
| Attribute      | Description                                                                                                                                                                                                                                                                                                                                                                |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PredefinedType | Identifies the predefined type of a impact device from which the type modelled, may be set. This type may associate additional specific property sets.NOTE The PredefinedType shall only be used, if no [_IfcImpactProtectionDeviceType_]($element://{2611DC1C-60E0-47b7-8506-B0D8829FA389}) is assigned, providing its own IfcImpactProtectionDeviceType .PredefinedType. |

Associations
------------
| Attribute      | Description   |
|----------------|---------------|
| PredefinedType |               |

