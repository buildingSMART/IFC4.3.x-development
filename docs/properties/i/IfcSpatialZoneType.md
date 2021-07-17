IfcSpatialZoneType
==================

The _IfcSpatialZoneType_ defines a list of commonly shared property set definitions of a space and an optional set of product representations. It is used to define a space specification (i.e. the specific space information, that is common to all occurrences of that space type).

> NOTE&nbsp; The product representations are defined as representation maps (at the level of the supertype _IfcTypeProduct_, which gets assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[1]_ being an _IfcMappedItem_.

A spatial zone type is used to define the common properties of a certain type of space that may be applied to many instances of that type to assign a specific style. Space types may be exchanged without being already assigned to occurrences.

> NOTE&nbsp; The spatial zone types are often used to represent space catalogues, less so for sharing a common representation map. Spatial zone types in a space catalogue share same space classification and a common set of space requirement properties.

The occurrences of _IfcSpatialZoneType_ are represented by instances of _IfcSpatialZone_.

> HISTORY&nbsp; New entity in IFC4.
