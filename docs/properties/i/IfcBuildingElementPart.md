IfcBuildingElementPart
======================

_IfcBuildingElementPart_ represents major components as subordinate parts of a building element. Typical usage examples include precast concrete sandwich walls, where the layers may have different geometry representations. In this case the layered material representation does not sufficiently describe the element. Each layer is represented by an own instance of the _IfcBuildingElementPart_ with its own geometry description.

The kind of building element part is further specified by a corresponding instance of _IfcBuildingElementPartType_, referred to by _IfcRelDefinesByType_.

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Moved from _IfcStructuralElementsDomain_ schema to _IfcSharedComponentElements_ schema, compatible change of supertype, attribute _PredefinedType_ added.
