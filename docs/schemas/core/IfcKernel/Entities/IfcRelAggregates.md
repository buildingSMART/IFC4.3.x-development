# IfcRelAggregates

The aggregation relationship _IfcRelAggregates_ is a special type of the general composition/decomposition (or whole/part) relationship _IfcRelDecomposes_. The aggregation relationship can be applied to all subtypes of _IfcObjectDefinition_.

In cases of aggregation of physical elements into a physical aggregate the shape representation of the whole (within the same representation identifier) can be taken from the sum of the shape representations of the parts.

> EXAMPLE&nbsp; A roof is the aggregation of the roof elements, such as roof slabs, rafters, purlins, etc. Within the same representation identifier (such as the body geometric representation), the shape representation of the roof is given by the shape representation of its parts.

Decompositions imply a dependency, implying that the whole depends on the definition of the parts and the parts depend on the existence of the whole. The behaviour that is implied from the dependency relationship has to be established inside the applications.

> HISTORY&nbsp; New entity in IFC2x.

{ .change-ifc2x4}
> IFC4 CHANGE The attributes _RelatingObject_ and _RelatedObjects_ are demoted from the supertype _IfcRelDecomposes_.

## Attributes

### RelatingObject
The object definition, either an object type or an object occurrence, that represents the aggregation. It is the whole within the whole/part relationship.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attribute has been demoted from the supertype _IfcRelDecomposes_ and defines the non-ordered aggregation relationship.

### RelatedObjects
The object definitions, either object occurrences or object types, that are being aggregated. They are defined as the parts in the whole/part relationship. No order is implied between the parts.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attribute has been demoted from the supertype _IfcRelDecomposes_ and defines the non-ordered set of parts within the aggregation.

## Formal Propositions

### NoSelfReference
The instance to with the relation points as provided by _RelatingObject_ shall not be contained in the set of _RelatedObjects_.
