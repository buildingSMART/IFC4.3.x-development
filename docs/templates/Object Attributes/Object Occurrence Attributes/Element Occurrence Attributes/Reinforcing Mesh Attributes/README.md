Reinforcing Mesh Attributes
===========================



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
