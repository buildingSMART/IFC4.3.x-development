IfcBoundaryNodeConditionWarping
===============================
Describes linearly elastic support conditions or connection conditions,
including linearly elastic warping restraints.  
  
Applicability:  
  
* Point supports and connections.  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  All attribute data types changed from numeric to SELECT between
> Boolean and numeric. Stiffnesses may now also be negative, for example to
> capture destabilizing effects in boundary conditions. The IFC2x3 convention
> of -1. representing infinite stiffness is no longer valid and must not be
> used. Infinite stiffness, i.e. fixed supports, are now modeled by the
> Boolean value TRUE.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralloadresource/lexical/ifcboundarynodeconditionwarping.htm)


