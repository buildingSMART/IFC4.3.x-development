# IfcBuildingElementProxyType

_IfcBuildingElementProxyType_ defines a list of commonly shared property set definitions of a building element proxy and an optional set of product representations. It is used to define an element specification (i.e. the specific product information, that is common to all occurrences of that product type).<!-- end of definition -->

> NOTE The product representations are defined as representation maps (at the level of the supertype _IfcTypeProduct_, which gets assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[1]_ being an _IfcMappedItem_.

A building element proxy type is used to define the common properties of a certain type of a building element proxy that may be applied to many instances of that type to assign a specific style. Building element proxy types may be exchanged without being already assigned to occurrences.

> NOTE Although an building element proxy does not have a predefined ontological meaning the provision of a type may be helpful in sharing information among multiple occurrences. Applications that provide type information for element types not yet included in the current IFC specification can use the _IfcBuildingElementProxyType_ to exchange such types.

The occurrences of the _IfcBuildingElementProxyType_ are represented by instances of _IfcBuildingElementProxy_.

> HISTORY New entity in IFC2x3.

## Attributes

### PredefinedType
Predefined types to define the particular type of an building element proxy. There may be property set definitions available for each predefined or user defined type.

## Formal Propositions

### CorrectPredefinedType
The inherited attribute _ElementType_ shall be provided, if the _PredefinedType_ is set to USERDEFINED.

## Concepts

### Type Body Geometry



