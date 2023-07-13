Object Type Predefined Type
===========================

Many object occurrence and object type entities have an attribute named _PredefinedType_ consisting of a specific enumeration. Such predefined type essentially provides another level of inheritance to further differentiate objects without the need for additional entities. Predefined types are not just informational; various rules apply such as applicable property sets, part composition, and distribution ports. If the object is typed by an _IfcTypeObject_, then the _PredefinedType_ at the _IfcObject_ occurrence shall only be used if the _PredefinedType_ at _IfcTypeObject_ is set to _NOTDEFINED_.

Note that the PredefinedType attribute itself is defined at the leaf classes of the inheritance hierarchy with a specific enumeration attribute for that given leaf class.

```
concept {
    IfcTypeObject:Types -> IfcRelDefinesByType:RelatingType
    IfcRelDefinesByType:RelatedObjects -> IfcObject:IsTypedBy
    IfcObject:ObjectType -> IfcLabel

    IfcTypeObject:ElementType[binding="TypeUserDefinedType"]
    IfcTypeObject:PredefinedType[binding="TypePredefinedType"]
    IfcObject:ObjectType[binding="UserDefinedType"]
    IfcObject:PredefinedType[binding="PredefinedType"]
}
```
