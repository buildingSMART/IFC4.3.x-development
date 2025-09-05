Control Flow
============

Control elements (such as sensors) that monitor or control behaviour of flow elements (such as valves) use this relationship to indicate control flow logical behaviour.

```
concept {
    IfcDistributionControlElement:AssignedToFlowElement -> IfcRelFlowControlElements:RelatedControlElements
    IfcRelFlowControlElements:RelatingFlowElement -> IfcDistributionFlowElement
    IfcRelFlowControlElements:RelatingFlowElement[binding="Type"]
}
```
