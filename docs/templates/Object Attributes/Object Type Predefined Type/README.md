Object Type Predefined Type
===========================

Many object occurrence and object type entities have an attribute named _PredefinedType_ consisting of a specific enumeration. Such predefined type essentially provides another level of inheritance to further differentiate objects without the need for additional entities. Predefined types are not just informational; various rules apply such as applicable property sets, part composition, and distribution ports. If the object is typed by an _IfcTypeObject_, then the _PredefinedType_ at the _IfcObject_ occurrence shall only be used if the _PredefinedType_ at _IfcTypeObject_ is set to _NOTDEFINED_.

```
concept {
}
```
