# IfcBuildingElementProxyTypeEnum

This enumeration defines the available generic types for _IfcBuildingElementProxy_ or _IfcBuildingElementProxyType_.<!-- end of definition -->

> HISTORY  New enumeration IFC2x3

> IFC4.3.0.0 CHANGE  Enumerators PROVISIONFORVOID and PROVISIONFORSPACE deprecated. Use an _IfcVirtualElement_ with PROVISIONFORVOID and CLEARANCE at _IfcVirtualElementTypeEnum_ instead.

> IFC4 CHANGE  Enumerators PROVISIONFORVOID and PROVISIONFORSPACE added.

> DEPRECATION  The enumerator COMPLEX, ELEMENT, PARTIAL shall no longer be used.

## Items

### COMPLEX
Not used - kept for upward compatibility.

### ELEMENT
Not used - kept for upward compatibility.

### PARTIAL
Not used - kept for upward compatibility.

### PROVISIONFORVOID
The proxy denotes a provision for voids (a proposed opening not applied as void yet).

> IFC4.3.0.0 DEPRECATION Use IfcVirtualElement with PROVISIONFORVOID instead.

### PROVISIONFORSPACE
The proxy denotes a provision for space (e.g. the space allocated as a provision for mechanical equipment or furniture).

> IFC4.3.0.0 DEPRECATION Use IfcVirtualElement with CLEARANCE instead.

### USERDEFINED
User-defined building element proxy.

### NOTDEFINED
Undefined building element proxy.
