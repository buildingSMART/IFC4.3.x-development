# IfcElectricDistributionBoard

A distribution board is a flow controller in which instances of electrical devices are brought together at a single place for a particular purpose.

A distribution provides a housing for connected electrical distribution elements so that they can be viewed, operated or acted upon from a single place. Each connected item may have its own geometric representation and location.

> HISTORY&nbsp; New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcElectricDistributionBoardType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no electric distribution board type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcElectricDistributionBoardType_.
