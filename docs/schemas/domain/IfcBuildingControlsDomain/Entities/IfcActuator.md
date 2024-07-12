# IfcActuator

An actuator is a mechanical device for moving or controlling a mechanism or system. An actuator takes energy, usually created by air, electricity, or liquid, and converts that into some kind of motion.<!-- end of definition -->

> HISTORY New entity in IFC4

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcActuatorType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no actuator type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcActuatorType_.

## Concepts

### Control Flow



#### IfcFlowController

Indicates a connected valve, damper, or switch controlled by the actuator.

### Material Set



#### Casing

Material from which the casing is constructed.

### Object Typing



### Port Nesting



#### Sink_Input_Signal

Receives signal.

### Property Sets for Objects



### Quantity Sets



