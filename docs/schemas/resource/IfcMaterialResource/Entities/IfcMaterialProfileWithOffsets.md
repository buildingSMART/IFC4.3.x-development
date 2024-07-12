# IfcMaterialProfileWithOffsets

_IfcMaterialProfileWithOffsets_ is a specialization of _IfcMaterialProfile_ with additional longitudinal offsets .<!-- end of definition -->

Relative positions of _IfcMaterialProfileWithOffsets_ in the longitudinal direction of an element can be defined giving offsets at the start at the end, or at start and end. This shall not be used for relative positions of individual profiles in the plane of profile definition, which is given in composite profile definition itself. Also, care should be taken especially when used with _IfcMaterialProfileSetUsageTapering_ for correct start and end offset assignment.

> HISTORY  New entity in IFC4.

## Attributes

### OffsetValues
The numerical value of profile offset, in the direction of the axis direction - always AXIS1 that is, the axis along the extrusion path. The _OffsetValues[1]_ identifies the offset from the lower position along the axis direction (normally the start of the standard extrusion), the _OffsetValues[2]_ identifies the offset from the upper position along the axis direction (normally the end of the standard extrusion).
