# IfcStructuralPlanarAction

This entity defines an action with constant value which is distributed over a surface.

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Intermediate supertype _IfcStructuralSurfaceAction_ inserted.

> NOTE&nbsp; Like its supertype _IfcStructuralSurfaceAction_, this action type may also act on curved faces.

## WhereRules

### SuitableLoadType
A planar action shall place either a planar force or a temperature load.

### ConstPredefinedType
This surface action subtype is restricted to constant load distribution over its domain.
