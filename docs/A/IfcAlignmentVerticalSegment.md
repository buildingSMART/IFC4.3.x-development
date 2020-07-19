IfcAlignmentVerticalSegment
===========================
Geometric segments are used to define the vertical alignment. The segments are
ordered. Each vertical segment is defined with:  

  

  * a starting point known by its distance along the horizontal alignment [m]
  

  * the starting point elevation in [m]
  

  * the starting direction as a gradient [‰]
  

  * the segment length in [m]
  

  * the information on how the segment is connected to the following segment. This information is used to describe possible discontinuities (e.g. if there is a vertical bend).
  

  
Additionally:  

  

  * a radius, for arc segments [m]
  

  * the initial and final radius for transition segments as well as the type of transition curve. Some transition curves require additional parameters.
  

  
The elevation (= Cartesian Z-coordinate) of the starting point, the segment
length and the starting gradient are defined for each geometric element.


