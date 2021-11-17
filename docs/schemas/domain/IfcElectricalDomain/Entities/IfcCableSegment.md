# IfcCableSegment

A cable segment is a flow segment used to carry electrical power, data, or telecommunications signals.

A cable segment is used to typically join two sections of an electrical network or a network of components carrying the electrical service.

> HISTORY&nbsp; New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType
Identifies the predefined types of cable segment from which the type required may be set.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCableSegmentType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no cable segment type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCableSegmentType_.

## Concepts

### Composition


### Material


### Object Typing


### Port


### Property Sets for Objects


### Quantity Sets


