Reinforcing Mesh Attributes
===========================



```
concept {
    IfcReinforcingMesh:Tag -> IfcIdentifier
    IfcReinforcingMesh:IsTypedBy -> IfcRelDefinesByType
    IfcRelDefinesByType:RelatingType -> IfcReinforcingMeshType
    IfcReinforcingMeshType:MeshLength -> IfcPositiveLengthMeasure
    IfcReinforcingMeshType:MeshWidth -> IfcPositiveLengthMeasure
    IfcReinforcingMeshType:LongitudinalBarNominalDiameter -> IfcPositiveLengthMeasure
    IfcReinforcingMeshType:TransverseBarNominalDiameter -> IfcPositiveLengthMeasure
    IfcReinforcingMeshType:LongitudinalBarCrossSectionArea -> IfcAreaMeasure
    IfcReinforcingMeshType:TransverseBarCrossSectionArea -> IfcAreaMeasure
    IfcReinforcingMeshType:LongitudinalBarSpacing -> IfcPositiveLengthMeasure
    IfcReinforcingMeshType:TransverseBarSpacing -> IfcPositiveLengthMeasure
    IfcReinforcingMeshType:BendingShapeCode -> IfcLabel
    IfcReinforcingMeshType:BendingParameters -> IfcLengthMeasure
    IfcReinforcingMeshType:BendingParameters -> IfcPlaneAngleMeasure
}
```
