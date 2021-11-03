Constraint Association
======================

The concept _Constraint Association_ describes how object or object types may have associated constraints indicating a qualitative objective or a quantitative metric to be met.

Constraints based on metrics are measurable, such that the status of a metric being valid is computer-interpretable. Metric constraints are based on simple conditional logic such as greater than a particular value or included within a specified list or table. Constraints may be combine multiple metrics using boolean logic such as AND, OR, XOR, or NOT.

```
concept {
    IfcObjectDefinition:HasAssociations -> IfcRelAssociatesConstraint:RelatedObjects
    IfcRelAssociatesConstraint:RelatingConstraint -> IfcObjective
    IfcObjective:BenchmarkValues -> IfcMetric
    IfcObjective:ObjectiveQualifier -> IfcObjectiveEnum
    IfcObjective:LogicalAggregator -> IfcLogicalOperatorEnum
    IfcMetric:DataValue -> IfcMetricValueSelect
    IfcMetric:DataValue -> IfcAppliedValue
    IfcMetric:DataValue -> IfcTable
    IfcMetric:Benchmark -> IfcBenchmarkEnum
    IfcMetric:ReferencePath -> IfcReference
    IfcMetric:Name -> IfcLabel
    IfcMetric:Description -> IfcText
    IfcAppliedValue:ArithmeticOperator -> IfcArithmeticOperatorEnum
    IfcAppliedValue:Components -> IfcAppliedValue
    IfcAppliedValue:AppliedValue -> IfcLengthMeasure
    IfcAppliedValue:AppliedValue -> IfcReal
    IfcTable:Rows -> IfcTableRow
    IfcTable:Columns -> IfcTableColumn
    IfcTableColumn:Identifier -> IfcIdentifier
    IfcTableColumn:Name -> IfcLabel
    IfcTableColumn:Description -> IfcText
    IfcTableColumn:ReferencePath -> IfcReference
    IfcMetric:DataValue[binding="DataValue"]
    IfcReference:AttributeIdentifier[binding="Attribute1"]
}
```
