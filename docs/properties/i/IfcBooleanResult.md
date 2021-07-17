IfcBooleanResult
================

The _IfcBooleanResult_ is the result of applying a Boolean operation to two operands being solids.

> EXAMPLE&nbsp; If the first operand is a block and the second operand is a solid cylinder of suitable dimensions and location, the boolean result produced with the difference operator would be a block with a circular hole.

{ .extDef}
> NOTE&nbsp; Definition according to ISO/CD 10303-42:1992  
> A Boolean result is the result of a regularized operation on two solids to create a new solid. Valid operations are regularized union, regularized intersection, and regularized difference. For purpose of Boolean operations, a solid is considered to be a regularized set of points. The final Boolean result depends upon the operation and the two operands. In the case of the difference operator the order of the operands is also significant. The operator can be either union, intersection or difference. The effect of these operators is described below: > * Union on two solids is the new solid that is the regularization of the set of all points that are in either the first operand or the second operand or in both.
> * Intersection on two solids is the new solid that is the regularization of the set of all points that are in both the first operand and the second operand.
> * The result of the difference operation on two solids is the regularization of the set of all points which are in the first operand, but not in the second operand.

> NOTE&nbsp; Corresponding STEP type **boolean_result** defined in ISO 10303-42.

> HISTORY&nbsp; New entity in IFC1.5.1.
