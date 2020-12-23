# IfcAlarm

An alarm is a device that signals the existence of a condition or situation that is outside the boundaries of normal expectation or that activates such a device.

Alarms include the provision of break glass buttons and manual pull boxes that are used to activate alarms.

> HISTORY&nbsp; New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType


## WhereRules

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcAlarmType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no alarm type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcAlarmType_.
