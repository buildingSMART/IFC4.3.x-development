IfcPropertyBoundedValue
=======================
A property with a bounded value, _IfcPropertyBoundedValue_, defines a property
object which has a maximum of two (numeric or descriptive) values assigned,
the first value specifying the upper bound and the second value specifying the
lower bound. It defines a property - value bound (min-max) combination for
which the property _Name_, an optional _Description_,\S\ the optional
_UpperBoundValue_ with measure type, the optional _LowerBoundValue_ with
measure type, and the optional _Unit_ is given. A set point value can be
provided in addition to the upper and lower bound values for operational value
setting.  
  
The unit is handled by the _Unit_ attribute, see Table 1 for an example of a
bounded property:  
  
* If the _Unit_ attribute is not given, then the unit is already implied by the type of _IfcMeasureValue_ or _IfcDerivedMeasureValue_. The associated unit can be found at the _IfcUnitAssignment_ globally defined at the project level (_IfcProject.UnitsInContext_).   
* If the _Unit_ attribute is given, then the unit assigned by the _Unit_ attribute overrides the globally assigned unit.   
  
The _IfcPropertyBoundedValue_ allows for the specification of an interval for
the value component of the property description. If either the
_LowerBoundValue_ or the _UpperBoundValue_ is not given, then it indicates an
open bound (either a minimum value or a maximum value). The interval is by
definition inclusive, that is, the value given for the _LowerBoundValue_ or
the _UpperBoundValue_ is included in the interval.  
  
> NOTE  An _IfcPropertyBoundedValue_ may be exchanged with no values assigned
> yet. In this case the _LowerBoundValue_ and the _UpperBoundValue_ are set to
> NIL.  
  
>  
>  
>  
  
  
  
  
| Name  
| UpperBoundValue  
| LowerBoundValue  
| SetPointValue  
| Type  
(through _IfcValue_ )  
| Unit  
  
  
---|---|---|---|---|---  
  
  
OverallHeight  
| 1930  
| 2300  
| <nil>  
| _IfcPositiveLengthMeasure_  
| -  
  
  
  
OverallWidth  
| 0.9  
| 1.25  
| <nil>  
| _IfcPositiveLengthMeasure_  
| m  
  
  
  
MaxHeight  
| 20.0  
| <nil>  
| <nil>  
| _IfcPositiveLengthMeasure_  
| -  
  
  
  
MinWeight  
| <nil>  
| 20  
| <nil>  
| _IfcMassMeasure_  
| kg  
  
  
  
* Where rules ensures same measure type for all values  
  
  
  
  
  
  
  

Table 1 -- Bounded property with values, measure types and units

  
  
  
  
  
> HISTORY \S\ New entity in IFC2x.  
  
{ .change-ifc2x2}  
> IFC2x2 CHANGE  The attribute type of the attribute _UpperBoundValue_ and
> _LowerBoundValue_ has been made optional with upward compatibility for file
> based exchange.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The attribute _SetPointValue_ has been added.  
  
{ .spec-head}  
Informal Propositions:  
  
1\. If the measure type for the upper and lover bound value is a numeric
measure, then the following shall be true: _UpperBoundValue_ >
_LowerBoundValue_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpropertyresource/lexical/ifcpropertyboundedvalue.htm)


Attribute definitions
---------------------
| Attribute       | Description                                                                                                                                                                                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UpperBoundValue | Upper bound value for the interval defining the property value. If the value is not given, it indicates an open bound (all values to be greater than or equal to _LowerBoundValue_).                                                                                                                          |
| LowerBoundValue | Lower bound value for the interval defining the property value. If the value is not given, it indicates an open bound (all values to be lower than or equal to _UpperBoundValue_).                                                                                                                            |
| Unit            | Unit for the upper and lower bound values, if not given, the default value for the measure type is used as defined by the global unit assignment at _IfcProject.UnitInContext_. The applicable unit is then selected by the underlying TYPE of the _UpperBoundValue_, _LowerBoundValue_, and _SetPointValue_) |
| SetPointValue   | Set point value as typically used for operational value setting.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  The attribute has been added at the end of the attribute list.                                                                                                                                      |

