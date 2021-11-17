# IfcJunctionBox

A junction box is an enclosure within which cables are connected.

Cables may be members of an electrical circuit (for electrical power systems) or be information carriers (in a telecommunications system). A junction box is typically intended to conceal a cable junction from sight, eliminate tampering or provide a safe place for electrical connection.

> HISTORY&nbsp; New entity in IFC4

{ .note}
>

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcJunctionBoxType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no junction box type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcJunctionBoxType_.

## Concepts

### Element Connectivity


### Element Nesting


> IFC4 ADD1 CHANGE  Junction boxes no longer have ports defined, but rely on element nesting for indicating containment of electrical devices.


### Filling


### Material


### Object Typing


### Property Sets for Objects


### Quantity Sets


