# IfcRelationship

_IfcRelationship_ is the abstract generalization of all objectified relationships in IFC. Objectified relationships are the preferred way to handle relationships among objects. This allows to keep relationship specific properties directly at the relationship and opens the possibility to later handle relationship specific behavior.

There are two different types of relationships, 1-to-1 relationships and 1-to-many relationships, used within the subtypes of _IfcRelationship_. The following convention applies to all subtypes:

* The two sides of the objectified relationship are named Relating+"name of relating object" and Related+"name of related object"
* In case of the 1-to-many relationship, the related side of the relationship shall be an aggregate being a set 1:N

> HISTORY  New entity in IFC1.0.
