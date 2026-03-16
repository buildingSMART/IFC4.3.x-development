# IfcElectricFlowTreatmentDevice

An electric flow treatment device is used to remove unwanted matter from an electric or electronic signal in a flow distribution system.
<!-- end of short definition -->

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcElectricFlowTreatmentDeviceType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcElectricFlowTreatmentDeviceType_.
