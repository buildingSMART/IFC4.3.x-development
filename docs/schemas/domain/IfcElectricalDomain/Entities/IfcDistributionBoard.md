# IfcDistributionBoard

A distribution board is a flow controller in which instances of electrical or communication devices are brought together at a single place for a particular purpose.
<!-- end of short definition -->

A distribution provides a housing for connected distribution elements so that they can be viewed, operated or acted upon from a single place. Each connected item may have its own geometric representation and location.

## Attributes

### PredefinedType


## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset(e.g. because an _IfcDistributionBoardType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcDistributionBoardType_.
