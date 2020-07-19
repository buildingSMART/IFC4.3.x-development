IfcAlignment2DHorizontalSegment
===============================
Individual segment along the _IfcAlignment2DHorizontal_, being defined in the
x/y coordinate space. Each single horizontal alignment segment has an
associated curve geometry. The following segment curve types are defined by
the _CurveGeometry_:  
  
* for line segment - _IfcLineSegment2D_  
* circular arc segment - _IfcCircularArcSegment2D_  
* clothoidal arc segment - _IfcClothoidalArcSegment2D_  
  
For each horizontal segment, the following non-redundant information is
provided:  
  
* the start point (in x/y coordinates)  
* the start direction (in radians or degree, with local x (east) being 0, and increasing counter-clock wise)  
* the segment length  
* the curve parameter needed for circular and clothoidal arc segments  
  
The following information can be calculated (and is therefore not exchanged
explicitly to avoid redundancy and inconsistencies)  
  
* the end point (from start point, direction, segment length and curve parameter)  
* the start distance along (from the end distance along of the previous segment, or the start distance along of the horizontal alignment (if it is the first segment)  
* the end distance along (from the start distance and the segment length)  
* the end direction (from the curve parameter, the start direction and the segment length)  
* the point of intersection (from the start direction and the end direction)  
  
The following checks can be done to validate the correct exchange:  
  
* continuity \X2\2013\X0\ does the calculated end point of the previous segment matches with the provided start point of this segment  
* tangential continuity \X2\2013\X0\ does the calculated end direction of the previous segment matches with the provided start direction of this segment  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricconstraintresource/lexical/ifcalignment2dhorizontalsegment.htm)


