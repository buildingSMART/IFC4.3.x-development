Object User Identity
====================

An object may be labeled for human identification where the _Name_ may indicate a well-known identifier. While there is no restriction on usage of such identifier, it is recommended the _Name_ is unique within it's containing scope. Further guidance on usage is provided at specific entities; for example, for spaces, the _Name_ may reflect a room number. An object may have a description provided via the _Description_ attribute that provides further context in identifying or locating the object.

Specific subtypes introduce additional attributes for _User Identity_.

* Spatial objects may be further identified via the _LongName_ attribute. This value should generally correspond to building signage describing floor levels or rooms. While the _Name_ attribute generally provides a coded or abbreviated identifier, the _LongName_ provides a functional name for the location such as "Reception Area". See concept template _Spatial Element Occurrence Attributes_
* Physical elements may be further identified via the _Tag_ attribute. This is a human readable identifier such as an element or item number While there is no restriction on usage of such tags, it is recommended the _Tag_ is unique within it's containing scope. See concept template _Element Occurrence Attributes_

```
concept {
    IfcObject:Name -> IfcLabel
    IfcObject:Description -> IfcText
    IfcObject:IsTypedBy -> IfcRelDefinesByType:RelatedObjects
    IfcRelDefinesByType:RelatingType -> IfcTypeObject
    IfcTypeObject:Name -> IfcLabel
    IfcTypeObject:Description -> IfcText
}
```
