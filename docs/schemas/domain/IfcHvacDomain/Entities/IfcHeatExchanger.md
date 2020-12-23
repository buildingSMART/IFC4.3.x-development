# IfcHeatExchanger

A heat exchanger is a device used to provide heat transfer between non-mixing media such as plate and shell and tube heat exchangers.

_IfcHeatExchanger_ is commonly used on water-side distribution systems to recover energy from a liquid to another liquid (typically water-based), whereas _IfcAirToAirHeatRecovery_ is commonly used on air-side distribution systems to recover energy from a gas to a gas (usually air).

> HISTORY&nbsp; New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType


## WhereRules

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcHeatExchangerType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no heat exchanger type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcHeatExchangerType_.
