Resource Cost
=============

Resources can have associated costs indicating financial costs and environmental impacts incurred according to a specified base quantity.

Each cost value may be defined using a constant amount or calculated according to specified formula.

```
concept {
    IfcConstructionResource:BaseCosts -> IfcAppliedValue
    IfcAppliedValue:Name -> IfcLabel
    IfcConstructionResource:BaseCosts[binding="CostType"]
    IfcAppliedValue:Name[binding="CostName"]
    IfcAppliedValue:AppliedValue[binding="ValueType"]
}
```
