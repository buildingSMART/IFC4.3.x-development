IfcAppliedValue
===============
This entity captures a value driven by a formula, with additional
qualifications including unit basis, valid date range, and categorization.  
  
The extent of the _IfcAppliedValue_ is determined by the _AppliedValue_
attribute which may be defined either as an _IfcMeasureWithUnit_ or as an
_IfcMonetaryMeasure_ or as an _IfcRatioMeasure_ via the
_IfcAppliedValueSelect_ type.  
  
Optionally, an _IfcAppliedValue_ may have an applicable date. This is intended
to fix the date on which the value became relevant for use. It may be the date
on which the value was set in the model or it may be a prior or future date
when the value becomes operable. Similarly, an _IfcAppliedValue_ may have a
''fixed until'' date. This is intended to fix the date on which the value
ceases to be relevant for use.  
  
An instance of _IfcAppliedValue_ may have a unit basis asserted. This is
defined as an _IfcMeasureWithUnit_ that determines the extent of the unit
value for application purposes. It is assumed that when this attribute is
asserted, then the value given to _IfcAppliedValue_ is that for unit quantity.
This is not enforced within the schema and thus needs to be controlled within
an application.  
  
Applied values may be referenced from a document (such as a price list). The
relationship between one or more occurrences of _IfcAppliedValue_ (or its
subtypes) is achieved through the use of the
_IfcExternalReferenceRelationship_ in which the document provides the
_IfcExternalReferenceRelationship.RelatingExtReference_ and the value
occurrences are the _IfcExternalReferenceRelationship.RelatedResourceObjects_.  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Entity made non-abstract to support general formula expressions
> of constraints, data type of date-based attributes changed into _IfcDate_,
> _ValueType_ and _Condition_ promoted from _IfcCostValue_, _Components_ and
> _ArithmeticOperator_ attributes added to replace
> _IfcAppliedValueRelationship_ for more efficient encoding and reference
> tracking.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifccostresource/lexical/ifcappliedvalue.htm)


