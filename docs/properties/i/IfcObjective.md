IfcObjective
============

An _IfcObjective_ captures qualitative information for an objective-based constraint.

_IfcObjective_ is a subtype of _IfcConstraint_ and may be associated with any subtype of _IfcRoot_ through the _IfcRelAssociatesConstraint_ relationship in the _IfcControlExtension_ schema, or may be associated with _IfcProperty_ by _IfcResourceConstraintRelationship_.

The aim of _IfcObjective_ is to specify the purpose for which the constraint is applied and to capture the benchmark metrics of the constraint.

> HISTORY&nbsp; New entity in IFC2.0.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Attribute _BenchmarkValues_ modified to be a LIST of _IfcConstraint_, attribute _ResultValues_ replaced with _IfcLogicalOperatorEnum_.
