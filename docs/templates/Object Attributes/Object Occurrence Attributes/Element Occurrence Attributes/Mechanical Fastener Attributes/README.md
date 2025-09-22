Mechanical Fastener Attributes
==============================

> NOTE: This template for attributes, like similar ones, originates from legacy requirements tied to mvdXML and an earlier era when MVD defined exchange information requirements. Such templates no longer add value to the specification, nor do they convey information beyond what is already defined in the schema. Additionally, some templates reference deprecated entities, potentially causing unnecessary confusion.
As part of a broader effort to clean up documentation, this and other non-essential templates will be removed in the next release.

```
concept {
    IfcMechanicalFastener:Tag -> IfcIdentifier
    IfcMechanicalFastener:NominalDiameter -> IfcPositiveLengthMeasure_0
    IfcMechanicalFastener:NominalDiameter -> IfcPositiveLengthMeasure_4
    IfcMechanicalFastener:NominalLength -> IfcPositiveLengthMeasure_1
    IfcMechanicalFastener:NominalLength -> IfcPositiveLengthMeasure_5
    IfcMechanicalFastener:IsTypedBy -> IfcRelDefinesByType:RelatedObjects
    IfcRelDefinesByType:RelatingType -> IfcMechanicalFastenerType
    IfcMechanicalFastenerType:NominalDiameter -> IfcPositiveLengthMeasure_2
    IfcMechanicalFastenerType:NominalLength -> IfcPositiveLengthMeasure_3
}
```
