IfcRelAssociatesDocument
========================
The objectified relationship (_IfcRelAssociatesDocument_) handles the
assignment of a document information (items of the select _IfcDocumentSelect_)
to objects occurrences (subtypes of _IfcObject_) or object types (subtypes of
_IfcTypeObject_).  
  
The relationship is used to assign a document reference or a more detailed
document information to objects. A single document reference can be applied to
multiple objects.  
  
The inherited attribute _RelatedObjects_ define the objects to which the
document association is applied. The attribute _RelatingDocument_ is the
reference to a document reference, applied to the object(s).  
  
> HISTORY  New entity in IFC2x.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifckernel/lexical/ifcrelassociatesdocument.htm)


Attribute definitions
---------------------
| Attribute        | Description                                                        |
|------------------|--------------------------------------------------------------------|
| RelatingDocument | Document information or reference which is applied to the objects. |

Associations
------------
| Attribute        | Description   |
|------------------|---------------|
| RelatingDocument |               |
| RelatingDocument |               |

