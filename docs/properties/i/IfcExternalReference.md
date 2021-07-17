IfcExternalReference
====================

An _IfcExternalReference_ is the identification of information that is not explicitly represented in the current model or in the project database (as an implementation of the current model). Such information may be contained in classifications, documents or libraries. The _IfcExternalReference_ identifies a particular item, such as a dictionary entry, a classification notation, or a document reference within the external source.

Only the _Location_ (as a URL) is given to describe the place where the information can be found. Also an optional _Identification_ as a key to allow more specific references (as to sections or tables) is provided. The _Identification_ defines a system interpretable method to identify the relevant part of information at the source. In addition a human interpretable _Name_ can be assigned to identify the information subject, such as a classification code.

_IfcExternalReference_ is an abstract supertype of all external reference entities.

> HISTORY&nbsp; New entity in IFC2x.

{ .change-ifc2x4}
> IFC 2x4 CHANGE&nbsp; Attribute _Identification_ renamed from ItemReference, attribute _Location_ datatype changed, and inverse attribute _ExternalReferenceForResources_ added.
