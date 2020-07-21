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


Attribute definitions
---------------------
| Attribute                  | Description                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------------------|
| Starting Point             | Starting point defined by the distance along the horizontal alignment.                                                 |
| Starting Point alternative | Alternative to the distance along the starting point can also be defined with horizontal Cartesian coordinates (X, Y). |
| Starting Point Elevation   | Elevation of the starting point (= Cartesian Z-coordinate)                                                             |
| Starting Direction         | Gradient (=Vertical azimuth) at the starting point                                                                     |
| Segment Length             | Length of the vertical segment                                                                                         |
| Tangential Continuity      | Tangential Continuity for the end point. Possible values are:

  * Not connected according national regulation
  * Connect with directional bend


  * Connected                                                                                                                        |

