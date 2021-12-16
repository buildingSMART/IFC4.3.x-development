Port Connectivity
=================

Ports on distribution elements, such as ducts and airoutlets, or pipes and sanitary elements are connected with each other using the _Port Connectivity_. The port connection determines the direction of flow between the connected ports belonging to the distribution elements.

```
concept {
    IfcDistributionPort_0:ConnectedTo -> IfcRelConnectsPorts_0:RelatingPort
    IfcDistributionPort_0:ConnectedFrom -> IfcRelConnectsPorts_1:RelatedPort
    IfcRelConnectsPorts_0:RelatedPort -> IfcDistributionPort_1
    IfcRelConnectsPorts_0:RealizingElement -> IfcFlowSegment
    IfcRelConnectsPorts_1:RelatingPort -> IfcDistributionPort_3
    IfcDistributionPort_0:ConnectedTo[binding="ConnectedToPort"]
    IfcDistributionPort_0:ConnectedFrom[binding="ConnectedFromPort"]
}
```
