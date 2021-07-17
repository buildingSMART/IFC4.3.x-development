IfcGroup
========

_IfcGroup_ is an generalization of any arbitrary group. A group is a logical collection of objects. It does not have its own position, nor can it hold its own shape representation. Therefore a group is an aggregation under some non-geometrical / topological grouping aspects.

> EXAMPLE&nbsp; An example for a group is a system, since it groups elements under the aspect of their role, regardless of their position in a building. One of the most important usage of a group representing a system is the _IfcDistributionSystem_, that groups distribution components, such as space heaters and valves into a heating system.

A group can hold any collection of objects, the relationship _IfcRelAssignsToGroup_ is used to establish the group collection. Objects within a group are products, processes, controls, resources, actors or other groups, thus groups can be nested. An object can be part of zero, one, or many groups. Grouping relationships are not required to be hierarchical nor do they imply a dependency.

Groups are assigned to other objects (such as a process or a resource) by the relationship object that refers to the corresponding object:

* Process: assigned using _IfcRelAssignsToProcess_
* Resource: assigned using _IfcRelAssignsToResource_
* Controls: affecting the group using _IfcRelAssignsToControl_

A group can be exchanged without having already objects within the group collection.

_IfcGroup_ does not define an own object coordinate system, nor does it have an independent shape representation.

> NOTE&nbsp; Use _IfcRelAggregates_ together with the appropriate subtypes of _IfcProduct_ to define an aggregation of products that may have its own position and shape representation. This relationship shall be used to create a product breakdown structure.

> HISTORY&nbsp; New entity in IFC1.0.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The inverse _IsGroupedBy_ relationship is set to 0..n
