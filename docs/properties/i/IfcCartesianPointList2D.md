IfcCartesianPointList2D
=======================

The _IfcCartesianPointList2D_ defines an ordered collection of two-dimentional Cartesian points. Each Cartesian point is provided as an two-dimensional point by a fixed list of two coordinates. The attribute _CoordList_ is a two-dimensional list, where

* first dimension is an unbounded list representing each 2D Cartesian point;
* second dimension is a fixed list of two list members, where [1] is the x-coordinate, and [2] the y-coordinate of the Cartesian point.

> NOTE&nbsp; The _IfcCartesianPointList2D_ is introduced to provide a compact representation of larger list of points, such as in indexable representation of points used as vertices in poly curves.

> HISTORY&nbsp; New entity in IFC4 ADD1.
