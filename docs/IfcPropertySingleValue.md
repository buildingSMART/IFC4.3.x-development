IfcPropertySingleValue
======================
The property with a single value _IfcPropertySingleValue_ defines a property
object which has a single (numeric or descriptive) value assigned. It defines
a property - single value combination for which the property _Name_, an
optional _Description_,\S\ and an optional _NominalValue_ with measure type is
provided. In addition, the default unit as specified within the project unit
context can be overriden by assigning an _Unit_.  
  
The unit is handled by the _Unit_ attribute, see Table 1 for an example of
various single value properties:  
  
* If the _Unit_ attribute is not given, then the unit is already implied by the type of _IfcMeasureValue_ or _IfcDerivedMeasureValue_. The associated unit can be found at the _IfcUnitAssignment_ globally defined at the project level (_IfcProject.UnitsInContext_).  
* If the _Unit_ attribute is given, then the unit assigned by the _Unit_ attribute overrides the globally assigned unit.  
  
  
  
  
  
  
  
  
| **Name**  
| **NominalValue**  
| **Type** (through _IfcValue_ )  
| **Unit**  
  
---|---|---|---  
  
  
Description  
| Manufacturer "A" door  
| _IfcLabel_  
| -  
  
  
  
PanelThickness  
| 0.12  
| _IfcPositiveLengthMeasure_  
| -  
  
  
  
ThermalTransmittance  
| 2.6  
| _IfcThermalTransmittanceMeasure_  
| W/(m2K)  
  
  
  
  
  
  
  

Table 1 -- Single value properties with values, measure types and units

  
  
  
  
  
> HISTORY \S\ New entity in IFC1.0.  
  
{ .change-ifc2x}  
> IFC2x CHANGE  Entity has been renamed from IfcSimpleProperty.  
  
{ .change-ifc2x3}  
> IFC2x3 CHANGE \S\ Attribute _NominalValue_ has been made OPTIONAL with
> upward compatibility for file based exchange.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpropertyresource/lexical/ifcpropertysinglevalue.htm)


