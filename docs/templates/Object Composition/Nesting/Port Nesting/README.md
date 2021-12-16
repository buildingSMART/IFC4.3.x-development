Port Nesting
============

Ports indicate possible connections to other objects according to specified system types, flow direction, and connection properties. Ports are typically connected between devices via cables, pipes, or ducts.

Ports may have placement defined indicating the position and outward orientation of the port relative to the product or product type. Ports may also have material profile sets defined indicating the flow area and connection enclosure.

```
concept {
    IfcDistributionElement:IsNestedBy -> IfcRelNests:RelatingObject
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
    IfcDistributionElement:PredefinedType[binding="PredefinedType"]
    IfcDistributionPort:Name[binding="PortName"]
    IfcDistributionPort:FlowDirection[binding="Flow"]
    IfcDistributionPort:SystemType[binding="SystemType"]
}
```
