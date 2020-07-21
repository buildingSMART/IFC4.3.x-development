IfcPropertyTableValue
=====================
_IfcPropertyTableValue_ is a property with a value range defined by a property
object which has two lists of (numeric or descriptive) values assigned. The
values specify a table with two columns. The defining values provide the first
column and establish the scope for the defined values (the second column). An
optional _Expression_ attribute may give the equation used for deriving the
range value, which is for information purposes only.  
  
The _IfcPropertyTableValue_ defines a defining/defined property value
combination for which the property name, the table with defining and defined
values with measure type (and optional the units for defining and defined
values) are given.  
  
> NOTE  The _IfcPropertyTableValue_ only captures properties that can be
> expressed by a table with two columns. Use IfcPropertyReferenceValue with
> the PropertyReference being an IfcTable to express all those properties that
> require a table with tree or more columns.  
  
The units are handled by the _DefiningUnit_ and _DefinedUnit_ attributes, see
Table 1 for an example of a table value property:  
  
* If the _DefiningUnit_ or _DefinedUnit_ attribute is not given, then the unit is already implied by the type of _IfcMeasureValue_ or _IfcDerivedMeasureValue_. The associated unit can be found at the _IfcUnitAssignment_ globally defined at the project level (_IfcProject.UnitsInContext_).   
* If the _DefiningUnit_ or _DefinedUnit_ attribute is given, then the unit assigned by the unit attribute overrides the globally assigned unit.   
  
The _IfcPropertyTableValue_ allows for the specification of a table of
defining/defined value pairs of the property description. The optional
attribute _CurveInterpolation_ allows to determine the interval between two
given values.  
  
  
  
  
  
  
  
  
| Name  
| DefiningValues  
| DefiningValue Type  
(through IfcValue)  
| DefinedValues  
| DefinedValue Type  
(through IfcValue)  
| DefingUnit  
| DefinedUnit  
  
---|---|---|---|---|---|---  
  
  
SoundTransmissionLoss  
| 100  
| _IfcFrequencyMeasure_  
| 20  
| _IfcNumericMeasure_  
| -  
| dB  
  
  
  
  
  
| 200  
  
| _IfcFrequencyMeasure_  
  
| 42  
  
| _IfcNumericMeasure_  
  
|  
  
|  
  
  
  
  
  
  
| 400  
  
| _IfcFrequencyMeasure_  
  
| 46  
  
| _IfcNumericMeasure_  
  
|  
  
|  
  
  
  
  
  
  
| 800  
  
| _IfcFrequencyMeasure_  
  
| 56  
  
| _IfcNumericMeasure_  
  
|  
  
|  
  
  
  
  
  
  
| 1600  
  
| _IfcFrequencyMeasure_  
  
| 60  
  
| _IfcNumericMeasure_  
  
|  
  
|  
  
  
  
  
  
  
| 3200  
  
| _IfcFrequencyMeasure_  
  
| 65  
  
| _IfcNumericMeasure_  
  
|  
  
|  
  
  
  
  
  
  
  
  

Table 1 -- Table value property with values, measure types and units

  
  
  
  
  
> HISTORY  New entity in IFC2x.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Attributes _DefiningValues_ and _DefinedValues_ have been made
> OPTIONAL with upward compatibility for file based exchange. The attribute
> _CurveInterpolation_ has been added.  
  
  
  
{ .spec-head}  
Informal Propositions:  
  
1\. The list of _DefinedValues_ and the list of _DefiningValues_ are
corresponding lists.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpropertyresource/lexical/ifcpropertytablevalue.htm)


Attribute definitions
---------------------
| Attribute          | Description                                                                                                                                                                                                                                      |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DefiningValues     | List of defining values, which determine the defined values. This list shall have unique values only.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  The attribute has been made optional with upward compatibility for file based exchange.           |
| DefinedValues      | Defined values which are applicable for the scope as defined by the defining values.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  The attribute has been made optional with upward compatibility for file based exchange.                            |
| Expression         | Expression for the derivation of defined values from the defining values, the expression is given for information only, i.e. no automatic processing can be expected from the expression.                                                        |
| DefiningUnit       | Unit for the defining values, if not given, the default value for the measure type (given by the TYPE of the defining values) is used as defined by the global unit assignment at IfcProject.                                                    |
| DefinedUnit        | Unit for the defined values, if not given, the default value for the measure type (given by the TYPE of the defined values) is used as defined by the global unit assignment at IfcProject.                                                      |
| CurveInterpolation | Interpolation of the curve between two defining and defined values that are provided. if not provided a linear interpolation is assumed.\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  The attribute has been added at the end of the attribute list. |

Formal Propositions
-------------------
| Rule   | Description   |
|--------|---------------|
| WR21   |               |
| WR22   |               |
| WR23   |               |

