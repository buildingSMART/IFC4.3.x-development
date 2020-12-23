# IfcLibraryReference

An _IfcLibraryReference_ is a reference into a library of information by _Location_ (provided as a URI). It also provides an optional inherited _Identification_ key to allow more specific references to library sections or tables. The inherited _Name_ attribute allows for a human interpretable identification of the library item. Also, general information on the library from which the reference is taken, is given by the _ReferencedLibrary_ relation which identifies the relevant occurrence of _IfcLibraryInformation_.

The _ifcLibraryReference_ additionally provides the capability to handle multilingual library entries. The _Language_ attribute then holds the language tag for the language used by the strings kept in the _Name_ and the _Description_ attribute.

> HISTORY&nbsp; New entity in IFC2.0.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; _Description_ and _Language_ attribute added; _ReferencedLibrary_ attribute added (reversing previous ReferenceIntoLibrary inverse relationship).

## Attributes

### Description
Additional description provided for the library reference.
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; New attribute added at the end of the attribute list.

### Language
The language in which a library reference is expressed.
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; New attribute added at the end of the attribute list.

### ReferencedLibrary
The library information that is being referenced.

### LibraryRefForObjects
The library reference with which objects are associated.
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; New inverse attribute.
