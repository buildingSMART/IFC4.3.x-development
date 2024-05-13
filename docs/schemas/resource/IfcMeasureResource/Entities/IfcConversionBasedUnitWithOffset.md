# IfcConversionBasedUnitWithOffset

_IfcConversionBasedUnitWithOffset_ is a unit which is converted from another unit by applying a conversion factor and an offset.

> HISTORY  New entity in IFC4.

Example: The temperature unit Fahrenheit is based on the temperature unit Kelvin as follows:

$$ f = 1.8k - 459.67 $$

wherein _k_ is an absolute temperature expressed in Kelvin and _f_ is the same temperature in Fahrenheit. The following entity instances provide Fahrenheit as a unit:

```
IfcConversionBasedUnitWithOffset(
     IfcDimensionalExponents(0, 0, 0, 0, 1, 0, 0),
     THERMODYNAMICTEMPERATUREUNIT,
     'Fahrenheit',
     IfcMeasureWithUnit(
         IfcThermodynamicTemperatureMeasure(1/1.8),
         IfcSIUnit(THERMODYNAMICTEMPERATUREUNIT, ?, KELVIN)),
     -459.67);
```

## Attributes

### ConversionOffset
A positive or negative offset to add after the inherited _ConversionFactor_ was applied.
