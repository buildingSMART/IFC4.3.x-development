# IfcSpatialElementType

_IfcSpatialElementType_ defines a list of commonly shared property set definitions of a spatial structure element and an optional set of product representations. It is used to define a spatial element specification (the specific element information, that is common to all occurrences of that element type).

> NOTE  The product representations are defined as representation maps (at the level of the supertype _IfcTypeProduct_, which gets assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[1]_ being an _IfcMappedItem_.

A spatial element type is used to define the common properties of a certain type of a spatial structure element that may be applied to many instances of that type to assign a specific style. Spatial element types (i.e. the instantiable subtypes) may be exchanged without being already assigned to occurrences.

> NOTE  The spatial element types are often used to represent catalogues of predefined spatial types for shared attributes, less so for sharing a common representation map.

The occurrences of subtypes of the abstract _IfcSpatialElementType_ are represented by instances of subtypes of the abstract _IfcSpatialElement_.

> HISTORY  New entity in IFC4.

## Attributes

### ElementType
The type denotes a particular type that indicates the object further. The use has to be established at the level of instantiable subtypes. In particular it holds the user defined type, if the enumeration of the attribute 'PredefinedType' is set to USERDEFINED.

## Concepts

### Spatial Element Type Predefined Type



