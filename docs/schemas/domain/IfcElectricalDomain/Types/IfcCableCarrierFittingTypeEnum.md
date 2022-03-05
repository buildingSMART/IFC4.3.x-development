# IfcCableCarrierFittingTypeEnum

The _IfcCableCarrierFittingTypeEnum_ defines the range of different types of cable carrier fitting that can be specified.

> HISTORY  New type in IFC2x2.

## Items

### BEND
A fitting that changes the route of the cable carrier.

### CONNECTOR
Connector fitting, typically used to join two ports together within a flow distribution system (e.g., a coupling used to join two duct segments).

> IFC4.3.0.0 CHANGE New enumeration

### CROSS
A fitting at which two branches are taken from the main route of the cable carrier simultaneously.

> IFC4.3.0.0 DEPRECATION Use JUNCTION instead.

### JUNCTION
A fitting with typically more than two ports used to redistribute flow among the ports and/or to change the direction of flow between connected elements (e.g, tee, cross, wye, etc.).

> IFC4.3.0.0 CHANGE New enumeration

### TEE
A fitting at which a branch is taken from the main route of the cable carrier.

> IFC4.3.0.0 DEPRECATION Use JUNCTION instead.

### TRANSITION
A fitting with typically two ports having different shapes or sizes. Can also be used to change the direction of flow between connected elements.

> IFC4.3.0.0 CHANGE New enumeration

### USERDEFINED
User-defined type.

### NOTDEFINED
Undefined type.
