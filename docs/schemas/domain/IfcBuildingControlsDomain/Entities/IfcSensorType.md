# IfcSensorType

The distribution control element type **IfcSensorType** defines commonly shared information for occurrences of sensors. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
* common ports
<!-- end of short definition -->

It is used to define a sensor type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcSensorType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcSensorType** are represented by instances of _IfcSensor_. Refer to the documentation at _IfcSensor_ for supported property sets, materials, composition, and ports.

> HISTORY New entity in IFC2x2

## Attributes

### PredefinedType
Identifies the predefined types of sensor from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType

