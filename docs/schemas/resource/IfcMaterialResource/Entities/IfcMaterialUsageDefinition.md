# IfcMaterialUsageDefinition

_IfcMaterialUsageDefinition_ is a general supertype for all material related information items in IFC that have occurrence specific assignment parameters to assign a set of materials with shape parameters to a reference geometry item of that component.

There are two ways of assigning a set of materials with shape parameters:

* a layer set to a reference curve - assigning a material layer set with material layers having a sequence and thickness parameter to a reference curve of an element - represented by the 'Axis' shape representation of that element
* a profile set to a cardinal point - assigning a material profile set with assigned profile geometry and insertion points to a reference curve by an offset, called "cardinal point" - the reference curve is represented by the 'Axis' shape representation of that element

Each instantiable subtype of _IfcMaterialUsageDefinition_ has to be assigned to a subtype of _IfcElement_ by using the objectified relationship _IfcRelAssociatesMaterial_; it is only valid in conjunction with an element occurrence.

> HISTORY  New entity in IFC4

**Informal Propositions**

1. It is illegal to assign a subtype of _IfcMaterialUsageDefinition_ to a subtype of _IfcElementType_, it shall only be assigned to an element occurrence.

## Attributes

### AssociatedTo
Use of the _IfcMaterialUsageDefinition_ subtypes within the material association of an element occurrence. The association is established by the _IfcRelAssociatesMaterial_ relationship.
