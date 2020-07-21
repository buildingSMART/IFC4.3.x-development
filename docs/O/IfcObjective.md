IfcObjective
============
An _IfcObjective_ captures qualitative information for an objective-based
constraint.  
  
_IfcObjective_ is a subtype of _IfcConstraint_ and may be associated with any
subtype of _IfcRoot_ through the _IfcRelAssociatesConstraint_ relationship in
the _IfcControlExtension_ schema, or may be associated with _IfcProperty_ by
_IfcResourceConstraintRelationship_.  
  
The aim of _IfcObjective_ is to specify the purpose for which the constraint
is applied and to capture the benchmark metrics of the constraint.  
  
> HISTORY  New entity in IFC2.0.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Attribute _BenchmarkValues_ modified to be a LIST of
> _IfcConstraint_, attribute _ResultValues_ replaced with
> _IfcLogicalOperatorEnum_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcconstraintresource/lexical/ifcobjective.htm)


Attribute definitions
---------------------
| Attribute            | Description                                                                                                                                                                                                                                                                                                    |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LogicalAggregator    | Enumeration that identifies the logical type of aggregation for the benchmark metrics.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC2X4 CHANGE  This attribute replaces replaces the former _ResultValues_ attribute and indicates the aggregation behavior formerly defined at _IfcConstraintAggregationRelationship_. |
| ObjectiveQualifier   | Enumeration that qualifies the type of objective constraint.                                                                                                                                                                                                                                                   |
| UserDefinedQualifier | A user defined value that qualifies the type of objective constraint when ObjectiveQualifier attribute of type _IfcObjectiveEnum_ has value USERDEFINED.                                                                                                                                                       |

Formal Propositions
-------------------
| Rule   | Description   |
|--------|---------------|
| WR21   |               |

Associations
------------
| Attribute       | Description   |
|-----------------|---------------|
| BenchmarkValues |               |

