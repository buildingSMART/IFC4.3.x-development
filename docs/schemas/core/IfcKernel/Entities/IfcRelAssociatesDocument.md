# IfcRelAssociatesDocument

The objectified relationship (_IfcRelAssociatesDocument_) handles the assignment of document information (items of the select _IfcDocumentSelect_) to objects occurrences (subtypes of _IfcObject_) or object types (subtypes of _IfcTypeObject_).<!-- end of definition -->

The relationship is used to assign a document reference or more detailed document information to objects. A single document reference can be applied to multiple objects.

The inherited attribute _RelatedObjects_ defines the objects to which the document association is applied. The attribute _RelatingDocument_ is the reference to a document reference, applied to the object(s).

> HISTORY New entity in IFC2x.

## Attributes

### RelatingDocument
Document information or reference which is applied to the objects.
