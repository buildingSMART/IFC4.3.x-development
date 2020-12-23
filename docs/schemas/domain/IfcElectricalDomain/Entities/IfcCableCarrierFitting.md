# IfcCableCarrierFitting

A cable carrier fitting is a fitting that is placed at junction or transition in a cable carrier system.

> HISTORY&nbsp; New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType
Identifies the predefined types of cable carrier fitting from which the type required may be set.

## WhereRules

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCableCarrierFittingType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no cable carrier fitting type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCableCarrierFittingType_.
