Tendon Attributes
=================



```
concept {
    IfcTendon:Tag -> IfcIdentifier
    IfcTendon:IsTypedBy -> IfcRelDefinesByType
    IfcRelDefinesByType:RelatingType -> IfcTendonType
    IfcTendonType:NominalDiameter -> IfcPositiveLengthMeasure
    IfcTendonType:CrossSectionArea -> IfcAreaMeasure
    IfcTendonType:SheathDiameter -> IfcPositiveLengthMeasure
}
```
