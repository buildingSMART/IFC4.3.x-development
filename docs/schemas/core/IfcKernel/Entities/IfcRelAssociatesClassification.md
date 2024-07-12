# IfcRelAssociatesClassification

The objectified relationship _IfcRelAssociatesClassification_ handles the assignment of a classification item (items of the select _IfcClassificationSelect_) to objects occurrences (subtypes of _IfcObject_) or object types (subtypes of _IfcTypeObject_).
<!-- end of short definition -->


The relationship is used to assign a classification item, or a classification system itself to objects. Depending on the type of the _RelatingClassification_ it is either:

* a reference to an classification item within an external classification system, or
* a reference to the classification system itself

> NOTE The reference to a classification item includes a link to the classification system within which the item is declared. It assigns the meaning of the classification item to the object (occurrence or type). The reference to the classification system provides the information that the object (occurrence or type) is governed by the classification system but no assignment of a particular items has been done yet.

The inherited attribute _RelatedObjects_ define the objects or object types to which the classification is applied. The attribute _RelatingClassification_ is the reference to a classification, applied to the object(s). A single _RelatingClassification_ can thereby be applied to one or multiple objects.

> HISTORY New entity in IFC2x.

## Attributes

### RelatingClassification
Classification applied to the objects.
