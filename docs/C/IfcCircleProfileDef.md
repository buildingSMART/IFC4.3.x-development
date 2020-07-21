IfcCircleProfileDef
===================
_IfcCircleProfileDef_ defines a circle as the profile definition used by the
swept surface geometry or by the swept area solid. It is given by its _Radius_
attribute and placed within the 2D position coordinate system, established by
the _Position_ attribute.  
  
> HISTORY  New entity in IFC1.5.  
  
Figure 1 illustrates parameters for the circle profile definition. The
parameterized profile defines its own position coordinate system. The
underlying coordinate system is defined by the swept surface or swept area
solid that uses the profile definition. It is the xy plane of either:  
  
* _IfcSweptSurface.Position_  
* _IfcSweptAreaSolid.Position_  
  
Or in case of sectioned spines, it is the xy plane of each list member of
_IfcSectionedSpine.CrossSectionPositions_. By using offsets of the position
location, the parameterized profile can be positioned centric (using x,y
offsets = 0.), or at any position relative to the profile. Explicit coordinate
offsets are used to define cardinal points (e.g. upper-left bound). The
_Position_ attribute defines the 2D position coordinate system of the circle.  
The _Radius_ attribute defines the radius of the circle.  
  
!["circle profile"](../figures/ifccircleprofiledef-layout1.gif "Figure 1 --
Circle profile")  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcprofileresource/lexical/ifccircleprofiledef.htm)


Attribute definitions
---------------------
| Attribute   | Description               |
|-------------|---------------------------|
| Radius      | The radius of the circle. |

