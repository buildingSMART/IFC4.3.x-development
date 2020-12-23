# IfcRoot

_IfcRoot_ is the most abstract and root class for all entity definitions that roots in the kernel or in subsequent layers of the IFC specification. It is therefore the common supertype of all IFC entities, beside those defined in an IFC resource schema. All entities that are subtypes of _IfcRoot_ can be used independently, whereas resource schema entities, that are not subtypes of _IfcRoot_, are not supposed to be independent entities.

> NOTE&nbsp; View definitions and implementation agreement may impose additional restrictions on the use of the _OwnerHistory_ to handle object versioning.

> HISTORY&nbsp; New entity in IFC1.0

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attribute _OwnerHistory_ has been made OPTIONAL.

## Attributes

### GlobalId
Assignment of a globally unique identifier within the entire software world.

### OwnerHistory
Assignment of the information about the current ownership of that object, including owning actor, application, local identification and information captured about the recent changes of the object, 

> NOTE&nbsp; only the last modification in stored - either as addition, deletion or modification.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attribute has been changed to be OPTIONAL.

### Name
Optional name for use by the participating software systems or users. For some subtypes of IfcRoot the insertion of the Name attribute may be required. This would be enforced by a where rule.

### Description
Optional description, provided for exchanging informative comments.

## UniqueRules

### UR1

