BreakerUnitIPICurve
===================

A curve that establishes the let through peak current of a breaker unit when a particular prospective current is applied.  Note that the breaker unit IPI curve is defined within a Cartesian coordinate system and this fact must be asserted within the property set:

(1) Defining value: A list of minimum 2 and maximum 16 numbers providing the currents in [A] for points in the I/Î log/log coordinate space. The curve is drawn as a straight line between two consecutive points.
(2) Defined value: A list of minimum 2 and maximum 16 numbers providing the let-through peak currents, Î, in [A] for points in the I/Î log/log coordinate space. The curve is drawn as a straight line between two consecutive points.
