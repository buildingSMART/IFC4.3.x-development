Object Predefined Type
======================

Many object occurrences have an attribute named _PredefinedType_ being a specific enumeration. Such predefined type essentially provides another level of "classification by inheritance" to further differentiate objects without the need for additional sub types. Predefined types are not just informational; various rules apply such as applicable property sets, part composition, and distribution ports. Such predefined types are added by selecting the correct enumerator for the attribute _PredefinedType_. If a custom value is needed, the attribute _ObjectType_ has to be used to define such custom type, whereas the _PredefinedType_ is set to _USERDEFINED_.

The main attributes to be provided for an _Object Occurrence Predefined Type_ are:

* _PredefinedType_: holds the entity specific enumeration of predefined types to further classify the entity
* _ObjectType_: allows for a custom value, if no applicable enumerator can be found



 If the object is typed by an _IfcTypeObject_, then the _PredefinedType_ at the _IfcObject_ occurrence shall only be used if the _PredefinedType_ at _IfcTypeObject_ is set to _NOTDEFINED_.

```
concept {
    IfcObject:ObjectType -> IfcLabel
    IfcObject:IsTypedBy -> IfcRelDefinesByType:RelatedObjects
    IfcRelDefinesByType:RelatingType -> IfcTypeObject
    IfcObject:ObjectType[binding="UserDefinedType"]
    IfcObject:PredefinedType[binding="PredefinedType"]
    IfcTypeObject:ElementType[binding="TypeUserdefinedType"]
    IfcTypeObject:PredefinedType[binding="TypePredefinedType"]
}
```
