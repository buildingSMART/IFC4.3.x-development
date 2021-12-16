Reinforcing Bar Attributes
==========================



```
concept {
    IfcReinforcingBar:Tag -> IfcIdentifier
    IfcReinforcingBar:IsTypedBy -> IfcRelDefinesByType:RelatedObjects
    IfcReinforcingBar:NominalDiameter -> IfcPositiveLengthMeasure_2
    IfcReinforcingBar:CrossSectionArea -> IfcAreaMeasure_1
    IfcReinforcingBar:BarLength -> IfcPositiveLengthMeasure_3
    IfcReinforcingBar:BarSurface -> IfcReinforcingBarSurfaceEnum_1
    IfcRelDefinesByType:RelatingType -> IfcReinforcingBarType
    IfcReinforcingBarType:NominalDiameter -> IfcPositiveLengthMeasure_0
    IfcReinforcingBarType:CrossSectionArea -> IfcAreaMeasure_0
    IfcReinforcingBarType:BarLength -> IfcPositiveLengthMeasure_1
    IfcReinforcingBarType:BarSurface -> IfcReinforcingBarSurfaceEnum_0
    IfcReinforcingBarType:BendingShapeCode -> IfcLabel
    IfcReinforcingBarType:BendingParameters -> IfcBendingParameterSelect
}
```
