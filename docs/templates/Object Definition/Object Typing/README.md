Object Typing
=============

Object occurrences can be defined by a particular object type, using the _Object Typing_ concept. A pair of entities are defined for most semantic objects - an object occurrence entity and a corresponding object type entity.

> EXAMPLE  The _IfcTank_ is the object occurrence entity that has a corresponding _IfcTankType_ being the object type entity.

On instance level, an object occurrence instance may have:

* similar state as its object type instance by applying all characteristics defined at the type;
* overridden state for particular characteristics;
* no defined object type instance.

Characteristics defined at the object type level may include:

* common naming and predefined type;
* common properties within a type driven property set;
* common geometry representations, applied as mapped representation to each occurrences;
* common material assignments (with exception of material set usages);
* common definition of a decomposition structure.

Many object occurrence and object type entities have an attribute named _PredefinedType_ consisting of a specific enumeration. Such predefined type essentially provides another level of inheritance to further differentiate objects without the need for additional entities. Predefined types are not just informational; various rules apply such as applicable property sets, part composition, and distribution ports. If the object is typed by an _IfcTypeObject_, then the _PredefinedType_ at the _IfcObject_ occurrence shall only be used if the _PredefinedType_ at _IfcTypeObject_ is set to _NOTDEFINED_.

> EXAMPLE  For scenarios of object types having part compositions, such parts may be reflected at object occurrences having separate state. For example, a _wall type_ may define a particular arrangement of studs, a _wall occurrence_ may reflect the same arrangement of studs, and studs within the wall occurrence may participate in specific relationships that do not exist at the type such as being connected to an electrical junction box.

> NOTE  If the object type has aggregated elements, such objects are reflected at the object occurrence using the _IfcRelDefinesByObject_ relationship.

```
concept {
    IfcObject:IsTypedBy -> IfcRelDefinesByType:RelatedObjects
    IfcRelDefinesByType:RelatingType -> IfcTypeObject
    IfcObject:IsTypedBy[binding="HasType"]
    IfcRelDefinesByType:RelatingType[binding="RelatingType"]
    IfcTypeObject:Name[binding="TypeName"]
}
```
