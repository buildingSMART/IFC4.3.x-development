IfcArchitectureDomain
=====================

The _IfcArchitectureDomain_ schema defines basic object concepts used in the architectural domain that have not been generalized and pushed lower in the model (such as shared with other domains or application types).

> NOTE&nbsp; Most elements used in the architectural domain are shared with other domains and are consequentially declared in lower level schemas, such as _IfcProductExtension_, or _IfcSharedBldgElements_.

Specific architectural elements that are not already covered by other schemas are defined here:

* door lining and panel parameters allowing for a limited parametric description of door shape and operation,
* window lining and panel parameters allowing for a limited parametric description of window shape and operation,
* specific permeable covering properties for window and door openings

These parameter definitions are used to enhance the specification of door and window elements, they are applied to _IfcDoorType_ and _IfcWindowType_ using the _HasPropertySets_ relation.

> HISTORY&nbsp; New schema in IFC1.5

{ .deprecated}
> DEPRECATION&nbsp; Use of _IfcDoorStyle_ and _IfcWindowStyle_ is deprecated. Use _IfcDoorType_ and _IfcWindowType_ instead.
