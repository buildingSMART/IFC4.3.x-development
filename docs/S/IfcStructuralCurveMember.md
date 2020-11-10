IfcStructuralCurveMember
========================
Instances of _IfcStructuralCurveMember_ describe edge members, i.e. structural
analysis idealizations of beams, columns, rods etc.. Curve members may be
straight or curved.  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Attribute _Axis_ and WHERE rule added. Use definitions changed.  
  
****Coordinate Systems****:  
  
See definitions at _IfcStructuralItem_. The local coordinate system is
established by the reference curve given by topology representation and by the
attribute _Axis_. The local x axis is parallel with the tangent on the
reference curve. The local z axis is located in the surface which is created
by sweeping _Axis_ along the reference curve and is directed according to
_Axis_. The local y axis is directed such that x,y,z form a right-handed
Cartesian coordinate system.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralanalysisdomain/lexical/ifcstructuralcurvemember.htm)


Attribute definitions
---------------------
| Attribute      | Description   |
|----------------|---------------|
| Axis           |               |
| PredefinedType |               |

