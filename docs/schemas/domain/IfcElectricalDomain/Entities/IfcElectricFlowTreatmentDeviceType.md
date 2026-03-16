# IfcElectricFlowTreatmentDeviceType

The flow treatment device type _IfcElectricFlowTreatmentDeviceType_ defines commonly shared information for occurrences of electric flow treatment devices. The set of shared information may include:

* common properties with shared property sets
* common representations
* common materials
* common composition of elements
* common ports
<!-- end of short definition -->

It is used to define an electric flow treatment device type specification indicating the specific product information that is common to all occurrences of that product type. The _IfcElectricFlowTreatmentDeviceType_ may be declared within _IfcProject_ or _IfcProjectLibrary_ using _IfcRelDeclares_ and may be exchanged with or without occurrences of the type. Occurrences of _IfcElectricFlowTreatmentDeviceType_ are represented by instances of _IfcElectricFlowTreatmentDevice_. Refer to the documentation at _IfcElectricFlowTreatmentDevice_ for supported property sets, materials, composition, and ports.

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.
