# IfcMetric

An _IfcMetric_ is used to capture quantitative resultant metrics that can be applied to objectives.

_IfcMetric_ is a subtype of _IfcConstraint_ and may be associated with any subtype of _IfcRoot_ through the _IfcRelAssociatesConstraint_ relationship in the _IfcControlExtension_ schema, or may be associated with _IfcProperty_ by _IfcResourceConstraintRelationship_.

The aim of _IfcMetric_ is to capture the quantitative aspects of a constraint.

> HISTORY  New entity in IFC2.0.

{ .change-ifc2x4}
> IFC4 CHANGE  ReferencePath attribute added for indicating the value to be constrained along a path of attribute references.

## Attributes

### Benchmark
Enumeration that identifies the type of benchmark data.

### ValueSource
Reference source for data values.

If _DataValue_ refers to an _IfcTable_, this attribute identifies the relevent column identified by _IfcTableColumn_._Identifier_.

### DataValue
The value to be compared on associated objects. A null value indicates comparison to null.
{ .change-ifc4}
> IFC4 ADD1 CHANGE  This attribute is now optional.

### ReferencePath
Optional path to an attribute to be constrained on associated objects.
If provided, the metric may be validated by resolving the path to the current value on associated object(s), and comparing such value with _DataValue_ according to the _Benchmark_.
