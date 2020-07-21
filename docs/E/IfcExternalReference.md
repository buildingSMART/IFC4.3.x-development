IfcExternalReference
====================
An _IfcExternalReference_ is the identification of information that is not
explicitly represented in the current model or in the project database (as an
implementation of the current model). Such information may be contained in
classifications, documents or libraries. The _IfcExternalReference_ identifies
a particular item, such as a dictionary entry, a classification notation, or a
document reference within the external source.  
  
Only the _Location_ (as a URL) is given to describe the place where the
information can be found. Also an optional _Identification_ as a key to allow
more specific references (as to sections or tables) is provided. The
_Identification_ defines a system interpretable method to identify the
relevant part of information at the source. In addition a human interpretable
_Name_ can be assigned to identify the information subject, such as a
classification code.  
  
_IfcExternalReference_ is an abstract supertype of all external reference
entities.  
  
> HISTORY  New entity in IFC2x.  
  
{ .change-ifc2x4}  
> IFC 2x4 CHANGE  Attribute _Identification_ renamed from ItemReference,
> attribute _Location_ datatype changed, and inverse attribute
> _ExternalReferenceForResources_ added.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcexternalreferenceresource/lexical/ifcexternalreference.htm)


Attribute definitions
---------------------
| Attribute      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Location       | Location, where the external source (classification, document or library) can be accessed by electronic means. The electronic location is provided as an URI, and would normally be given as an URL location string.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  The data type has been changed from _IfcLabel_ to _IfcURIReference_ \X\0D> .                                                                                                                                                                                                           |
| Identification | The _Identification_ provides a unique identifier of the referenced item within the external source (classification, document or library). It may be provided as \X\0D* a key, e.g. a classification notation, like NF2.3\X\0D* a handle\X\0D* a uuid or guid\X\0D\X\0D\X\0DIt may be human readable (such as a key) or not (such as a handle or uuid) depending on the context of its usage (which has to be determined by local agreement).\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE Attribute renamed from _ItemReference_ for consistency. \X\0D> |
| Name           | Optional name to further specify the reference. It can provide a human readable identifier (which does not necessarily need to have a counterpart in the internal structure of the document).                                                                                                                                                                                                                                                                                                                                                        |

Formal Propositions
-------------------
| Rule   | Description   |
|--------|---------------|
| WR1    |               |

Associations
------------
| Attribute                     | Description   |
|-------------------------------|---------------|
| ExternalReferenceForResources |               |

