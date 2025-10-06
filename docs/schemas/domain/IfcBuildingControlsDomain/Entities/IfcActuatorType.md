# IfcActuatorType

The distribution control element type **IfcActuatorType** defines commonly shared information for occurrences of actuators. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
* common ports
<!-- end of short definition -->

It is used to define an actuator type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcActuatorType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcActuatorType** are represented by instances of _IfcActuator_. Refer to the documentation at _IfcActuator_ for supported property sets, materials, composition, and ports.

> HISTORY New entity in IFC2x2

## Attributes

### PredefinedType
Identifies the predefined types of actuator from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType

