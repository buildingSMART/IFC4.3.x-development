# IfcPort

A port provides the means for an element to connect to other elements.

An _IfcPort_ is associated with an _IfcElement_, it belongs to through the objectified relationship _IfcRelNests_ if such port is fixed, or _IfcRelConnectsPortToElement_ if such port is dynamically attached. Exactly two ports, belonging to two different elements, are connected with each other through the objectified relationship _IfcRelConnectsPorts_.

An instance of _IfcElement_ may have one or more points at which it connects to other instances of _IfcElement_. An instance of em>IfcPort is located at a point where a connection can occur. The location of the port is determined in the context of the local coordinate system of the element to which it belongs. As a subordinate part being fully dependent on the master element the _IfcPort_ shall have no independent containment relationship to the spatial structure.

The local placement for _IfcPort_ is defined in its supertype _IfcProduct_. It is defined by the _IfcLocalPlacement_, which defines the local coordinate system that is referenced by all geometric representations. The _PlacementRelTo_ relationship of _IfcLocalPlacement_ shall point to the local placement of the master _IfcElement_ or _IfcElementType_ (relevant subtypes), which is related to the _IfcPort_ by the relationship object _IfcRelNests_ for fixed ports, or _IfcRelConnectsPortToElement_ for dynamic ports.

> HISTORY  New entity in IFC2x2.

## Attributes

### ContainedIn
Reference to the element to port connection relationship. The relationship then refers to the element in which this port is contained.

> IFC4 CHANGE  The cardinality has been changed from 1:1 to 0:1.

> IFC4 DEPRECATION  The inverse relationship is deprecated for fixed ports due to deprecation of _IfcRelConnectsPortToElement_ for this usage. Use inverse relationship _Nests_ instead.

### ConnectedFrom
Reference to a port that is connected by the objectified relationship.

### ConnectedTo
Reference to the port connection relationship. The relationship then refers to the other port to which this port is connected.
