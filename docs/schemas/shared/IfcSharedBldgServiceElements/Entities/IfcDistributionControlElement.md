# IfcDistributionControlElement

The distribution element _IfcDistributionControlElement_ defines occurrence elements of a building automation control system that are used to impart control over elements of a distribution system.

_IfcDistributionControlElement_ defines elements of a building automation control system. These are typically used to control distribution system elements to maintain variables such as temperature, humidity, pressure, flow, power, or lighting levels, through the modulation, staging or sequencing of mechanical or electrical devices. The three general functional categories of control elements are as follows:

* Impart control over flow control elements (_IfcFlowController_) in a distribution system such as dampers, valves, or relays, typically through the use of actuation (_IfcActuator_).
* Sensing elements (_IfcSensor_) that measure changes in the controlled variable such as temperature, humidity, pressure, or flow.
* Controllers (_IfcController_) typically classified according to the control action they seek to perform and generally responsible for making decisions about the elements under control.

Since _IfcDistributionControlElement_ and its subtypes typically relate to many different distribution flow elements (_IfcDistributionFlowElement_), the objectified relationship _IfcRelFlowControlElements_ has been provided to relate control and flow elements as required.

The key distinction between _IfcDistributionFlowElement_ and _IfcDistributionControlElement_ is whether it is internal or external to the flow system, respectively. For example, the distinction between _IfcFlowMeter_ (subtype of _IfcDistributionFlowElement_ measuring a flow quantity) and _IfcFlowInstrument_ (subtype of _IfcDistributionControlElement_ measuring a flow quality), is based on this principal. A physical device that connects within the flow system in which it measures (having inlet/outlet pipes for the measured substance) follows the _IfcDistributionFlowElement_ hierarchy (and therefore _IfcFlowMeter_ which measures the flow internally). Otherwise, if it monitors/controls but does not connect inline within the flow system (it is external or is a component of another device), then it follows the _IfcDistributionControlElement_ hierarchy (and therefore _IfcFlowInstrument_ which may display various attributes through connected sensors).

> HISTORY&nbsp; New entity in IFC2.0.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Attribute _ControlElementId_ attribute deleted; replaced by classification usage. Ports are now primarily defined using _IfcRelNests_ to enable definition of ports at type definitions (both forward and backward compatible), provide a logical order, and reduce the number of relationship objects needed. The relationship _IfcRelConnectsPortToElement_ is still supported, however is now specific to dynamically connected ports.

## Attributes

### AssignedToFlowElement
Reference through the relationship object to related distribution flow elements.
