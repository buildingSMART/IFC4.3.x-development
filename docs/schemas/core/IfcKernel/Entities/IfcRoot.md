# IfcRoot

_IfcRoot_ is the most abstract and root class for all entity definitions that roots in the kernel or in subsequent layers of the IFC specification. It is therefore the common supertype of all IFC entities, beside those defined in an IFC resource schema. All entities that are subtypes of _IfcRoot_ can be used independently, whereas resource schema entities, that are not subtypes of _IfcRoot_, are not supposed to be independent entities.<!-- end of definition -->

> NOTE View definitions and implementation agreements may impose additional restrictions on the use of the _OwnerHistory_ to handle object versioning.

> HISTORY New entity in IFC1.0

{ .change-ifc2x4}
> IFC4 CHANGE The attribute _OwnerHistory_ has been made OPTIONAL.

## Attributes

### GlobalId
Assignment of a globally unique identifier within the entire software world.

### OwnerHistory
Assignment of the information about the current ownership of that object, including owning actor, application, local identification and information captured about the recent changes of the object,

> NOTE Only the last modification is stored - either as addition, deletion or modification.

{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been changed to be OPTIONAL.

### Name
Optional name for use by the participating software systems or users. For some subtypes of IfcRoot the insertion of the Name attribute may be required. This would be enforced by a where rule.

### Description
Optional description, provided for exchanging informative comments.

## UniqueRules

### UR1

## Concepts

### Revision Control

Ownership, history, and merge state is captured using IfcOwnerHistory.

### Software Identity

IfcRoot assigns the globally unique ID. In addition it may provide for a name and a description about the concept.

