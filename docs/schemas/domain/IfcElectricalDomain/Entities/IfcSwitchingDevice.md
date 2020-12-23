# IfcSwitchingDevice

A switch is used in a cable distribution system (electrical circuit) to control or modulate the flow of electricity.

Switches include those used for electrical power, communications, audio-visual, or other distribution system types as determined by the available ports.

> HISTORY&nbsp; New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcSwitchingDeviceType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no switching device type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcSwitchingDeviceType_.
