IfcMetric
=========

An _IfcMetric_ is used to capture quantitative resultant metrics that can be applied to objectives.

_IfcMetric_ is a subtype of _IfcConstraint_ and may be associated with any subtype of _IfcRoot_ through the _IfcRelAssociatesConstraint_ relationship in the _IfcControlExtension_ schema, or may be associated with _IfcProperty_ by _IfcResourceConstraintRelationship_.

The aim of _IfcMetric_ is to capture the quantitative aspects of a constraint.

> HISTORY&nbsp; New entity in IFC2.0.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; ReferencePath attribute added for indicating the value to be constrained along a path of attribute references.
