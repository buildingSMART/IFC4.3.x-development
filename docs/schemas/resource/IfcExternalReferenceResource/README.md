IfcExternalReferenceResource
============================

The _IfcExternalReferenceResource_ provides the means to access or use information from external sources including:

* Classifications
* Documents
* Libraries

### 8.6.1.1 Classifications
A classification is a label having a value whose meaning is determined in an index or classification system. Values and meanings may be declared externally or they may be directly declared within an exchange file. It provides for:

* one or more classification notations to an object.
* one or more facets to a classification notation.
* referencing of facets of a classification notation from a described source (classification item or classification table)
* exposure of the hierarchy of a classification structure.
* identification of the classification source
* referencing a classification held on an external source.

### 8.6.1.2 Documents
The scope of the documents model is:

* to manage reference to documents
* to manage information about documents
* to be equally applicable to documents that are paper based or digital

It is not intended to be a complete document model and does not overlap in intent or content with such models.

Information may be referenced from external sources. Reference to a document is by its location (address) to enable access through mechanisms such as the World Wide Web. This is done through the _IfcDocumentReference_ class. This is a type of _IfcExternalReference_ that has a label (which can be the reference address) and identifier. Additionally, a name attribute provides the document with a human readable extension or qualifier to the location. Information concerning the document itself can also be stored as an attribute of the document reference.

Information about a document can be captured in the _IfcDocumentInformation_ class. This identifies and names the document and document owner. It may also include for the document:

* description
* revision identifier
* creation and revision times
* duration of document validity using 'valid from' and 'valid to' attributes.

Documents frequently hold references to information held in other documents, for example, documents referencing standards that are also documents. A significant tree structure of document information referencing could be built up in this way. Such relationships between document information can be captured through the _IfcDocumentInformationRelationship_ class which manages both relating and related document information and inversely captures the document information carrying the pointer and the document information to which pointers refer.

### 8.6.1.3 Libraries
The scope of the library model is to be able to reference information stored in external data libraries. It is assumed that, most frequently, information will populate property sets within an IFC model and that many of these property sets will be defined outside of this specification.

The _IfcLibraryInformation_ entity provides specific information about an actual library data source including its name, version, version date, publisher and publication location. Additionally it can be assigned to high level objects in a Building Information Model such as a Project or Building where there may be a need to identify the library used.

The _IfcLibraryReference_ entity is more widely used (and should be considered as the default selection). A library reference provides for the identifying of a specific record within a library data source through use of a name, location (web location) and item reference (which locates the data within the library data source). The provision of a language attribute allows the language in which a library reference is expressed to be identified

> HISTORY  New schema in IFC2x.
