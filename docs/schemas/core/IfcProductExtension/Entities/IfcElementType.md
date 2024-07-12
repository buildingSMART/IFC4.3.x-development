# IfcElementType

_IfcElementType_ defines a list of commonly shared property set definitions of an element and an optional set of product representations. It is used to define an element specification (i.e. the specific product information, that is common to all occurrences of that product type).
<!-- end of short definition -->


> NOTE The product representations are defined as representation maps (at the level of the supertype _IfcTypeProduct_, which gets assigned by an element instance through the _IfcShapeRepresentation.Item[1]_ being an _IfcMappedItem_.

An element type is used to define the common properties of a certain type or style of an element that may be applied to instances of that element type to assign a specific style. Element types (the instantiable subtypes) may be exchanged without being already assigned to occurrences.

> HISTORY New entity in IFC2x2

## Attributes

### ElementType
The type denotes a particular type that indicates the object further. The use has to be established at the level of instantiable subtypes. In particular it holds the user defined type, if the enumeration of the attribute 'PredefinedType' is set to USERDEFINED.

## Concepts

### Element Type Predefined Type



### Type Body AdvancedBrep Geometry



### Type Body Brep Geometry



### Type Body CSG Geometry



### Type Body Tessellated Geometry



### Type Element Aggregation



