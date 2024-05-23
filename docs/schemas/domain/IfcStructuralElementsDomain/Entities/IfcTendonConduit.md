A TendonConduit represents the components of the conduit system for tendons embedded in concrete structure.

<!-- end of short definition -->


## Attributes

### PredefinedType
The predefined generic type of the tendon conduit.

## Formal Propositions

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset (e.g. because an _IfcTendonConduitType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
If this occurrence is defined by a type object, the latter has to be an _IfcTendonConduitType_.
