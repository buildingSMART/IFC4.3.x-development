

<!-- end of short definition -->
## Items

### CONSTANT
No inputs

### MODIFIER
Single analog input is read, added to SignalOffset, multiplied by SignalFactor, and written to the output value

### ABSOLUTE
Single analog input is read and absolute value is written to the output value

### INVERSE
Single analog input is read, 1

### HYSTERESIS
Hysteresis

### RUNNINGAVERAGE
Single analog input is read, averaged over SignalTime, and written to the output value

### DERIVATIVE
Single analog input is read and the rate of change during the SignalTime is written to the output value

### INTEGRAL
Single analog input is read and the average value during the SignalTime is written to the output value

### BINARY
Single binary input is read and SignalOffset is written to the output value if True

### ACCUMULATOR
Single binary input is read, and for each pulse the SignalOffset is added to the accumulator, and while the accumulator is greater than the SignalFactor, the accumulator is decremented by SignalFactor and the integer result is incremented by one

### PULSECONVERTER
Single integer input is read, and for each increment the SignalMultiplier is added and written to the output value

### LOWERLIMITCONTROL
Lower Limit Control

### UPPERLIMITCONTROL
Upper Limit Control

### SUM
Two analog inputs are read, added, and written to the output value

### SUBTRACT
Two analog inputs are read, subtracted, and written to the output value

### PRODUCT
Two analog inputs are read, multiplied, and written to the output value

### DIVIDE
Two analog inputs are read, divided, and written to the output value

### AVERAGE
Single analog input is read, averaged over SignalTime, and written to the output value

### MAXIMUM
Two analog inputs are read and the maximum is written to the output value

### MINIMUM
Two analog inputs are read and the minimum is written to the output value

### REPORT
Report

### SPLIT
Split

### INPUT
Controller element is a dedicated input

### OUTPUT
Controller element is a dedicated output

### VARIABLE
Controller element is an in-memory variable

### OTHER
required category not on scale

### NOTKNOWN
Value is unkown

### UNSET
Value has not been specified
