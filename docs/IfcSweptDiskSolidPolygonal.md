IfcSweptDiskSolidPolygonal
==========================
The _IfcSweptDiskSolidPolygonal_ is a _IfcSweptDiskSolid_ where the
_Directrix_ is restricted to be provided by an poly line only. An optional
_FilletRadius_ attribute can be asserted, it is then applied as a fillet to
all transitions between the segments of the poly line.  
  
> NOTE  The geometric item _IfcIndexedPolyCurve_ provides a more compact
> representation compared with _IfcPolyline_. Therefore it is the prefered
> curve representation for the _Directrix_. The _IfcIndexedPolyCurve_ shall
> not have _Segments_ defined, resticting it to a poly line only.  
  
> HISTORY  New entity in IFC4.  
  
{ .spec-head}  
Informal Propositions:  
  
1\. The _FilletRadius_, if provided, has to be smaller then or equal to the
length of the start and end segment of the _IfcPolyline_, and smaller then or
equal to one half of the lenght of the shortest inner segment.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcsweptdisksolidpolygonal.htm)


