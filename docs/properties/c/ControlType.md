ControlType
===========

The type of signal modification effected and applicable ports: 

CONSTANT: No inputs; SignalOffset is written to the output value.
MODIFIER: Single analog input is read, added to SignalOffset, multiplied by SignalFactor, and written to the output value.
ABSOLUTE: Single analog input is read and absolute value is written to the output value.
INVERSE: Single analog input is read, 1.0 is divided by the input value and written to the output value.
HYSTERISIS: Single analog input is read, delayed according to SignalTime, and written to the output value.
RUNNINGAVERAGE: Single analog input is read, averaged over SignalTime, and written to the output value.
DERIVATIVE: Single analog input is read and the rate of change during the SignalTime is written to the output value.
INTEGRAL: Single analog input is read and the average value during the SignalTime is written to the output value.
BINARY: Single binary input is read and SignalOffset is written to the output value if True.
ACCUMULATOR: Single binary input is read, and for each pulse the SignalOffset is added to the accumulator, and while the accumulator is greater than the SignalFactor, the accumulator is decremented by SignalFactor and the integer result is incremented by one.
PULSECONVERTER: Single integer input is read, and for each increment the SignalMultiplier is added and written to the output value.
SUM: Two analog inputs are read, added, and written to the output value.
SUBTRACT: Two analog inputs are read, subtracted, and written to the output value.
PRODUCT: Two analog inputs are read, multiplied, and written to the output value.
DIVIDE: Two analog inputs are read, divided, and written to the output value.
AVERAGE: Two analog inputs are read and the average is written to the output value.
MAXIMUM: Two analog inputs are read and the maximum is written to the output value.
MINIMUM: Two analog inputs are read and the minimum is written to the output value..
INPUT: Controller element is a dedicated input.
OUTPUT: Controller element is a dedicated output.
VARIABLE: Controller element is an in-memory variable.
