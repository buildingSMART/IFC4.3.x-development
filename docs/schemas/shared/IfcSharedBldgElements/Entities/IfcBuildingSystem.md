# IfcBuildingSystem

A building system is a group by which building elements are grouped according to a common function within the facility.

The group _IfcBuildingSystem_ defines the occurrence of a specialized system for use within the context of a building and finishing fabric. Important functionalities for the description of a building system are derived from supertypes:

* From _IfcSystem_ it inherits the ability to couple the building system via _IfcRelServicesBuildings_ to one or more _IfcSpatialElement_ subtypes as necessary.
* From _IfcGroup_ it inherits the inverse attribute _IsGroupedBy_, pointing to the relationship class _IfcRelAssignsToGroup_. This allows to group building elements (instances of _IfcBuildingElement_ subtypes, _IfcFurnishingElement_ subtype, _IfcElementAssembly_ and _IfcTransportElement_).
* From _IfcObjectDefinition_ it inherits the inverse attribute _IsDecomposedBy_ pointing to the relationship class _IfcRelAggregates_. It provides the hierarchy between the separate (partial) building systems.

> HISTORY&nbsp; New entity in IFC4.

## Attributes

### PredefinedType
Predefined types of distribution systems.

### LongName
Long name for a building system, used for informal purposes. It should be used, if available, in conjunction with the inherited _Name_ attribute.
> NOTE&nbsp; In many scenarios the _Name_ attribute refers to the short name or number of a building system, and the _LongName_ refers to a descriptive name.
