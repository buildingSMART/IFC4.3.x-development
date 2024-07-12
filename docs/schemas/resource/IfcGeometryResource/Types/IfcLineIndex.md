# IfcLineIndex

The _IfcLineIndex_ describes a single or multiple straight segments within a poly curve by providing a list on indices. The first index is the start point of the line segment, the last index is the end point of the line segment. If more than two indices are included, then all intermediate indices define intermediate points of the poly line segment connected in the order of appearance of the list of indices.
<!-- end of short definition -->


> NOTE The type is used for _IfcIndexedPolyCurve_ to point into an _IfcCartesianPointList_ for providing the Cartesian points of the straight segments of the poly curve.

> HISTORY New Type in IFC4 ADD1
