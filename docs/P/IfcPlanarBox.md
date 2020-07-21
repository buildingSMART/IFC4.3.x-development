IfcPlanarBox
============
A planar box specifies an arbitrary rectangular box and its location in a two
dimensional Cartesian coordinate system. If the planar box is used within a
three-dimensional coordinate system, it defines the rectangular box within the
XY plane.  
  
> NOTE  Entity adapted from **planar_box** defined in ISO10303-46  
  
> HISTORY  New entity in IFC2x2.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpresentationdefinitionresource/lexical/ifcplanarbox.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                                                                                                                                                                                                                    |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Placement   | The _IfcAxis2Placement_ positions a local coordinate system for the definition of the rectangle. The origin of this local coordinate system serves as the lower left corner of the rectangular box.\X\0D \X\0D> NOTE  In case of a 3D placement by _IfcAxisPlacement3D the _IfcPlanarBox_ is defined within the xy plane of the definition coordinate system._ |

