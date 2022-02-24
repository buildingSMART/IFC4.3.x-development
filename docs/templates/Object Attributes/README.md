Object Attributes
=================

All entities having semantic significance derive from _IfcRoot_, where instances are identifiable within a data set using a compressed globally unique identifier (IFC-GUID). This identifier must never change during the lifetime of an object, which allows data to be merged, versioned, or referenced from other locations.

Resource-level instances (not deriving from _IfcRoot_) do not have any identity, such that two instances having identical state are considered equal. For example, if an object has coordinates described by an _IfcCartesianPoint_ instance, another object with the same coordinates may have a separate instance of _IfcCartesianPoint_ or share the same instance; such difference is a matter of data storage optimization and does not imply any semantic relationship. This also implies that non-rooted instances may only exist if referenced by at least one rooted instance through either a direct attribute or inverse attribute, or following a chain of attribute references on instances.

The distinction between rooted and non-rooted (resource-level) entities achieves several goals:

{ .ref}
* File size may be reduced by interning (sharing) non-rooted data instances;
* Database retrieval may be more efficient by storing non-rooted data local to rooted data instances;
* Storage size may be reduced by avoiding IFC-GUID storage for items not requiring direct retrieval;
* Comparisons of differences may be done at a higher level where the context of such change is apparent;
* Implementations may treat non-rooted data instances as immutable for efficiency or simplified usage.
