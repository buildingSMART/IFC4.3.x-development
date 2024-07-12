# IfcBuiltElementType

The _IfcBuiltElementType_ provides the type information for _IfcBuiltElement_ occurrences.
<!-- end of short definition -->

> NOTE The product representations are defined as representation maps (at the level of the supertype _IfcTypeProduct_, which gets assigned by an element occurrence instance through the _IfcShapeRepresentation.Item[1]_ being an _IfcMappedItem_.

A built element type is used to define the common properties of a certain type of built element that are applied to all occurrences of that type. It is used to define a built element specification (i.e. the specific product information, that is common to all occurrences of that product type). Built element types (or the instantiable subtypes) may be exchanged without being already assigned to occurrences.

The _IfcBuiltElementType_ can be instantiated in the case when arbitrary built element types cannot be expressed by a subtype of _IfcBuiltElementType_.

> NOTE The deprecated _IfcBuildingElementProxyType_ shall not be used to represent any arbitrary built element type, use a direct instantiation of _IfcBuiltElementType_ instead.

Occurrences of subtypes of the _IfcBuiltElementType_ are represented by instances of the appropriate subtypes of _IfcBuiltElement_.

> HISTORY New entity in IFC2x2.

> IFC4.3.0.0 CHANGE The entity has been renamed from IfcBuildingElementType and made non abstract.
