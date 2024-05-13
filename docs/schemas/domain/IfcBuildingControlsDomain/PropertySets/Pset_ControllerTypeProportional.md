# Pset_ControllerTypeProportional

Properties for signal handling for an proportional controller taking setpoint and feedback inputs and creating a single valued output. HISTORY: In <!-- end of definition -->IFC4, SignalFactor1, SignalFactor2 and SignalFactor3 changed to ProportionalConstant, IntegralConstant and DerivativeConstant.  SignalTime1 and SignalTime2 changed to SignalTimeIncrease and SignalTimeDecrease.


## Comments

### ControlType

PROPORTIONAL: Output is proportional to the control error. The gain of a proportional control (Kp) will have the effect of reducing the rise time and reducing , but never eliminating, the steady-state error of the variable controlled.
PROPORTIONALINTEGRAL: Part of the output is proportional to the control error and part is proportional to the time integral of the control error. Adding the gain of an integral control (Ki) will have the effect of eliminating the steady-state error of the variable controlled, but it may make the transient response worse.
PROPORTIONALINTEGRALDERIVATIVE: Part of the output is proportional to the control error, part is proportional to the time integral of the control error and part is proportional to the time derivative of the control error. Adding the gain of a derivative control (Kd) will have the effect of increasing the stability of the system, reducing the overshoot, and improving the transient response of the variable controlled.

### Value

The expected range and default value.  While the property data type is IfcReal (to support all cases including when the units are unknown), a unit may optionally be provided to indicate the measure and unit.

### Labels

Labels indicate transition points such as 'Hi', 'Lo', 'HiHi', or 'LoLo'.
