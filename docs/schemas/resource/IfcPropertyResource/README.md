IfcPropertyResource
===================

The _IfcPropertyResource_ defines a basic set of property types that can be associated with occurrence objects (subtypes of _IfcObject_) and type objects (subtypes of _IfcTypeObject_) through the _IfcPropertySet_ (defined in the _IfcKernel_ schema). These properties are used to assign property definitions that are semantically defined by a name string and are extensible in terms of their definitions.

> NOTE  Frequently, there is a need to extend the attributes that are attached to an individual object or group of objects. Yet it may not be necessary to extend the attributes for every object within the same class. Using the same capabilities as for types of an element, it is possible to define such sets of attributes and associate them with individual objects.

The association of attributes to objects can be defined by two different ways:

* by defining a type object (_IfcTypeObject_) which defines a specific object information (including the relevant properties) that is assigned to all instances (or occurrences) of the type object (via the _IfcRelDefinesByType_ relationship).
* by defining a property set (_IfcPropertySet_, a logical grouping of related properties) which defines the common property information for an individual instance (or occurrence), this is done via the _IfcRelDefinesByProperties_ relationship.

The semantic information of what an individual property denotes has to be given by the _Name_ attribute. The _Name_ is human interpretable and can also be computer interpretable by convention. This convention has to be established by implementers' agreements.

> NOTE  The IFC specification defines a set of property sets, which provides a recommended usage of property sets for objects in the IFC model. In addition to the IFC property set specification also regional or project specific definitions of property sets are possible. Thereby property sets provide an mechanism to localize IFC definitions.

All subtypes of _IfcProperty_ are referenced later by the _IfcPropertySet_. Thereby the _IfcPropertySet_ establishes a tree of property definitions through the _IfcSimpleProperty_ (and its subtypes) and _IfcComplexProperty_. Any instance of _IfcSimpleProperty_ within this tree shall only be referenced once (by either _IfcPropertySet_ or _IfcComplexProperty_).

> NOTE  The property set attached to an object shall have a tree structure, therefore all properties (either _IfcSimpleProperty_ -and subtypes- or _IfcComplexProperty_) shall be used only once within that structure.
