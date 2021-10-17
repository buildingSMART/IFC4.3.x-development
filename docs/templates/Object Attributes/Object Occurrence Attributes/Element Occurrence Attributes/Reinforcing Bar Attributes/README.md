Reinforcing Bar Attributes
==========================



```
concept {
    IfcReinforcingBar:Tag -> IfcIdentifier
    IfcReinforcingBar:IsTypedBy -> IfcRelDefinesByType
    IfcReinforcingBar:NominalDiameter -> IfcPositiveLengthMeasure
    IfcReinforcingBar:CrossSectionArea -> IfcAreaMeasure
    IfcReinforcingBar:BarLength -> IfcPositiveLengthMeasure
    IfcReinforcingBar:BarSurface -> IfcReinforcingBarSurfaceEnum
    IfcRelDefinesByType:RelatingType -> IfcReinforcingBarType
    IfcReinforcingBarType:NominalDiameter -> IfcPositiveLengthMeasure
    IfcReinforcingBarType:CrossSectionArea -> IfcAreaMeasure
    IfcReinforcingBarType:BarLength -> IfcPositiveLengthMeasure
    IfcReinforcingBarType:BarSurface -> IfcReinforcingBarSurfaceEnum
    IfcReinforcingBarType:BendingShapeCode -> IfcLabel
    IfcReinforcingBarType:BendingParameters -> IfcBendingParameterSelect
}
```
