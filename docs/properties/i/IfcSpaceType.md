IfcSpaceType
============

A space represents an area or volume bounded actually or theoretically. Spaces are areas or volumes that provide for certain functions within a building.

The _IfcSpaceType_ defines a list of commonly shared defines commonly shared information for occurrences of spaces. The set of shared information may include:

* common properties within shared property sets 
* common shape representations 

It is used to define an space specification (i.e. the specific space information, that is common to all occurrences of that space type. Space types may be exchanged without being already assigned to occurrences.

> NOTE&nbsp; The space types are often used to represent space catalogues, less so for sharing a common representation map. Space types in a space catalogue share same space classification and a common set of space requirement properties.

The occurrences of _IfcSpaceType_ are represented by instances of _IfcSpace_.

> HISTORY&nbsp; New entity in IFC2x3.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The attribute _LongName_ has been added to the end of the entity definition.
