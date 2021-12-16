Type Port Nesting
=================

Ports may be specified on types, following the same rules as defined for corresponding occurrences.

On type objects, ports are not connected, but serve as placeholders indicating that occurrences of the enclosing type object shall use a duplicate list of ports for connecting to ports on other object occurrences.

```
concept {
    IfcDistributionElementType:IsNestedBy -> IfcRelNests:RelatingObject
    IfcRelNests:RelatedObjects -> IfcDistributionPort
    IfcDistributionPort:Name -> IfcLabel
    IfcDistributionPort:FlowDirection -> IfcFlowDirectionEnum
    IfcDistributionPort:SystemType -> IfcDistributionSystemEnum
    IfcDistributionPort:ObjectPlacement -> IfcLocalPlacement
    IfcDistributionPort:PredefinedType -> IfcDistributionPortTypeEnum
    IfcLocalPlacement:RelativePlacement -> IfcAxis2Placement3D
    IfcAxis2Placement3D:Location -> IfcCartesianPoint
    IfcAxis2Placement3D:Axis -> IfcDirection_0
    IfcAxis2Placement3D:RefDirection -> IfcDirection_1
}
```
