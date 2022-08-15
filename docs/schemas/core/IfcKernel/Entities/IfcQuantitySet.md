# IfcQuantitySet

_IfcQuantitySet_ is the the abstract supertype for all quantity sets attached to objects. The quantity set is a container class that holds the individual quantities within a quantity tree. These quantities are interpreted according to their name attribute and classified according to their measure type. Some quantity sets are included in the IFC specification and have a predefined set of quantities indicated by assigning a significant name. These quantity sets are listed as "quantity sets" within this specification. Quantity sets applicable to certain objects are listed in the object specification.

An _IfcPropertySetTemplate_ may define the underlying structure, i.e. the required name, the applicable object or object types to which the quantity set can be attached, and the individual quantities that maybe included. Quantity sets are related to other objects by using the relationship object that refers to the corresponding object:

* **Occurrence Object**: _IfcRelDefinesByProperties_ using the inverse attribute _DefinesOccurrence_.
* **Type Object**: using a direct link by inverse attribute _DefinesType_.
* **Underlying template**: _IfcRelDefinesByTemplate_ using the inverse attribute _IsDefinedBy_.
* **External reference**: subtypes of _IfcRelAssociates_ are used to provide a link to a classification system, or external library providing further reference to the quantity set. Accessible by inverse attribute _HasAssociations_.

> HISTORY  New entity in IFC4.
