Control Flow
============

Control elements (such as sensors) that monitor or control behavior of flow elements (such as valves) use this relationship to indicate control flow logical behavior.

```
concept {
    IfcDistributionControlElement:AssignedToFlowElement -> IfcRelFlowControlElements:RelatedControlElements
    IfcRelFlowControlElements:RelatingFlowElement -> IfcDistributionFlowElement
}
```
