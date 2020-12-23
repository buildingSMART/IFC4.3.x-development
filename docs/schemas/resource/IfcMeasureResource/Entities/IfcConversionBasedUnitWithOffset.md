# IfcConversionBasedUnitWithOffset

_IfcConversionBasedUnitWithOffset_ is a unit which is converted from another unit by applying a conversion factor and an offset.

> HISTORY&nbsp; New entity in IFC4.

Example: The temperature unit Fahrenheit is based on the temperature unit Kelvin as follows:

> _f_&nbsp;=&nbsp;_k_&nbsp;&middot;&nbsp;1.8&nbsp;&ndash;&nbsp;459.67

wherein _k_ is an absolute temperature expressed in Kelvin and _f_ is the same temperature in Fahrenheit. The following entity instances provide Fahrenheit as a unit:

> 
> ```
> 
IfcConversionBasedUnitWithOffset(  
> &nbsp;&nbsp;&nbsp;&nbsp;IfcDimensionalExponents(0, 0, 0, 0, 1, 0, 0),  
> &nbsp;&nbsp;&nbsp;&nbsp;THERMODYNAMICTEMPERATUREUNIT,  
> &nbsp;&nbsp;&nbsp;&nbsp;'Fahrenheit',  
> &nbsp;&nbsp;&nbsp;&nbsp;IfcMeasureWithUnit(  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IfcThermodynamicTemperatureMeasure(1.8),  
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IfcSiUnit(THERMODYNAMICTEMPERATUREUNIT, ?, KELVIN)),  
> &nbsp;&nbsp;&nbsp;&nbsp;-459.67);

> ```

## Attributes

### ConversionOffset
A positive or negative offset to add after the inherited _ConversionFactor_ was applied.
