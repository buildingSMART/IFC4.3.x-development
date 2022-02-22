# IfcRelDeclares

The objectified relationship _IfcRelDeclares_ handles the declaration of objects (subtypes of _IfcObject_) or properties (subtypes of _IfcPropertyDefinition_) to a project or project library (represented by _IfcProject_, or _IfcProjectLibrary_).

The relationship handles the assignment of other objects, like _IfcActor_, or _IfcTypeObject_ to the project, or project libary. The attribute _RelatedDefinitions_ provides the references to the first level objects, that are the elements within the context. All other objects that relate to the first level objects are also defined in the context.

> NOTE  Every object (as subtype of _IfcObject_) has to be declared within the context of a single _IfcProject_, or of a _IfcProjectLibrary_ assigned to a single _IfcProject_. This declaration is transitive. For example: the _IfcWorkPlan_ as first level object is declared within the context of _IfcProject_ via _IfcRelDeclares_, all related _IfcWorkSchedule_'s are related to the context in a transitive way through _IfcWorkPlan_.

> NOTE  The assignment excludes subtypes of _IfcProduct_'s, these are assigned to the _IfcProject_ using the spatial structure approach through _IfcSpatialStructureElement_(s), where the outer container element such as _IfcSite_ or _IfcBuilding_ has an _IfcRelAggregates_ relationship with the _IfcProject_.

The _RelatingContext_ is the project, or project library that comprises all elements. The unit assignments and the presentation contexts defined at _IfcProject_ or _IfcProjectLibrary_ apply to all these elements.

> HISTORY  New entity in IFC4.

## Attributes

### RelatingContext
Reference to the _IfcProject_ to which additional information is assigned.

### RelatedDefinitions
Set of object or property definitions that are assigned to a context and to which the unit and representation context definitions of that context apply.

## Formal Propositions

### NoSelfReference
The instance to with the relation points shall not be contained in the set of _RelatedObjects_.
