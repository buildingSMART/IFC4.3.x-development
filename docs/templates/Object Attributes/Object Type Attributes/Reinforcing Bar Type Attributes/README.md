Reinforcing Bar Type Attributes
===============================

Reinforcing may be further described according to physical characteristics.

```
concept {
    IfcReinforcingBarType:NominalDiameter -> IfcPositiveLengthMeasure
    IfcReinforcingBarType:CrossSectionArea -> IfcAreaMeasure
    IfcReinforcingBarType:BarLength -> IfcPositiveLengthMeasure
    IfcReinforcingBarType:BarSurface -> IfcReinforcingBarSurfaceEnum
    IfcReinforcingBarType:BendingShapeCode -> IfcLabel
    IfcReinforcingBarType:BendingParameters -> IfcBendingParameterSelect
}
```
