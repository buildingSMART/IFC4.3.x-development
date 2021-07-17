IfcBoundaryNodeCondition
========================

Describes linearly elastic support conditions or connection conditions.

Applicability:

* Point supports and connections.

> HISTORY&nbsp; New entity in IFC2x2.  
> IFC 2x4 change: Attributes _LinearStiffnessX/Y/Z_ renamed to _TranslationalStiffnessX/Y/Z_.

{ .change-ifc2x4}
> IFC4 CHANGE All attribute data types changed from numeric to SELECT between Boolean and numeric. Stiffnesses may now also be negative, for example to capture destabilizing effects in boundary conditions. The IFC2x3 convention of -1. representing infinite stiffness is no longer valid and must not be used. Infinite stiffness, i.e. fixed supports, are now modeled by the Boolean value TRUE.
