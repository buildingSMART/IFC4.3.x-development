# IfcMobileTelecommunicationsAppliance

A mobile telecommunications appliance is a device that transmits, converts, amplifies or receives signals used in mobile networks.
Note: This entity is used to define specific appliances used in mobile telecommunication networks. General communications appliances and those used in fixed transmission networks should be instantiated using IfcCommunicationsAppliance.

## Attributes

### PredefinedType


## WhereRules

### CorrectPredefinedType
Either the _PredefinedType_ attribute is unset(e.g. because an _IfcMobileTelecommunicationsApplianceType_ is associated), or the inherited attribute _ObjectType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

### CorrectTypeAssigned
Either there is no type object associated, i.e. the _IsTypedBy_ inverse relationship is not provided, or the associated type object has to be of type _IfcMobileTelecommunicationsApplianceType_.
