IfcCurveSegment2D
=================
The abstract definition of a bounded 2D curve representation item. Each curve
segment is defined by a start point, a start direction, a segment length and
additional curve geometry parameter. It defines arcs without the need to use a
trimmed curve.  
  
> NOTE  Such 2D curves are used in particular by horizontal alignment
> segments.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometryresource/lexical/ifccurvesegment2d.htm)


Attribute definitions
---------------------
| Attribute      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StartPoint     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| StartDirection | The direction of the tangent at the start point. Direction value 0. indicates a curve with a start tangent along the positive x-axis. Values increases counter-clockwise, and decreases clockwise. Depending on the plane angle unit, either degree or radians, the sensible range is -360\S\0 \X2\2264\X0\ n \X2\2264\X0\ 360\S\0 (or -2\X2\03C0\X0\ \X2\2264\X0\ n \X2\2264\X0\ 2\X2\03C0\X0\\). Values larger then a full circle (>|360\S\0| or >|2 \X2\03C0\X0\| shall not be used. |
| SegmentLength  | The length along the curve                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

