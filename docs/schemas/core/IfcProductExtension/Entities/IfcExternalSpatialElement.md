# IfcExternalSpatialElement

The external spatial element defines external regions at the building site. Those regions can be defined:

* logically - for example, an instance of _IfcExternalSpatialElement_ could represent the air space around the building without having an own shape representation, or
* physically - for example, an instance of _IfcExternalSpatialElement_ could represent the sloping ground around the building to identify the part of the external building envelop that is below ground.
<!-- end of short definition -->

> HISTORY New entity in IFC4.

## Attributes

### PredefinedType
Predefined generic types for an external spatial element that are specified in an enumeration. There might be property sets defined specifically for each predefined type.

### BoundedBy
Reference to a set of _IfcRelSpaceBoundary_ entities that defines the physical or virtual delimitation of that external spatial element against physical or virtual boundaries.
