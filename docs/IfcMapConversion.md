IfcMapConversion
================
The map conversion deals with transforming the local engineering coordinate
system, often called world coordinate system, into the coordinate reference
system of the underlying map.  
  
> NOTE  The _IfcMapConversion_ does not handle the projection of a map from
> the geodetic coordinate reference system.  
  
The map conversion allows to convert the local origin of the local engineering
coordinate system to its place within a map (easting, northing, orthogonal
height) and to rotate the x-axis of the local engineering coordinate system
within the horizontal (easting/westing) plane of the map.  
  
> NOTE  The z axis of the local engineering coordinate system is always
> parallel to the z axis of the map coordinate system.  
  
The scale factor can be used when the length unit for the 3 axes of the map
coordinate system are not identical with the length unit established for this
project (see\S\ _IfcProject.UnitsInContext_), if omitted, the scale factor 1.0
is assumed.  
  
> HISTORY  New entity in IFC4  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcrepresentationresource/lexical/ifcmapconversion.htm)


