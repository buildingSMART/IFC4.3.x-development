# IfcDocumentInformation

_IfcDocumentInformation_ captures "metadata" of an external document. The actual content of the document is not defined in this specification; instead, it can be found following the _Location_ attribute.

The same _IfcDocumentInformation_ can be referenced from the exchange structure in total or in parts (e.g. by refering to particular chapters or paragraphs) using the _IfcDocumentReference_. All _IfcDocumentReference_'s that utilize the _IfcDocumentInformation_ are accessible by the inverse relationship _HasDocumentReferences_.

> HISTORY&nbsp; New entity in IFC2x.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Attribute _HasDocumentReferences_ changed to be inverse, attribute _Location_ added, and attribute _ElectronicFormat_ modified.

## Attributes

### Identification
Identifier that uniquely identifies a document.
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Attribute renamed from _DocumentId_.

### Name
File name or document name assigned by owner.

### Description
Description of document and its content.

### Location
Resource identifier or locator, provided as URI, URN or URL, of the document information for online references.
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; New attribute added at the place of the removed attribute _DocumentReferences_.

### Purpose
Purpose for this document.

### IntendedUse
Intended use for this document.

### Scope
Scope for this document.

### Revision
Document revision designation.

### DocumentOwner
Information about the person and/or organization acknowledged as the 'owner' of this document. In some contexts, the document owner determines who has access to or editing right to the document.

### Editors
The persons and/or organizations who have created this document or contributed to it.

### CreationTime
Date and time stamp when the document was originally created.
{ .change-ifc2x4}
> IFC4 CHANGE The data type has been changed to _IfcDateTime_, the date time string according to ISO8601.

### LastRevisionTime
Date and time stamp when this document version was created.
{ .change-ifc2x4}
> IFC4 CHANGE The data type has been changed to _IfcDateTime_, the date time string according to ISO8601.

### ElectronicFormat
Describes the media type used in various internet protocols, also referred to as "Content-type", or "MIME-type (Multipurpose Internet Mail Extension), of the document being referenced. It is composed of (at least) two parts, a type and a subtype.
> NOTE&nbsp; The iana (Internet Assigned Numbers Authority) published the media types.

> EXAMPLE&nbsp; 'image/png' denotes an image type of png (Portable Network Graphics) subtype, 'application/pdf' denotes an application specific type of pdf (Portable Document Format) subtype

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The data type has been changed from entity data type to _IfcIdentifier_.

### ValidFrom
Date when the document becomes valid.
{ .change-ifc2x4}
> IFC4 CHANGE The data type has been changed to _IfcDate_, the date string according to ISO8601.

### ValidUntil
Date until which the document remains valid.
{ .change-ifc2x4}
> IFC4 CHANGE The data type has been changed to _IfcDate_, the date string according to ISO8601.

### Confidentiality
The level of confidentiality of the document.

### Status
The current status of the document. Examples of status values that might be used for a document information status include:  
- DRAFT  
- FINAL DRAFT  
- FINAL  
- REVISION

### DocumentInfoForObjects
The document information with which objects are associated.
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; New inverse attribute.

### HasDocumentReferences
The document references to which the document applies

### IsPointedTo
An inverse relationship from the IfcDocumentInformationRelationship to the related documents./EPM-HTML>

### IsPointer
An inverse relationship from the IfcDocumentInformationRelationship to the relating document.
