# IfcDerivedUnit

{ .extDef}
> NOTE&nbsp; Definition according to ISO/CD 10303-41:1992  
> A derived unit is an expression of units.

> EXAMPLE&nbsp; Newton per square millimetre is a derived unit.

> NOTE&nbsp; Corresponding ISO 10303 name: derived_unit, please refer to ISO/IS 10303-41 for the final definition of the formal standard.

> HISTORY&nbsp; New entity in IFC1.5.1.

## Attributes

### Elements
The group of units and their exponents that define the derived unit.

### UnitType
Name of the derived unit chosen from an enumeration of derived unit types for use in IFC models.

### UserDefinedType


### Dimensions
Dimensional exponents derived using the function IfcDerivedDimensionalExponents using (SELF) as the input value.

## Formal Propositions

### WR1
Units as such shall not be re-defined as derived units.

### WR2
When attribute UnitType has enumeration value USERDEFINED
then attribute UserDefinedType shall also have a value.
