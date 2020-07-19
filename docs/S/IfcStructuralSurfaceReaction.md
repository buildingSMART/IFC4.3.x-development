IfcStructuralSurfaceReaction
============================
This entity defines a reaction which occurs distributed over a surface. A
surface reaction may be connected with a surface member or surface connection.  
  
> HISTORY  New entity in IFC4.  
  
****Coordinate Systems****:  
  
See definitions at _IfcStructuralActivity_.  
  
****Topology Use Definitions****:  
  
See definitions at _IfcStructuralActivity_.  
  
{ .spec-head}  
Informal Propositions:  
  

  

  1. If the surface reaction is of the predefined type CONST, _SELF\\\IfcStructuralActivity.AppliedLoad_ must not be of type _IfcStructuralLoadConfiguration_.
  

  2. If the surface reaction is of the predefined type BILINEAR, _SELF\\\IfcStructuralActivity.AppliedLoad_ shall be of type _IfcStructuralLoadConfiguration_ and shall contain three items with two-dimensional _IfcStructuralLoadConfiguration.Locations_ , defining the location of the result samples in local coordinates of the surface reaction.  

  3. If the surface reaction is of the predefined type DISCRETE, _SELF\\\IfcStructuralActivity.AppliedLoad_ shall be of type _IfcStructuralLoadConfiguration_ and shall contain two or more items with two-dimensional locations.  

  4. If the surface reaction is of the predefined type ISOCONTOUR, _SELF\\\IfcStructuralActivity.AppliedLoad_ shall be of type _IfcStructuralLoadConfiguration_ and shall contain the same number of items as the set _SELF.IfcProduct.Representation.Representations[?].Items_. Each item in the load configuration shall have a two-dimensional location, defining the location of the result samples in local coordinates of the surface reaction. Each item in _SELF\\\IfcStructuralActivity.AppliedLoad_ shall be located at exactly one of the isocontours.  

> NOTE  The set of representation items is unordered, hence result locations
> are required to correlate result values and isocontours.

  

> NOTE  Isocontours are represented as _IfcPCurve_ s which are defined in
> terms of surface parameters u,v, while result locations are given in local
> surface item coordinates x,y. It is strongly recommended that the surface
> parameterization u,v is scaled 1:1 in order to avoid different scales of u,v
> versus x,y. If u,v are scaled 1:1 and the _IfcPCurve_ ''s base surface is
> identical with the surface item''s base surface, u,v and local x,y are
> identical.

  

  

  5. All items in _SELF\\\IfcStructuralActivity.AppliedLoad\\\IfcStructuralLoadConfiguration.Values_ shall be of the same entity type.
  

  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcstructuralanalysisdomain/lexical/ifcstructuralsurfacereaction.htm)


