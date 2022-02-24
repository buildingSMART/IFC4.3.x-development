Group Assignment
================

_Group Assignment_ established an arbitrary collection of objects within a group. The grouping relationship does not apply any other meaning then grouping objects under some aspect. It is non-hierarchical, that is objects can be grouped into different logical groups, and it does not interfere with other relationship concepts, such as _ObjectAggregation_.

The _Group Assignment_ concept establish a given object as being the group collection for other objects. An _IfcZone_ is a specific group object for collecting spaces, _IfcDistributionSystem_ is a specific group object for collecting distribution elements. Usually a grouping relationship is applied to group elements for a particular purpose or function. It usually implies the existence of a grouping relationship and the provision of some identity under which the group is characterized.

* Group collection is handled by an instance of _IfcRelAssignsToGroup_, which assigns all group members to the _IfcGroup_ being the collection.
* Objects included in group as collected items are linked by _IsGroupedBy_ pointing to _IfcRelAssignsToGroup_

> NOTE  The _IfcGroup_ maybe not yet have a grouping relationship established, it then identifies an empty group.

> EXAMPLE  An air handler belonging to an air conditioning system is an example of such group assignment.

```
concept {
    IfcGroup:IsGroupedBy -> IfcRelAssignsToGroup:RelatingGroup
    IfcRelAssignsToGroup:RelatedObjects -> IfcProduct
    IfcGroup:IsGroupedBy[binding="IsGrouped"]
    IfcRelAssignsToGroup:RelatedObjects[binding="RelatedObjects"]
}
```
