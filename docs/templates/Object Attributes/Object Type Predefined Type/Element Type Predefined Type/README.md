Element Type Predefined Type
============================

If a custom value is needed to describe a physical object type, the attribute ElementType may be used to define such custom type, where the PredefinedType is set to USERDEFINED.

Physical element types may be further identified via the Tag attribute. This is a human readable identifier such as an element or item number. While there is no restriction on usage of such tags, it is recommended the Tag is unique within it's containing scope.

```
concept {
    IfcElementType:ElementType -> IfcLabel_0
    IfcElementType:Tag -> IfcLabel_1
}
```
