IfcCartesianPointList2D
=======================
The _IfcCartesianPointList2D_ defines an ordered collection of two-dimentional
Cartesian points. Each Cartesian point is provided as an two-dimensional point
by a fixed list of two coordinates. The attribute _CoordList_ is a two-
dimensional list, where  
  
* first dimension is an unbounded list representing each 2D Cartesian point;  
* second dimension is a fixed list of two list members, where [1] is the x-coordinate, and [2] the y-coordinate of the Cartesian point.  
  
> NOTE  The _IfcCartesianPointList2D_ is introduced to provide a compact
> representation of larger list of points, such as in indexable representation
> of points used as vertices in poly curves.  
  
> HISTORY  New entity in IFC4 ADD1.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifccartesianpointlist2d.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CoordList   | Two-dimensional list of Cartesian points provided by two coordinates.                                                                                                     |
| TagList     | List of tags corresponding to each point that may be used to identify a basis curve according to the Tag attribute at _IfcOffsetCurveByDistances_ or _IfcAlignmentCurve_. |

