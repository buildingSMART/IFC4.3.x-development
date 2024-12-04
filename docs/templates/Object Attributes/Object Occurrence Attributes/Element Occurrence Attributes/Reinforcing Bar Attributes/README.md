Reinforcing Bar Attributes
==========================

> NOTE: This template for attributes, like similar ones, originates from legacy requirements tied to mvdXML and an earlier era when MVD defined exchange information requirements. Such templates no longer add value to the specification, nor do they convey information beyond what is already defined in the schema. Additionally, some templates reference deprecated entities, potentially causing unnecessary confusion.
As part of a broader effort to clean up documentation, this and other non-essential templates will be removed in the next release.

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
