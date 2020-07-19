IfcStructuralLoadConfiguration
==============================
This class combines one or more load or result values in a 1- or 2-dimensional
configuration.  
  
> HISTORY  New entity in IFC4.  
  
{ .spec-head}  
Informal Propositions:  
  
1\. All items in _Values_ shall be of the same type.  
2\. If the loads or results comprise a curve activity, 1-dimensional locations
shall be given, measured locally along the curve. The location shall not
exceed the bounds of the curve actvity. The load samples and corresponding
locations shall be given in ascending order of locations.  
3\. If the loads or results comprise a surface activity, 2-dimensional
locations shall be given, measured in the surface activity''s local x and y
directions. The location shall not exceed the bounds of the surface activity.  
  
> NOTE  There are no ordering requirements in the 2-dimensional case, but the
> 1-dimensional case shall be spatially ordered for simplicity.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralloadresource/lexical/ifcstructuralloadconfiguration.htm)


