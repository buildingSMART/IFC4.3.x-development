# IfcShadingDeviceType

The building element type **IfcShadingDeviceType** defines commonly shared information for occurrences of shading devices. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements

It is used to define a shading device type specification indicating the specific product information that is common to all occurrences of that product type. The **IfcShadingDeviceType** may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of **IfcShadingDeviceType** are represented by instances of _IfcShadingDevice_. Refer to the documentation at _IfcShadingDevice_ for supported property sets, materials, and composition.

> HISTORY&nbsp; New entity in IFC4.

## Attributes

### PredefinedType
Identifies the predefined types of a shading device element from which the type required may be set.

## WhereRules

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
