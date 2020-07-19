IfcTShapeProfileDef
===================
_IfcTShapeProfileDef_ defines a section profile that provides the defining
parameters of a T-shaped section to be used by the swept area solid. Its
parameters and orientation relative to the position coordinate system are
according to the following illustration. The centre of the position coordinate
system is in the profile''s centre of the bounding box.  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x3}  
> IFC2x3 CHANGE  All profile origins are now in the center of the bounding
> box.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Type of _FilletRadius_, _FlangeEdgeRadius_, and _WebEdgeRadius_
> relaxed to allow for zero radius. Trailing attribute _CentreOfGravityInY_
> deleted, use respective property in _IfcExtendedProfileProperties_ instead.  
  
Figure 1 illustrates parameters of the T-shape profile definition.  
  
  
  
  
  
|  
![T-shape profile](../figures/ifctshapeprofiledef.gif)  
  
  
|  
  

_Position_  
  
The parameterized profile defines its own position coordinate system.  
The underlying  
coordinate system is defined by the swept area solid  
that uses the profile definition. It is the xy plane of:

  

  

  * IfcSweptAreaSolid.Position
  

  

by using offsets of the position location, the parameterized profile  
can be positioned centric (using x,y offsets = 0.), or at any position  
relative to the profile.

  
  
  
  
---|---  
  
  
  
  
  

Figure 1 -- T-shape profile  
  
  
  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcprofileresource/lexical/ifctshapeprofiledef.htm)


