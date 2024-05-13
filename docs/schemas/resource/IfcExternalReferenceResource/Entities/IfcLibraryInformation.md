# IfcLibraryInformation

An _IfcLibraryInformation_ describes an external structured store of information, normally organized in a manner which allows information lookup through an index or reference value. _IfcLibraryInformation_ provides the library _Name_ and optional _Description_, _Version_, _VersionDate_ and _Publisher_ attributes. A _Location_ may be added for electronic access to the library.<!-- end of definition -->

> EXAMPLE A library may be an external network of elements in a Building Automation System structured using BACnet or Brickschema. Alternatively, a library may reference an external revision control system. A library may also reference an arbitrary external database.

> HISTORY  New entity in IFC2x.

{ .change-ifc2x4}
> IFC4 CHANGE  _Location_ and _Description_ attributes added; _Publisher_ and _VersionDate_ data type changed; _HasLibraryReferences_ inverse attribute added (previous LibraryReference changed to inverse).

> IFC4.3.0.0 CHANGE IfcLibraryInformation now is explicitly defined for use to reference external systems.

## Attributes

### Name
The name which is used to identify the library.

### Version
Identifier for the library version used for reference.

### Publisher
Information of the organization that acts as the library publisher.
{ .change-ifc2x4}
> IFC4 CHANGE  The data type has been changed to _IfcActorSelect_.

### VersionDate
Date of the referenced version of the library.
{ .change-ifc2x4}
> IFC4 CHANGE  The data type has been changed to _IfcDateTime_, the date and time string according to ISO8601.

### Location
Resource identifier or locator, provided as URI, URN or URL, of the library information for online references.
{ .change-ifc2x4}
> IFC4 CHANGE  New attribute added at the end of the attribute list.

### Description
Additional description provided for the library revision information.
{ .change-ifc2x4}
> IFC4 CHANGE  New attribute added at the end of the attribute list.

### LibraryInfoForObjects
The library information with which objects are associated.
{ .change-ifc2x4}
> IFC4 CHANGE  New inverse attribute.

### HasLibraryReferences
The library references to which the library information applies.
