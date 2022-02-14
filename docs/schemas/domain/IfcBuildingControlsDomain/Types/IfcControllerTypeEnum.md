# IfcControllerTypeEnum

The _IfcControllerTypeEnum_ defines the range of different types of controller that can be specified.

> HISTORY&nbsp; New enumeration in IFC2.0.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; PROPORTIONALINTEGRAL and PROPORTIONALINTEGRALDERIVATIVE values deleted (property set enumeration now used). MULTIPOSITION added.

## Items

### FLOATING
Output increases or decreases at a constant or accelerating rate.

### PROGRAMMABLE
Output is programmable such as Discrete Digital Control (DDC).

### PROPORTIONAL
Output is proportional to the control error and optionally time integral and derivative.

### MULTIPOSITION
Output is discrete value, can be one of three or more values.

### TWOPOSITION
Output can be either on or off.

### USERDEFINED
User-defined type.

### NOTDEFINED
Undefined type.
