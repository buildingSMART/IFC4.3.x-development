IfcPropertyListValue
====================
An _IfcPropertyListValue_ defines a property that has several (numeric or
descriptive) values assigned, these values are given by an ordered list.\S\ It
defines a property - list value combination for which the property _Name_, an
optional _Description_,\S\ the optional _ListValues_ with measure type and
optionally an _Unit_ is given. An _IfcPropertyListValue_ is a list of values.
The order in which values appear is significant. All list members shall be of
the same type.  
  
The unit is handled by the _Unit_ attribute, see Table 1 for an example of a
list property:  
  
* If the _Unit_ attribute is not given, then the unit is already implied by the type of _IfcMeasureValue_ or _IfcDerivedMeasureValue_. The associated unit can be found at the _IfcUnitAssignment_ globally defined at the project level (_IfcProject.UnitsInContext_).   
* If the _Unit_ attribute is given, then the unit assigned by the _Unit_ attribute overrides the globally assigned unit.   
  
> NOTE  An _IfcPropertyListValue_ may be exchanged with no values assigned
> yet. In this case the _ListValues_ are set to NIL.  
  
  
  
>  
  
  
  
  
| Name  
---  
  
ListValues  
| Type  
(through _IfcValue_ )  
| Unit  
  
  
  
ApplicableSizes  
| 1200  
| _IfcPositiveLengthMeasure_  
| -  
  
  
  
-  
| 1600  
| _IfcPositiveLengthMeasure_  
| -  
  
  
  
-  
| 2400  
| _IfcPositiveLengthMeasure_  
| -  
  
  
  
  
  

Table 1 -- List property with values, measure types and units

  
  
  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Attribute _ListValues_ has been made OPTIONAL with upward
> compatibility for file based exchange.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpropertyresource/lexical/ifcpropertylistvalue.htm)


