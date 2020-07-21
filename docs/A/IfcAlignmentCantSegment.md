IfcAlignmentCantSegment
=======================
Geometric segments are used to define the railway cant. The segments are
ordered. Each cant segment is defined with:  

  

  * a starting point known by its distance along the horizontal alignment [m]
  

  * the segment length in [m]
  

  * the start cant value in [mm]
  

  * the end cant value in [mm]
  

  * the information on how the segment is connected to the following segment. This information is used to describe possible discontinuities (e.g. invalid sudden change of cant or missing cant information if end point and starting point differ over a threshold).
  

  
Additionally:  

  

  * an information which describes if a smoothing was applied between two cant segments
  


Attribute definitions
---------------------
| Attribute                  | Description                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------------------|
| Starting Point             | Starting point defined by the distance along the horizontal alignment.                                                 |
| Starting point alternative | Alternative to the distance along the starting point can also be defined with horizontal Cartesian coordinates (X, Y). |
| Segment Length             | Length of the cant segment                                                                                             |
| Starting Cant left         | Value of the cant left at the beginning of the segment in [mm]                                                         |
| Ending Cant left           | Value of the cant left at the end of the segment in [mm]                                                               |
| Starting Cant right        | Value of the cant right at the beginning of the segment in [mm]                                                        |
| Endig Cant right           | Value of the cant right at the end of the segment in [mm]                                                              |
| Tangential Continuity      | Tangential Continuity for the end point. Possible values are:

  * Not connected according national regulation
  * Connect with smoothing


  * Connected                                                                                                                        |

