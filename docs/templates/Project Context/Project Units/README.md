Project Units
=============

The project context includes the definition of the default units within the IFC data set. They are declared once for the context of the whole data set. Default units are those units that apply:

* to all geometric representation items within the geometric representation contexts; 
* to all attributes with a defined datatype indicating a measure datatype; 
* to all properties and quantities with a defined datatype indicating a measure datatype and with no local unit definitions provided. 

Default units are defined as either:

* SI Units with SI unit name and prefix
* Conversion based units with a conversion factor to its SI unit
* Derived units, consisting of one-to-many unit elements, being SI units or conversion based units
* Monetary unit as a special case of a unit to hold the currency name

> EXAMPLE  Meter is an SI unit without prefix, milli meter is an SI unit with prefix, inch and foot are conversion based units to be declared with a converstion factor to the SI unit (here meter), heat flux density (W/m2) is a derived unit with the unit elements Power (W) and Area (m2), and Euro is a monetary unit.

```
concept {
    IfcContext:UnitsInContext -> IfcUnitAssignment
    IfcContext:Phase -> IfcLabel_4
    IfcContext:ObjectType -> IfcLabel_5
    IfcContext:LongName -> IfcLabel_6
    IfcUnitAssignment:Units -> IfcDerivedUnit
    IfcUnitAssignment:Units -> IfcMonetaryUnit
    IfcUnitAssignment:Units -> IfcSIUnit
    IfcUnitAssignment:Units -> IfcConversionBasedUnit
    IfcUnitAssignment:Units -> IfcConversionBasedUnitWithOffset
    IfcDerivedUnit:UnitType -> IfcDerivedUnitEnum
    IfcDerivedUnit:Elements -> IfcDerivedUnitElement
    IfcDerivedUnit:UserDefinedType -> IfcLabel_0
    IfcDerivedUnitElement:Unit -> IfcNamedUnit
    IfcMonetaryUnit:Currency -> IfcLabel_1
    IfcSIUnit:UnitType -> IfcUnitEnum_0
    IfcSIUnit:Prefix -> IfcSIPrefix
    IfcSIUnit:Name -> IfcSIUnitName
    IfcConversionBasedUnit:Dimensions -> IfcDimensionalExponents_0
    IfcConversionBasedUnit:UnitType -> IfcUnitEnum_1
    IfcConversionBasedUnit:Name -> IfcLabel_2
    IfcConversionBasedUnit:ConversionFactor -> IfcMeasureWithUnit_0
    IfcConversionBasedUnitWithOffset:Dimensions -> IfcDimensionalExponents_1
    IfcConversionBasedUnitWithOffset:UnitType -> IfcUnitEnum_2
    IfcConversionBasedUnitWithOffset:Name -> IfcLabel_3
    IfcConversionBasedUnitWithOffset:ConversionFactor -> IfcMeasureWithUnit_1
    IfcConversionBasedUnitWithOffset:ConversionOffset -> IfcReal
    IfcContext:UnitsInContext[binding="HasUnits"]
    IfcDerivedUnit:UnitType[binding="DerivedUnitType"]
    IfcSIUnit:UnitType[binding="SIUnitType"]
    IfcSIUnit:Name[binding="SIUnitName"]
    IfcConversionBasedUnit:UnitType[binding="ConversionUnitType"]
    IfcConversionBasedUnit:Name[binding="ConversionUnitName"]
}
```
