IfcDocumentReference
====================
An _IfcDocumentReference_ is a reference to the location of a document. The
reference is given by a system interpretable _Location_ attribute (a URL
string) where the document can be found, and an optional inherited internal
reference _Identification_, which refers to a system interpretable position
within the document. The optional inherited _Name_ attribute is meant to have
meaning for human readers. Optional document metadata can also be captured
through reference to _IfcDocumentInformation_.  
  
> HISTORY  New entity in IFC2.0  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcexternalreferenceresource/lexical/ifcdocumentreference.htm)


Attribute definitions
---------------------
| Attribute             | Description                                                                                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ReferencedDocument    |                                                                                                                                                                  |
| DocumentRefForObjects |                                                                                                                                                                  |
| Description           | Description of the document reference for informational purposes.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  New attribute added at the end of the attribute list. |

