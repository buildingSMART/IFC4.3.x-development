IfcBuiltSystem
==============

A built system is a group by which built elements are grouped according to a common function within the facility.
The group _IfcBuiltSystem_  defines the occurrence of a specialized system for use within the context of a facilities physical or finishing fabric. Important functionalities for the description of a built system are derived from supertypes:
* From _IfcSystem_ it inherits the ability to couple the built system via _IfcRelReferencedInSpatialStructure_ to one or more _IfcSpatialElement_ subtypes as necessary.
* From _IfcGroup_ it inherits the inverse attribute IsGroupedBy, pointing to the relationship class _IfcRelAssignsToGroup_ . This allows the grouping of built elements (instances of _IfcBuiltElement_ subtypes, _IfcFurnishingElement_ subtypes, _IfcElementAssembly_ and _IfcTransportElement_).
* From _IfcObjectDefinition_ it inherits the inverse attribute IsDecomposedBy pointing to the relationship class _IfcRelAggregates_. It provides the hierarchy between the separate (partial) building systems.
