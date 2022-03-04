# IfcPreDefinedPropertySet

_IfcPreDefinedPropertySet_ is a generalization of all statically defined property sets that are assigned to an object or type object. The statically or pre-defined property sets are entities with a fixed list of attributes having particular defined data types.

Property sets are related to other objects by using the relationship object that refers to the corresponding object:

* **Occurrence Object**: _IfcRelDefinesByProperties_ using the inverse attribute _DefinesOccurrence_.
* **Type Object**: using a direct link by inverse attribute _DefinesType_.

_IfcPreDefinedPropertySet_'s can be assigned to objects and object types but do not have a defining property set template.

> HISTORY  New entity in IFC4
