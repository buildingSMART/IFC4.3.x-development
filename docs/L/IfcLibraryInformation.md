IfcLibraryInformation
=====================
An _IfcLibraryInformation_ describes a library where a library is a structured
store of information, normally organized in a manner which allows information
lookup through an index or reference value. _IfcLibraryInformation_ provides
the library _Name_ and optional _Description_, _Version_, _VersionDate_ and
_Publisher_ attributes. A _Location_ may be added for electronic access to the
library.  
  
In a broder sense, _IfcLibraryInformation_ includes the meta data for capture
the revision information when checking in library and other data into a
revision control system.  
  
> HISTORY  New entity in IFC2x.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  _Location_ and _Description_ attributes added; _Publisher_ and
> _VersionDate_ data type changed; _HasLibraryReferences_ inverse attribute
> added (previous LibraryReference changed to inverse).  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcexternalreferenceresource/lexical/ifclibraryinformation.htm)


Attribute definitions
---------------------
| Attribute             | Description                                                                                                                                                                                                   |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HasLibraryReferences  |                                                                                                                                                                                                               |
| LibraryInfoForObjects |                                                                                                                                                                                                               |
| Name                  | The name which is used to identify the library.                                                                                                                                                               |
| Version               | Identifier for the library version used for reference.                                                                                                                                                        |
| Publisher             | Information of the organization that acts as the library publisher.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  The data type has been changed to _IfcActorSelect_.                                              |
| VersionDate           | Date of the referenced version of the library.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  The data type has been changed to _IfcDateTime_, the date and time string according to ISO8601.                       |
| Location              | Resource identifier or locator, provided as URI, URN or URL, of the library information for online references.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  New attribute added at the end of the attribute list. |
| Description           | Additional description provided for the library revision information.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  New attribute added at the end of the attribute list.                                          |

