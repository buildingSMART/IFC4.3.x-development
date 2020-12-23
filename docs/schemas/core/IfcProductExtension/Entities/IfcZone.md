# IfcZone

A zone is a group of spaces, partial spaces or other zones. Zone structures may not be hierarchical (in contrary to the spatial structure of a project - see _IfcSpatialStructureElement_), i.e. one individual _IfcSpace_ may be associated with zero, one, or several _IfcZone_'s. _IfcSpace_'s are grouped into an _IfcZone_ by using the objectified relationship _IfcRelAssignsToGroup_ as specified at the supertype _IfcGroup_.

> NOTE&nbsp; Certain use cases may restrict the freedom of non hierarchical relationships. In some building service use cases the zone denotes a view based delimited volume for the purpose of analysis and calculation. This type of zone cannot overlap with respect to that analysis, but may overlap otherwise.

> HISTORY&nbsp; New entity in IFC1.0

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The entity is now subtyped from _IfcSystem_ (not its supertype _IfcGroup_) with upward compatibility for file based exchange.

## Attributes

### LongName
Long name for a zone, used for informal purposes. It should be used, if available, in conjunction with the inherited _Name_ attribute.
> NOTE&nbsp; In many scenarios the _Name_ attribute refers to the short name or number of a zone, and the _LongName_ refers to the full name.

  
{ .change-ifc2x4}
> IFC4 CHANGE The attribute has been added at the end of the entity definition.

## WhereRules

### WR1
An _IfcZone_ is grouped by the objectified relationship _IfcRelAssignsToGroup_. Only objects of type _IfcSpace_, _IfcZone_ and _IfcSpatialZone_ are allowed as _RelatedObjects_.
