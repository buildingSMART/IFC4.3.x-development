IfcConversionBasedUnitWithOffset
================================
_IfcConversionBasedUnitWithOffset_ is a unit which is converted from another
unit by applying a conversion factor and an offset.  
  
> HISTORY  New entity in IFC4.  
  
Example: The temperature unit Fahrenheit is based on the temperature unit
Kelvin as follows:  
  
> _f_ = _k_ * 1.8 - 459.67  
  
wherein _k_ is an absolute temperature expressed in Kelvin and _f_ is the same
temperature in Fahrenheit. The following entity instances provide Fahrenheit
as a unit:  
  
>  
> ```  
>  
IfcConversionBasedUnitWithOffset(  
>     IfcDimensionalExponents(0, 0, 0, 0, 1, 0, 0),  
>     THERMODYNAMICTEMPERATUREUNIT,  
>     ''Fahrenheit'',  
>     IfcMeasureWithUnit(  
>         IfcThermodynamicTemperatureMeasure(1.8),  
>         IfcSiUnit(THERMODYNAMICTEMPERATUREUNIT, ?, KELVIN)),  
>     -459.67);  
  
> ```  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcmeasureresource/lexical/ifcconversionbasedunitwithoffset.htm)


Attribute definitions
---------------------
| Attribute        | Description                                                                              |
|------------------|------------------------------------------------------------------------------------------|
| ConversionOffset | A positive or negative offset to add after the inherited _ConversionFactor_ was applied. |

