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


Attribute definitions
---------------------
| Attribute            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UnitBasis            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Components           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| HasExternalReference |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Name                 | A name or additional clarification given to a cost value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Description          | The description that may apply additional information about a cost value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| AppliedValue         | The extent or quantity or amount of an applied value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ApplicableDate       | The date on or from which an applied value is applicable.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE Type changed from IfcDateTimeSelect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| FixedUntilDate       | The date until which applied value is applicable.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE Type changed from IfcDateTimeSelect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Category             | Specification of the type of cost used.\X\0D\X\0D> NOTE  There are many possible types of cost value that may be identified. Whilst there is a broad understanding of the meaning of names that may be assigned to different types of costs, there is no general standard for naming cost types nor are there any broadly defined classifications. To allow for any type of cost value, the _IfcLabel_ datatype is assigned.\X\0D\X\0D\X\0D \X\0DIn the absence of any well defined standard, it is recommended that local agreements should be made to define allowable and understandable cost value types within a project or region. |
| Condition            | The condition under which a cost value applies. \X\0D\X\0DFor example, within the context of a bid submission, this may refer to an option that may or may not be elected.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ArithmeticOperator   | The arithmetic operator applied to component values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

