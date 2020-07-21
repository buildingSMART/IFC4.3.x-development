IfcAlignment2DVerticalSegment
=============================
Individual segment along the _IfcAlignment2DVertical_, being defined in the
distance-along/z coordinate space.  
  
The vertical alignment is defined by segments that connects end-to-start. The
vertical alignment curve geometry is defined in a plane with x = distance
along horizontal, the y = height (or elevation). The transition at the segment
connection is not enforced to be tangential, if the \X2\201C\X0\tangential
continuity\X2\201D\X0\ flag is set to false, otherwise a tangential continuity
shall be preserved.  
  
The following vertical segment types are defined:  
  
* line segment - _IfcAlignment2DVerSegLine_  
* circular arc segment - _IfcAlignment2DVerSegCircularArc_  
* parabolic arc segment - _IfcAlignment2DVerSegParabolicArc_ which can describe symmetric and unsymmetric parabolas  
  
For each vertical segment, the following non-redundant information is
provided:  
  
* the start point (in distance along/ height coordinates)  
* the start gradient (as a ratio measure with horizontal being 0, uphill positive, and downhill negative) usually between 1 < n < -1 (equal to a percentage of 100% < n < -100%, or to a degree of 45° < n < -45° but higher values are possible)  
* the length (as horizontal length along the distance along (not the curve segment length))  
* the curve parameter needed for circular and parabolic arc segments  
  
The following information can be calculated (and is therefore not exchanged
explicitly to avoid redundancy and inconsistencies)  
  
* the end distance along (from the distance along and segment length)  
* the end height (from start distance along, gradient, length and curve parameter)  
* the end direction (from start direction, segment length and curve parameter)  
* the point of vertical intersection (from start direction and end direction)  
  
The following checks can be done to validate the correct exchange:  
  
* continuity \X2\2013\X0\ does the calculated end distance along of the previous segment matches with the provided start distance along of this segment  
* tangential continuity \X2\2013\X0\ does the calculated end gradient of the previous segment matches with the provided start gradient of this segment  
  
> NOTE  Specific subtypes of the IfcAlignment2DVerticalSegment add specific
> geometric curve parameters. Connectivity between vertical segments is not
> necessarily tangential, but this can be enforced as a requirement through
> the attribute _TangentialContinuity_.  
  
!(../figures/ifcalignment2dverticalsegment.png "Figure 1 -- Alignment vertical
segment")  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricconstraintresource/lexical/ifcalignment2dverticalsegment.htm)


Attribute definitions
---------------------
| Attribute        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StartDistAlong   | Distance along the horizontal alignment, measured along the _IfcAlignment2DHorizontal_ given in the length unit of the global _IfcUnitAssignment_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| HorizontalLength | Length measured as distance along the horizontal alignment of the segment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| StartHeight      | Elevation in Z of the start point relative to the IfcAlignment coordinate system.\X\0D> NOTE  It is strongly advised to not offset the IfcAlignment coordinate system from the project engineering coordinate system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| StartGradient    | Gradient of the tangent of the vertical segment at the start point. It is provided as a ratio measure. The ratio is percentage/100 (0.1 is equal to 10%). It has a theoretical range of -\X2\221E\X0\ < n < \X2\221E\X0\ using a ratio measure. The equivalent range measured in degree is -90\S\0 < n < 90\S\0.\X\0D> NOTE  For practical application of start gradient, the range of the ratio measure should be within the limits of -1 \X2\2264\X0\ n \X2\2264\X0\ 1 (equivalent in degree -45\S\0 \X2\2264\X0\ n \X2\2264\X0\ 45\S\0). However larger limits might apply for particular usages.\X\0D\X\0DPositive gradient means an increasing height at the start (or uphill), a negative gradient means decreasing height at the start (or downhill). |

Associations
------------
| Attribute   | Description   |
|-------------|---------------|
| ToVertical  |               |

