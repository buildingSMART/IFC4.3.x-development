# IfcArcIndex

The _IfcArcIndex_ describes a single circular arc segment within a poly curve by providing a list on indices. The first index is the start point of the circular arc, the second index is a point on arc, the third index is the end point of the circular arc. The three points shall not be co-linear.

> NOTE  The type is used for _IfcIndexedPolyCurve_ to point into an _IfcCartesianPointList_ for providing the Cartesian points of the circular arc segments of the poly curve.

> HISTORY  New Type in IFC4 ADD1

{ .spec-head}
Informal Propositions:

1. The second index, resolving to a point on arc, shall resolve into a Cartesian point that has approximately the same distance to the start point and the end point of the circular arc. This is due to avoid numeric instability, if the point on arc is too close to either the start or the end point.
