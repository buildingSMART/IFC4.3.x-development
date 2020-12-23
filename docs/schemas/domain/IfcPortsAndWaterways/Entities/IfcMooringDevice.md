# IfcMooringDevice

A mooring device is an active or passive built element who's primary function is to participate in the mooring of a vessel, this could be in the form of a bollard used as am attachment point for lines or active equipment such as quick release hooks.

## Attributes

### PredefinedType


## WhereRules

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset(e.g. because an _IfcMooringDeviceType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcMooringDeviceType_.
