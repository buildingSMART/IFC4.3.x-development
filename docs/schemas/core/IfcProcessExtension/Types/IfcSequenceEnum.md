# IfcSequenceEnum

_IfcSequenceEnum_ is an enumeration that defines the different ways in which a time lag is applied to a sequence between two processes.
<!-- end of short definition -->

> HISTORY New entity in IFC1.0

## Items

### START_START
The predecessor task must start before the successor task may start.

### START_FINISH
The predecessor task must start before the successor task may finish.

### FINISH_START
The predecessor task must finish before the successor task may start.

### FINISH_FINISH
The predecessor task must finish before the successor task may finish.

### USERDEFINED
User defined.

### NOTDEFINED
Undefined.
