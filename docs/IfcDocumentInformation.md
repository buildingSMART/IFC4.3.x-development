IfcDocumentInformation
======================
_IfcDocumentInformation_ captures "metadata" of an external document. The
actual content of the document is not defined in this specification; instead,
it can be found following the _Location_ attribute.  
  
The same _IfcDocumentInformation_ can be referenced from the exchange
structure in total or in parts (e.g. by refering to particular chapters or
paragraphs) using the _IfcDocumentReference_. All _IfcDocumentReference_''s
that utilize the _IfcDocumentInformation_ are accessible by the inverse
relationship _HasDocumentReferences_.  
  
> HISTORY  New entity in IFC2x.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Attribute _HasDocumentReferences_ changed to be inverse,
> attribute _Location_ added, and attribute _ElectronicFormat_ modified.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcexternalreferenceresource/lexical/ifcdocumentinformation.htm)


