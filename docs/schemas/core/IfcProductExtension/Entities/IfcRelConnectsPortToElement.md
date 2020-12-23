# IfcRelConnectsPortToElement

_IfcRelConnectsPortToElement_ is a relationship between a distribution element and dynamically connected ports where connections are realised to other distribution elements.

Ports contained in different elements are connected to each other using the _IfcRelConnectsPorts_ relationship.

> NOTE&nbsp; See _IfcRelNests_ for its usages to represent an ordered collection of ports that are contained by an element and relevant subtypes of _IfcDistributionElement_ for examples and port use definition sections.

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; The objectified relation _IfcRelConnectsPortToElement_ is now specialized for use of dynamically connected ports. For fixed ports, use _IfcRelNests_ instead. Previously this objectified relationship _IfcRelConnectsPortToElement_ defined the relationship that is made between a port and the _IfcElement_ in which it is contained. It is a 1 to 1 relationship. The _IfcRelConnectsPortToElement_ established a whole part relationship between the element and its port. The port is used as the means to connect to other ports in other elements.

## Attributes

### RelatingPort
Reference to an Port that is connected by the objectified relationship.

### RelatedElement
Reference to an _IfcDistributionElement_ that has ports assigned.
{ .change-ifc2x4}
> IFC4 CHANGE Data type restricted to _IfcDistributionElement_.
