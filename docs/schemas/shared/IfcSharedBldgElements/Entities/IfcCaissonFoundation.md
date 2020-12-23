# IfcCaissonFoundation

CaissonFoundation essentially is a hollow box that can be either open or closed.

(NOTE: corresponding predefined type is deprecated from IfcFootingTypeEnum).

## Attributes

### PredefinedType
Predefined generic type for a caisson foundation that is specified in an enumeration. There may be a property set given specificly for the predefined types.
> NOTE&nbsp; The _PredefinedType_ shall only be used, if no _IfcCaissonFoundationType_ is assigned, providing its own _IfcCaissoFoundationType.PredefinedType_.

## WhereRules

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcCaissonFoundationType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no caisson foundation type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcCaissonFoundationType_.
