# IfcRelDeclares

The objectified relationship _IfcRelDeclares_ handles the declaration of objects (subtypes of _IfcObject_) or properties (subtypes of _IfcPropertyDefinition_) to a project or project library (represented by _IfcProject_, or _IfcProjectLibrary_).<!-- end of definition -->

The relationship handles the assignment of other objects, like _IfcActor_, or _IfcTypeObject_ to the project, or project library. The attribute _RelatedDefinitions_ provides the references to the first level objects, that are the objects within the context. All other objects that relate to the first level objects are also defined in the context.

> NOTE Every object (as subtype of _IfcObject_) has to be declared within the context of a single _IfcProject_, or of a _IfcProjectLibrary_ assigned to a single _IfcProject_. This declaration is transitive. For example: the _IfcWorkPlan_ as first level object is declared within the context of _IfcProject_ via _IfcRelDeclares_, all related _IfcWorkSchedule_'s are related to the context in a transitive way through _IfcWorkPlan_.

> NOTE This assignment using _IfcRelDeclares_ excludes every object (as subtype of _IfcObject_) already related to _IfcProject_ via other relationships. For example, _IfcSpatialStructureElement_(s) that are related to _IfcProject_ through _IfcRelAggregates_ relationships; and subtypes of _IfcProduct_'s that are contained in these _IfcSpatialStructureElement_(s) through _IfcRelContainedInSpatialStructure_ relationships.

The _RelatingContext_ is the project, or project library that comprises all objects. The unit assignments and the presentation contexts defined at _IfcProject_ or _IfcProjectLibrary_ apply to all these objects.

> HISTORY New entity in IFC4.

## Attributes

### RelatingContext
Reference to the _IfcProject_ to which additional information is assigned.

### RelatedDefinitions
Set of object or property definitions that are assigned to a context and to which the unit and representation context definitions of that context apply.

## Formal Propositions

### NoSelfReference
The instance to which the relation points shall not be contained in the set of _RelatedObjects_.
