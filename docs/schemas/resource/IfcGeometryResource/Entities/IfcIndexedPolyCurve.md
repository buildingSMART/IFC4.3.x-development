# IfcIndexedPolyCurve

The _IfcIndexedPolyCurve_ is a bounded curve with only linear and circular arc segments defined by a Cartesian point list and an optional list of segments, providing indices into the Cartesian point list. In the case that the list of _Segments_ is not provided, all points in the _IfcCartesianPointList_ are connected by straight line segments in the order they appear in the _IfcCartesianPointList_.<!-- end of definition -->

In the case that the list of _Segments_ is provided, it is interpreted as such:

* Segment of type _IfcLineIndex_: The first index is the start point of the poly line segment, the last index is the end point of the poly line segment. If more than two indices are included, then all intermediate indices define intermediate points of the polyline connected in the order of appearance of the indices;
* Segment of type _IfcArcIndex_: The first index is the start point of the circular arc, the second index is a point on arc, the third index is the end point of the circular arc. The three points shall not be co-linear. In case that this informal proposition is not maintained, the arc segment shall be treated as a polyline segment.

> EXAMPLE Figure 2 illustrates a bounded open _IfcIndexedPolyCurve_ having straight and arc segments. In this example, the straight segments only have two points and one edge, however more then two indices into the Cartesian point list can be includes, defining a multi edge polyline segment.

![poly curve with arcs examples](../../../../figures/ifcindexedpolycurve-fig1.png "Figure 2 — Bounded open _IfcIndexedPolyCurve_ with straight and arc segments")

> EXAMPLE Figure 2 illustrates a bounded open _IfcIndexedPolyCurve_ having only straight segments. In this example, no list of _Segments_ is provided, hence the points are drawn in the order of their appearance in the _IfcCartesianPointList_.

![poly curve examples](../../../../figures/ifcindexedpolycurve-fig2.png "Figure 2 — Bounded open _IfcIndexedPolyCurve_ with only straight segments")

The _IfcIndexedPolyCurve_ represents an open or a closed curve depending on the following condition:

* In the case that the list of _Segments_ is provided: If the last index of the last _Segment_ and the first index of the first _Segment_ are identical, then the poly curve is a closed curve, otherwise it is an open curve.
* In the case that the list of _Segments_ is not provided: If the first and the last Cartesian point in the Cartesian point list are identical, then the poly curve is a closed curve, otherwise it is an open curve.

> HISTORY New entity in IFC4 ADD1

**Informal Propositions**

1. Any two consecutive points of the _IfcIndexedPolyCurve_ shall not be coincident after taking the _Precision_ factor into account, given by the applicable _IfcGeometricRepresentationContext_.
2. The three points of any _IfcArcIndex_ segment of the _IfcIndexedPolyCurve_ shall not be colinear after taking the _Precision_ factor into account, given by the applicable _IfcGeometricRepresentationContext_.

## Attributes

### Points
A list of points, provided by a point list of either two, or three dimensions, that is used to define the poly curve. If the attribute _Segments_ is not provided, the poly curve is generated as a poly line by connecting the points in the order of their appearance in the point list. If the attribute _Segments_ is provided, the segments determine, how the points are to be used to create straight and circular arc segments.

### Segments
List of straight line and circular arc segments, each providing a list of indices into the Cartesian point list. Indices should preserve consecutive connectivity between the segments, the start index of the next segment shall be identical with the end index of the previous segment.

### SelfIntersect
Indication of whether the curve intersects itself or not; this is for information only.

## Formal Propositions

### Consecutive
If a list of indexed segments is provided, they need to be consecutive, meaning that the last index of all, but the last, segments shall be identical with the first index of the next segment.
