BreakerUnitFuseMeltingCurve
===========================

A curve that establishes the energy required to melt the fuse of a breaker unit when a particular prospective melting current is applied.  Note that the breaker unit fuse melting curve is defined within a Cartesian coordinate system and this fact must be:

(1) Defining value: ProspectiveCurrentMelting :A list of minimum 2 and maximum 8 numbers providing the currents in [A] for points in the
current/melting_energy log/log coordinate space. The curve is drawn as a straight line between two consecutive points.
(2) Defined value: MeltingEnergy: A list of minimum 2 and maximum 8 numbers providing the energy whereby the fuse is starting to melt, I2t, in [A2s] for points in the current/melting_energy log/log coordinate space. The curve is drawn as a straight line between two consecutive points.
