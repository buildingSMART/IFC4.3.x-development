# IfcProtectiveDeviceTypeEnum

The _IfcProtectiveDeviceTypeEnum_ specifically defines the range of different breaker unit types that can be used in conjunction with protective device. Types may also be used as a reference to a complete protective device in circumstances where tripping units are not separately identified (typically expected to be the case during earlier stages of design).

> HISTORY&nbsp; New type in IFC2x2. Modified definition and usage in IFC4.

## Items

### CIRCUITBREAKER


### EARTHLEAKAGECIRCUITBREAKER
A device that opens, closes, or isolates a circuit and has short circuit protection but no overload protection.  It attempts to break the circuit when there is a leakage of current from phase to earth, by measuring voltage on the earth conductor.

### EARTHINGSWITCH


### FUSEDISCONNECTOR
A device that will electrically open the circuit after a period of prolonged, abnormal current flow.

### RESIDUALCURRENTCIRCUITBREAKER
A device that opens, closes, or isolates a circuit and has short circuit and overload protection.  It attempts to break the circuit when there is a difference in current between any two phases.  May also be referred to as 'Ground Fault Interupter (GFI)' or 'Ground Fault Circuit Interuptor (GFCI)'

### RESIDUALCURRENTSWITCH
A device that opens, closes or isolates a circuit and has no short circuit or overload protection.  May also be identified as a 'ground fault switch'.

### VARISTOR
A high voltage surge protection device.

### ANTI


### SPARKGAP


### VOLTAGELIMITER


### USERDEFINED
User-defined type.

### NOTDEFINED

