IfcCircleHollowProfileDef
=========================
_IfcCircleHollowProfileDef_ defines a section profile that provides the
defining parameters of a circular hollow section (tube) to be used by the
swept area solid. Its parameters and orientation relative to the position
coordinate system are according to the following illustration.The centre of
the position coordinate system is in the profile''s centre of the bounding box
(for symmetric profiles identical with the centre of gravity).  
  
> HISTORY  New entity in IFC2x2.  
  
Figure 1 illustrates parameters of the circular hollow profile definition. The
parameterized profile defines its own position coordinate system. The
underlying coordinate system is defined by the swept area solid that uses the
profile definition. It is the xy plane of:  
  
* _IfcSweptAreaSolid.Position_  
  
By using offsets of the position location, the parameterized profile can be
positioned centric (using x,y offsets = 0.), or at any position relative to
the profile. Explicit coordinate offsets are used to define cardinal points
(for example, upper-left bound). The parameterized profile is defined by a set
of parameter attributes.  
  
!["CHS-shape profile"](figures/ifccirclehollowprofiledef.gif "Figure 1 --
Circle hollow profile")  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcprofileresource/lexical/ifccirclehollowprofiledef.htm)


