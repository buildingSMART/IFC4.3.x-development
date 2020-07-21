IfcExtrudedAreaSolidTapered
===========================
_IfcExtrudedAreaSolidTapered_ is defined by sweeping a cross section along a
linear spine. The cross section may change along the sweep from the shape of
the start cross section into the shape of the end cross section. The resulting
solid is bounded by three or more faces: A start face, an end face (each
defined by start and end planes and sections), and one or more lateral faces.
Each lateral face is a ruled surface defined by a pair of corresponding edges
of the start and end section.  
  
> NOTE  Given that the start and end section is provided by a polygon, the
> corresponding vertices of the start and end cross section are connected,
> forming a quadrilateral polygon between each pair of corresponding vertices.
> The surface defined by the bounding quadrilateral polygon is a ruled
> surface, that could be approximated by triangulation.  
  
The linear spine is defined by:  
  
* Start point: _SELF\\\IfcSweptAreaSolid.Position.Location_  
* Direction: _SELF\\\IfcExtrudedAreaSolid.ExtrudedDirection_  
* Distance: _SELF\\\IfcExtrudedAreaSolid.Depth_  
  
The start cross section is defined by _SELF\\\IfcSweptAreaSolid.SweptArea_:  
  
* A bounded planar surface lying in the XY plane of the position coordinate system defined by _SELF\\\IfcSweptAreaSolid.Position.P[1]_ and _SELF\\\IfcSweptAreaSolid.Position.P[2]_  
* The linear spine starts at the plane of the start cross section. The spine is not necessarily perpendicular to the plane.  
  
The end cross section is defined by _EndSweptArea_:  
  
* A bounded planar surface lying in the XY plane of the position coordinate system defined by translating the start position coordinates provided by _SELF\\\IfcSweptAreaSolid.Position_ along the spine direction by the spine distance. The plane of the end cross section is coplanar to the plane of the start cross section.  
*   
* The end cross section is topologically similar to the start cross section (i.e. having the same number of vertices and edges).  
* The end cross section can either be defined by the same paramteric profile using different parameter values, or by a 2D Cartesian transformation of the start profile within the end cross section plane.   
  
In case of two parameterized profiles the shape is constructed as follows:  
  
* The end profile, defined by a cross section based on the same profile paramterization as the start profile, is translated by the spine distance along the spine direction.  
* It may be shifted within the XY plane of the end postion coordinate system and may be twisted using the rotation parameter.  
* The shift and rotation parameter are provided by the end cross section being of type _IfcParameterizedProfileDef_, where   
* Shift is _EndSweptArea\\\IfcParameterizedProfileDef.Position.Location_  
* Rotation is _EndSweptArea\\\IfcParameterizedProfileDef.Position.RefDirection_   
* Corresponding vertices of the start and end cross section are connected. Lateral faces are constructed as ruled surfaces between corresponding edges of start and end cross section.  
  
In case of Cartesian transformation of the start cross section the shape is
constructed as follows:  
  
* The cross section curve, which starts as a curve in the XY plane of the position coordinate system, is first scaled about the origin by the scale parameter. It is then translated by the spine distance along the spine direction. It maybe twisted by using the rotation parameter.  
* The scale and rotation parameter are provided by the end cross section being of type _IfcDerivedProfileDef_, where   
* Scale is _EndSweptArea\\\IfcDerivedProfileDef.Operator.Scale_  
* Rotation is _EndSweptArea\\\IfcDerivedProfileDef.Operator.Axis1_   
* Corresponding vertices of the start and end cross section are connected. Lateral faces are constructed as ruled surfaces between corresponding edges of start and end cross section.  
  
> HISTORY  New entity in IFC4.  
  
{ .spec-head}  
Informal Propositions:  
  
1\. Mirroring within _IfcDerivedProfileDef.Operator_ shall not be used  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcextrudedareasolidtapered.htm)


Formal Propositions
-------------------
| Rule                     | Description   |
|--------------------------|---------------|
| CorrectProfileAssignment |               |

Associations
------------
| Attribute    | Description   |
|--------------|---------------|
| EndSweptArea |               |

