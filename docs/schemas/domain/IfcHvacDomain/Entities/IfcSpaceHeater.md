# IfcSpaceHeater

Space heaters utilize a combination of radiation and/or natural convection using a heating source such as electricity, steam or hot water to heat a limited space or area. Examples of space heaters include radiators, convectors, baseboard and finned-tube heaters.

_IfcUnitaryEquipment_ should be used for packaged units supporting a combination of heating, cooling, and/or dehumidification; _IfcCoil_ should be used for coil-based floor heating.

> HISTORY&nbsp; New entity in IFC4

{ .note}
> 

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Electric heaters formerly defined by _IfcElectricHeaterType_ are now represented by this entity with _PredefinedType_ set to _CONVECTOR_ and _Pset_SpaceHeaterCommon_._HeatTransferDimension_ reflecting _IfcElectricHeaterTypeEnum_ as follows: _ELECTRICPOINTHEATER_ = _POINT_, _ELECTRICCABLEHEATER_ = _CURVE_, _ELECTRICMATHEATER_ = _SURFACE_.

## Attributes

### PredefinedType


## WhereRules

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcSpaceHeaterType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no space heater type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcSpaceHeaterType_.
