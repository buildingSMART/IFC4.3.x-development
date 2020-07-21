IfcMetric
=========
An _IfcMetric_ is used to capture quantitative resultant metrics that can be
applied to objectives.  
  
_IfcMetric_ is a subtype of _IfcConstraint_ and may be associated with any
subtype of _IfcRoot_ through the _IfcRelAssociatesConstraint_ relationship in
the _IfcControlExtension_ schema, or may be associated with _IfcProperty_ by
_IfcResourceConstraintRelationship_.  
  
The aim of _IfcMetric_ is to capture the quantitative aspects of a constraint.  
  
> HISTORY  New entity in IFC2.0.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  ReferencePath attribute added for indicating the value to be
> constrained along a path of attribute references.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcconstraintresource/lexical/ifcmetric.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                                    |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Benchmark   | Enumeration that identifies the type of benchmark data.                                                                                                                        |
| ValueSource | Reference source for data values. \X\0D\X\0DIf _DataValue_ refers to an _IfcTable_, this attribute identifies the relevent column identified by _IfcTableColumn_._Identifier_. |
| DataValue   | The value to be compared on associated objects. A null value indicates comparison to null.\X\0D{ .change-ifc4}\X\0D> IFC4 ADD1 CHANGE  This attribute is now optional.         |

Associations
------------
| Attribute     | Description   |
|---------------|---------------|
| ReferencePath |               |

