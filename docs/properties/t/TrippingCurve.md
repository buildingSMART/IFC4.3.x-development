TrippingCurve
=============

A curve that establishes the release time of a tripping unit when a particular prospective current is applied.  Note that the tripping curve is defined within a Cartesian coordinate system and this fact must be asserted within the property set:

(1) Defining value is the Prospective Current which is a list of minimum 2 and maximum 16 numbers providing the currents in [x In] for points in the current/time log/log coordinate space. The curve is drawn as a straight line between two consecutive points.
(2) Defined value is a list of minimum 2 and maximum 16 numbers providing the release_time in [s] for points in the current/time log/log coordinate space. The curve is drawn as a straight line between two consecutive points. Note that a defined interpolation.
