# IfcReinforcementBarProperties

_IfcReinforcementBarProperties_ defines the set of properties for a specific combination of reinforcement bar steel grade, bar type and effective depth.
<!-- end of short definition -->

> HISTORY New entity in IFC2x2.

The total cross section area for the specific steel grade is always provided. Additionally also general reinforcing bar configurations as a count of bars may be provided as defined in attribute _BarCount_. In this case the nominal bar diameter should be identical for all given bars as defined in attribute _NominalBarDiameter_.

## Attributes

### TotalCrossSectionArea
The total effective cross-section area of the reinforcement of a specific steel grade.

### SteelGrade
The nominal steel grade defined according to local standards.

### BarSurface
Indicator for whether the bar surface is plain or textured.

### EffectiveDepth
The effective depth, i.e. the distance of the specific reinforcement cross section area or reinforcement configuration in a row, counted from a common specific reference point. Usually the reference point is the upper surface (for beams and slabs) or a similar projection in a plane (for columns).

### NominalBarDiameter
The nominal diameter defining the cross-section size of the reinforcing bar. The bar diameter should be identical for all bars included in the specific reinforcement configuration.

### BarCount
The number of bars with identical nominal diameter and steel grade included in the specific reinforcement configuration.
