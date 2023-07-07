Spatial Element Type Predefined Type
====================================

If a custom value is needed to describe a spatial element type, the attribute _ElementType_ may be used to define such custom type, where the _PredefinedType_ is set to _USERDEFINED_.

Specific subtypes introduce additional attributes for the _Object User Identity_ template.

* Spatial element type sub types may be further identified via the _Tag_ attribute. While there is no restriction on usage of such tags, it is recommended the _Tag_ is unique within its containing scope.
* Spatial element type sub types may be further attributed via the _LongName_ attribute. While the _Name_ attribute generally provides a coded or abbreviated identifier, the _LongName_ provides a functional name for the location such as "Reception Area".

> NOTE  Since the corresponding occurrences of _IfcSpatialElementType_ do not have a _Tag_ attribute, it is recommended not to use it here.

```
concept {
    IfcSpatialElementType:ElementType -> IfcLabel_0
    IfcSpatialElementType:Tag -> IfcLabel_1
}
```
