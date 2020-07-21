IfcAlignmentHorizontalSegment
=============================
Geometric segments are used to define the horizontal alignment. The segments
are ordered. Each horizontal segment is defined with:  

  

  * a starting point known by its cartesian coordinates
  

  * the starting direction in form of an azimuth [gon] or alternatively [rad](radiant).
  

  * the segment length in [m]
  

  * the information on how the segment is connected to the following segment. This information is used to describe possible discontinuities (e.g. if there is a horizontal bend).
  

  
Additionally:  

  

  * a radius, for arc segments
  

  * an initial and final radius for transition segments as well as the type of transition curve. Some transition curves require additional parameters.
  

  
  


Attribute definitions
---------------------
| Attribute             | Description                                                   |
|-----------------------|---------------------------------------------------------------|
| Starting Point        | Horizontal Cartesian coordinates (X, Y) of the starting point |
| Starting Direction    | Horizontal azimuth at the starting point                      |
| Segment Length        | Length of the horizontal segment                              |
| Tangential Continuity | Tangential Continuity for the end point. Possible values are:

  * Not connected according national regulation
  * Connect with directional bend
  * Connected                                                               |

