BreakerUnitCurve
================

A curve that establishes the let through energy of a breaker unit when a particular prospective current is applied.  Note that the breaker unit curve is defined within a Cartesian coordinate system and this fact must be asserted within the property set:

(1) Defining value: ProspectiveCurrent: A list of minimum 2 and maximum 16 numbers providing the currents in [A] for points in the current/I2t log/log coordinate space. The curve is drawn as a straight line between two consecutive points.
(2) Defined value: LetThroughEnergy: A list of minimum 2 and maximum 16 numbers providing the let-through energy, I2t, in [A2s] for points in the current/I2t log/log coordinate space. The curve is drawn as a straight line between two consecutive points.
