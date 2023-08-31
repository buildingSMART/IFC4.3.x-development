Constraint Association
======================

The concept _Constraint Association_ describes how object or object types may have associated constraints indicating a qualitative objective or a quantitative metric to be met.

Constraints based on metrics are measurable, such that the status of a metric being valid is computer-interpretable. Metric constraints are based on simple conditional logic such as greater than a particular value or included within a specified list or table. Constraints may combine multiple metrics using Boolean logic such as AND, OR, XOR, or NOT.

```
concept {
    IfcObjectDefinition:HasAssociations -> IfcRelAssociatesConstraint:RelatedObjects
    IfcRelAssociatesConstraint:RelatingConstraint -> IfcObjective
    IfcObjective:BenchmarkValues -> IfcMetric
    IfcObjective:ObjectiveQualifier -> IfcObjectiveEnum
    IfcObjective:LogicalAggregator -> IfcLogicalOperatorEnum
    IfcMetric:DataValue -> IfcMetricValueSelect
    IfcMetric:DataValue -> IfcAppliedValue_0
    IfcMetric:DataValue -> IfcTable
    IfcMetric:Benchmark -> IfcBenchmarkEnum
    IfcMetric:ReferencePath -> IfcReference_1
    IfcMetric:Name -> IfcLabel_1
    IfcMetric:Description -> IfcText_1
    IfcAppliedValue_0:ArithmeticOperator -> IfcArithmeticOperatorEnum
    IfcAppliedValue_0:Components -> IfcAppliedValue_1
    IfcAppliedValue_0:AppliedValue -> IfcLengthMeasure
    IfcAppliedValue_0:AppliedValue -> IfcReal
    IfcTable:Rows -> IfcTableRow
    IfcTable:Columns -> IfcTableColumn
    IfcTableColumn:Identifier -> IfcIdentifier
    IfcTableColumn:Name -> IfcLabel_0
    IfcTableColumn:Description -> IfcText_0
    IfcTableColumn:ReferencePath -> IfcReference_0
    IfcMetric:DataValue[binding="DataValue"]
    IfcReference_1:AttributeIdentifier[binding="Attribute1"]
}
```
