# IfcLinearPlacement

_IfcLinearPlacement_ provides a specialization of _IfcObjectPlacement_ in which the placement and axis direction of the object coordinate system is defined by a reference to a curve. RelativePlacement is therefore restricted to _IfcAxis2PlacementLinear_.

## Attributes

### RelativePlacement
Placement that provides location and orientation confined to the context of a curve. Linear placement is 3D in nature even in case of a 2D basis curve.

### CartesianPosition
Optional fallback for the `RelativePlacement` attribute, which may be used by importing applications that do not support linear placement.