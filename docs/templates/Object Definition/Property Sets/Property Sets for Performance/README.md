Property Sets for Performance
=============================

For performance history, properties are in the form of time series, for tracking data at points in time.

```
concept {
    IfcPerformanceHistory:IsDefinedBy -> IfcRelDefinesByProperties
    IfcRelDefinesByProperties:RelatingPropertyDefinition -> IfcPropertySet
    IfcPropertySet:HasProperties -> IfcPropertyReferenceValue
    IfcPropertyReferenceValue:PropertyReference -> IfcIrregularTimeSeries
    IfcIrregularTimeSeries:Values -> IfcIrregularTimeSeriesValue
    IfcIrregularTimeSeriesValue:TimeStamp -> IfcDateTime
    IfcIrregularTimeSeriesValue:ListValues -> IfcValue
}
```
