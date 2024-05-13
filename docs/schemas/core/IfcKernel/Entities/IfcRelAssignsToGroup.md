# IfcRelAssignsToGroup

The objectified relationship _IfcRelAssignsToGroup_ handles the assignment of object definitions (individual object occurrences as subtypes of _IfcObject_, and object types as subtypes of _IfcTypeObject_) to a group (subtypes of _IfcGroup_).

The relationship handles the assignment of group members to the group object. It allows for grouping arbitrary objects within a group, including other groups. The grouping relationship can be applied in a recursive manner. The resulting group is of type _IfcGroup_.

> NOTE  Examples of groups include zones as a grouping of spaces, distribution systems as a grouping of building service components, or structural analysis models as a grouping of structural items.

The inherited attribute _RelatedObjects_ gives the references to the objects, which are the elements within the group. The _RelatingGroup_ is the group that comprises all elements. The same object or object type can be included in zero, one or many groups. Grouping relationships are not hierarchical.

**Informal Propositions**

1. The group assignment relationship shall be acyclic, that is, a group shall not participate in its own grouping relationship.

> HISTORY  New entity in IFC1.0. It has been renamed from IfcRelGroups in IFC2x.

## Attributes

### RelatingGroup
Reference to group that contains all assigned group members.

## Formal Propositions

### NoSelfReference
The instance to which the relation points shall not be contained in the set of _RelatedObjects_.
