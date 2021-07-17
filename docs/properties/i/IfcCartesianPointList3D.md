IfcCartesianPointList3D
=======================

The _IfcCartesianPointList3D_ defines an ordered collection of three-dimentional Cartesian points. Each Cartesian point is provided as an three-dimensional point by a fixed list of three coordinates. The attribute _CoordList_ is a two-dimensional list, where

* first dimension is an unbounded list representing each 3D Cartesian point;
* second dimension is a fixed list of three list members, where [1] is the x-coordinate, [2] the y-coordinate and [3] the z-coordinate of the Cartesian point.

> NOTE&nbsp; The _IfcCartesianPointList_ is introduced to provide a compact representation of larger list of points, such as in point clouds, and in indexable representation of points used as vertices in tessellated items or poly curves.

> HISTORY&nbsp; New entity in IFC4.
