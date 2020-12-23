# IfcDistributionPort

A distribution port is an inlet or outlet of a product through which a particular substance may flow.

Distribution ports are used for passage of solid, liquid, or gas substances, as well as electricity for power or communications. Flow segments (pipes, ducts, cables) may be used to connect ports across products. Distribution ports are defined by system type and flow direction such that for two ports to be connected, they must share the same system type and have opposite flow directions (one side being a _SOURCE_ and the other being a _SINK_). Ports are similar to openings in that they do not have any visible geometry; such geometry is captured at the shape representation of the enclosing element or element type. Ports may have placement that indicates the position and orientation of the connection.

Ports are assigned the distribution systems in order to indicate its role in a particular system, e.g. cold water inlet.

> HISTORY&nbsp; New entity in IFC2x2

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Ports are now related to products and product types using the _IfcRelNests_ relationship; use of _IfcRelConnectsPortToElement_ is now reserved for dynamically attached ports (such as drilling a hole in a tank).

## Attributes

### FlowDirection
Enumeration that identifies if this port is a Sink (inlet), a Source (outlet) or both a SinkAndSource.

### PredefinedType


### SystemType
Enumeration that identifies the system type.  If a system type is defined, the port may only be connected to other ports having the same system type.
