BreakerUnitFuseBreakingingCurve
===============================

A curve that establishes the let through breaking energy of a breaker unit when a particular prospective breaking current is applied.  Note that the breaker unit fuse breaking curve is defined within a Cartesian coordinate system and this fact must be:

(1) Defining value: ProspectiveCurrentBreaking: A list of minimum 2 and maximum 8 numbers providing the currents in [A] for points in the
current/breaking energy log/log coordinate space. The curve is drawn as a straight line between two consecutive points.
(2) Defined value: LetThroughBreakingEnergy: A list of minimum 2 and maximum 8 numbers providing the breaking energy whereby the fuse has provided a break, I2t, in [A2s] for points in the current/breakting_energy log/log coordinate space. The curve is drawn as a straight line between two consecutive.
