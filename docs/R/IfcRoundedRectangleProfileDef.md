IfcRoundedRectangleProfileDef
=============================
_IfcRoundedRectangleProfileDef_ defines a rectangle with equally rounded
corners as the profile definition used by the swept surface geometry or the
swept area solid. It is given by the X extent, the Y extent, and the radius
for the rounded corners, and placed within the 2D position coordinate system,
established by the _Position_ attribute. It is placed centric within the
position coordinate system, that is, in the center of the bounding box.  
  
> HISTORY  New entity in IFC2x.  
  
{ .change-ifc2x}  
> IFC2x CHANGE  The _IfcRoundedRectangleProfileDef_ is now subtyped from
> _IfcRectangleProfileDef_. The _XDim_ and _YDim_ attributes have been removed
> (now inherited from supertype).  
  
Figure 1 illustrates parameters of the rounded rectangle profile definition.  
  
  
  
  
  
| ![rounded rectangle profile](../figures/ifcroundedrectangleprofiledef-
layout1.gif)  
|  

_Position_  
  
  
The parameterized profile defines its own position coordinate system.  
The underlying  
coordinate system is defined by the swept surface or swept area solid  
that uses the profile definition. It is the xy plane of either:

  

  

  * IfcSweptSurface.Position
  

  * IfcSweptAreaSolid.Position
  

  
or in case of sectioned spines the xy plane of each list member of
IfcSectionedSpine.CrossSectionPositions.  
  
  
  
  
By using offsets of the position location, the parameterized profile  
can be positioned centric (using x,y offsets = 0.), or at any position  
relative to the profile. Explicit coordinate offsets are used to define  
cardinal points (e.g. upper-left bound).  

_Parameter_  
  
  
The _IfcRoundedRectangleProfileDef_  
is defined within the  
position coordinate system, where the _XDim_  
defines the measure  
for the length of the rectangle (half along the positive x-axis), the _YDim_  
defines the length measure for the width of the rectangle (half along  
the positive y-axis) and the _RoundingRadius_  
defines the radius  
of curvature in all four corners of the rectangle.

  
  
  
---|---  
  
  
  
  
  

Figure 1 -- Rounded rectangle profile  
  
  
  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcprofileresource/lexical/ifcroundedrectangleprofiledef.htm)


