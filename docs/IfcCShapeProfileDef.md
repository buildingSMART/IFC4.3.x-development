IfcCShapeProfileDef
===================
_IfcCShapeProfileDef_ defines a section profile that provides the defining
parameters of a C-shaped section to be used by the swept area solid. This
section is typically produced by cold forming steel. Its parameters and
orientation relative to the position coordinate system are according to the
following illustration. The centre of the position coordinate system is in the
profile''s centre of the bounding box.  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x3}  
> IFC2x3 CHANGE  All profile origins are now in the center of the bounding
> box.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Type of _InternalFilletRadius_ relaxed to allow for zero
> radius. Trailing attribute _CentreOfGravityInX_ deleted, use respective
> property in _IfcExtendedProfileProperties_ instead.  
  
Figure 1 illustrates parameters of the C-shape profile definition. The
parameterized profile defines its own position coordinate system. The
underlying coordinate system is defined by the swept area solid that uses the
profile definition. It is the xy plane of:  
  
* _IfcSweptAreaSolid.Position_  
  
By using offsets of the position location, the parameterized profile can be
positioned centric (using x,y offsets = 0.), or at any position relative to
the profile. The parameterized profile is defined by a set of parameter
attributes. In the illustrated example, the ''CentreOfGravityInX'' property in
_IfcExtendedProfileProperties_, if provided, is negative.  
  
!["C-shape profile"](figures/ifccshapeprofiledef.gif "Figure 1 -- C-shape
profile")  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcprofileresource/lexical/ifccshapeprofiledef.htm)


