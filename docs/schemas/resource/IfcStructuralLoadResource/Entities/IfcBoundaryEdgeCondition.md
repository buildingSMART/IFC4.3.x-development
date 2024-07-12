# IfcBoundaryEdgeCondition

Describes linearly elastic support conditions or connection conditions.<!-- end of definition -->

Applicability:

* Curve supports and connections.

> HISTORY New entity in IFC2x2.
> IFC 2x4 change: Attributes _LinearStiffnessX/Y/Z_ renamed to _TranslationalStiffnessX/Y/Z_.

{ .change-ifc2x4}
> IFC4 change All attribute data types changed from numeric to SELECT between Boolean and numeric. Stiffnesses may now also be negative, for example to capture destabilizing effects in boundary conditions. The IFC2x3 convention of -1. representing infinite stiffness is no longer valid and must not be used. Infinite stiffness, i.e. fixed supports, are now modeled by the Boolean value TRUE.

## Attributes

### TranslationalStiffnessByLengthX
Translational stiffness value in x-direction of the coordinate system defined by the instance which uses this resource object.

### TranslationalStiffnessByLengthY
Translational stiffness value in y-direction of the coordinate system defined by the instance which uses this resource object.

### TranslationalStiffnessByLengthZ
Translational stiffness value in z-direction of the coordinate system defined by the instance which uses this resource object.

### RotationalStiffnessByLengthX
Rotational stiffness value about the x-axis of the coordinate system defined by the instance which uses this resource object.

### RotationalStiffnessByLengthY
Rotational stiffness value about the y-axis of the coordinate system defined by the instance which uses this resource object.

### RotationalStiffnessByLengthZ
Rotational stiffness value about the z-axis of the coordinate system defined by the instance which uses this resource object.
