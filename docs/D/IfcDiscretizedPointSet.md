IfcDiscretizedPointSet
======================
Class for grouping a set of discretized points. Each point set represents a
track axis alignment. The alignment curve is a non-parameterized space curve
that follows the ordered sequence of discretized points by straight lines (or
splines) between consecutive points. This is an alternative representation the
geometry of any track section described in the parameterized description.  


Attribute definitions
---------------------
| Attribute                     | Description                                                                                                                                                                                                                                    |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Associated discretized method | With which method the discretized points where defined:

  * straight lines (polynom)
  * splines (type of spline needed)
  * user defined                                                                                                                                                                                                                                                |
| Standard deviation horizontal | 1-sigma standard deviation [m] of a point in the horizontal plane. The value 0 indicates that the point was calculated and not measured.                                                                                                       |
| Standard deviation vertical   | 1-sigma standard deviation [m] of the point elevation. The value 0 indicates that the point was calculated and not measured.Remark:The 3D Standard deviation of a point can be calculated from the standard deviation horizontal and vertical. |

