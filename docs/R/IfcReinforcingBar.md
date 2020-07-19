IfcReinforcingBar
=================
A reinforcing bar is usually made of steel with manufactured deformations in
the surface, and used in concrete and masonry construction to provide
additional strength. A single instance of this class may represent one or many
of actual rebars, for example a row of rebars.  
  
> HISTORY  New entity in IFC2x2  
  
{ .change-ifc2x4}  
> IFC 2x4 CHANGE  All attributes are optional now. Several attributes are
> deprecated; their information now provided by _IfcReinforcingBarType_.
> Attribute _BarRole_ renamed to _PredefinedType_.  
  
{ .use-head}  
Geometry Use Definition  
  
Placement and representation are defined at the supertype
_IfcElementComponent_.  
  
The representation map of a mapped ''Body'' representation should contain a
representation of type ''AdvancedSweptSolid'' which holds an
_IfcSweptDiskSolid_ (including subtype _IfcSweptDiskSolidPolygonal_).  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralelementsdomain/lexical/ifcreinforcingbar.htm)


