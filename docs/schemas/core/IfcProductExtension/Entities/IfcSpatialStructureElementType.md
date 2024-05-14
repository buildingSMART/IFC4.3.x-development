# IfcSpatialStructureElementType

The element type (_IfcSpatialStructureElementType_) defines a list of commonly shared property set definitions of a spatial structure element and an optional set of product representations. It is used to define an element specification (i.e. the specific element information, that is common to all occurrences of that element type).<!-- end of definition -->

> NOTE  The product representations are defined as representation maps (at the level of the supertype _IfcTypeProduct_, which gets assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[1]_ being an _IfcMappedItem_.
>

A spatial structure element type is used to define the common properties of a certain type of a spatial structure element that may be applied to many instances of that type to assign a specific style. Spatial structure element types (the instantiable subtypes) may be exchanged without being already assigned to occurrences.

> NOTE  The spatial structure element types are often used to represent catalogues of predefined spatial types for shared attributes, less so for sharing a common representation map.

The occurrences of subtypes of the abstract _IfcSpatialStructureElementType_ are represented by instances of subtypes of _IfcSpatialStructureElement_.

> HISTORY  New entity in IFC2x3.
