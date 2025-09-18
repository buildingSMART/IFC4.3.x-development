# IfcTypeResource

_IfcTypeResource_ defines a specific (or type) definition of a resource. It is used to define a resource specification (the specific resource that is common to all occurrences that are defined for that resource) and could act as a resource template.
<!-- end of short definition -->

An _IfcTypeResource_ may have a list of property sets attached. Values of these properties are common to all occurrences of that resource type. The type occurrence relationship is realized using the objectified relationship _IfcRelDefinesByType_.

Subtypes of _IfcTypeResource_ may be exchanged without being already assigned to subtypes of _IfcResource_.

> HISTORY New entity in IFC4.

## Attributes

### Identification
An identifying designation given to a resource type.

### LongDescription
A long description, or text, describing the resource in detail.
> NOTE The inherited _SELF\IfcRoot.Description_ attribute is used as the short description.

### ResourceType
The type denotes a particular type that indicates the resource further. The use has to be established at the level of instantiable subtypes. In particular it holds the user defined type, if the enumeration of the attribute _PredefinedType_ is set to USERDEFINED.

### ResourceOf
Set of relationships to other objects, e.g. products, processes, controls, resources or actors to which this resource type is a resource.
> HISTORY New inverse relationship in IFC4.
