# IfcTendonAnchor

A tendon anchor is the end connection for tendons in prestressed or posttensioned concrete.

> HISTORY&nbsp; New entity in IFC2x2.

{ .history}
> IFC4 CHANGE&nbsp; Attribute _PredefinedType_ added.

## Attributes

### PredefinedType
Kind of tendon anchor.

## WhereRules

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcTendonAnchorType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
If this occurrence is defined by a type object, the latter has to be an _IfcTendonAnchorType_.
