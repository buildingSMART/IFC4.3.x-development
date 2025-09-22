Reinforcing Bar Type Attributes
===============================

> NOTE: This template for attributes, like similar ones, originates from legacy requirements tied to mvdXML and an earlier era when MVD defined exchange information requirements. Such templates no longer add value to the specification, nor do they convey information beyond what is already defined in the schema. Additionally, some templates reference deprecated entities, potentially causing unnecessary confusion.
As part of a broader effort to clean up documentation, this and other non-essential templates will be removed in the next release.

Reinforcing may be further described according to physical characteristics.

```
concept {
    IfcReinforcingBarType:NominalDiameter -> IfcPositiveLengthMeasure_0
    IfcReinforcingBarType:CrossSectionArea -> IfcAreaMeasure
    IfcReinforcingBarType:BarLength -> IfcPositiveLengthMeasure_1
    IfcReinforcingBarType:BarSurface -> IfcReinforcingBarSurfaceEnum
    IfcReinforcingBarType:BendingShapeCode -> IfcLabel
    IfcReinforcingBarType:BendingParameters -> IfcBendingParameterSelect
}
```
