Reinforcing Mesh Attributes
===========================

> NOTE: This template for attributes, like similar ones, originates from legacy requirements tied to mvdXML and an earlier era when MVD defined exchange information requirements. Such templates no longer add value to the specification, nor do they convey information beyond what is already defined in the schema. Additionally, some templates reference deprecated entities, potentially causing unnecessary confusion.
As part of a broader effort to clean up documentation, this and other non-essential templates will be removed in the next release.

```
concept {
    IfcReinforcingMesh:Tag -> IfcIdentifier
    IfcReinforcingMesh:IsTypedBy -> IfcRelDefinesByType:RelatedObjects
    IfcRelDefinesByType:RelatingType -> IfcReinforcingMeshType
    IfcReinforcingMeshType:MeshLength -> IfcPositiveLengthMeasure_0
    IfcReinforcingMeshType:MeshWidth -> IfcPositiveLengthMeasure_1
    IfcReinforcingMeshType:LongitudinalBarNominalDiameter -> IfcPositiveLengthMeasure_2
    IfcReinforcingMeshType:TransverseBarNominalDiameter -> IfcPositiveLengthMeasure_3
    IfcReinforcingMeshType:LongitudinalBarCrossSectionArea -> IfcAreaMeasure_0
    IfcReinforcingMeshType:TransverseBarCrossSectionArea -> IfcAreaMeasure_1
    IfcReinforcingMeshType:LongitudinalBarSpacing -> IfcPositiveLengthMeasure_4
    IfcReinforcingMeshType:TransverseBarSpacing -> IfcPositiveLengthMeasure_5
    IfcReinforcingMeshType:BendingShapeCode -> IfcLabel
    IfcReinforcingMeshType:BendingParameters -> IfcLengthMeasure
    IfcReinforcingMeshType:BendingParameters -> IfcPlaneAngleMeasure
}
```
