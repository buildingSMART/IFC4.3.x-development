_IfcAppliedValueSelect_ defines a value to be calculated within a formula.

<!-- end of short definition -->


Types are used as follows:

* _IfcValue_: A constant value using project default units.
* _IfcMeasureWithUnit_: A constant value using specified units.
* _IfcReference_: A value referenced on an object attribute.

For cost values, the following guidance applies:

* _IfcMeasureWithUnit_ allows the specification of both the actual figure for the value together with the currency in which the value is represented.
* Selecting _IfcMonetaryMeasure_ allows the specification only of the value, the currency being as set by the global context.
* Selecting _IfcRatioMeasure_ assumes that the amount is a percentage or other REAL number. Note that if the amount is normally specified as -20%, then this figure will need to be converted to a multiplier of 0.8

> HISTORY New select type in IFC2x2.
