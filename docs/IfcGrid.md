IfcGrid
=======
_IfcGrid_ ia a planar design grid defined in 3D space used as an aid in
locating structural and design elements. The position of the grid
(_ObjectPlacement_) is defined by a 3D coordinate system (and thereby the
design grid can be used in plan, section or in any position relative to the
world coordinate system). The position can be relative to the object placement
of other products or grids. The XY plane of the 3D coordinate system is used
to place the grid axes, which are 2D curves (for example, line, circle, arc,
polyline).  
  
The inherited attributes _Name_ and _Description_ can be used to define a
descriptive name of the grid and to indicate the grid''s purpose. A grid is
defined by (normally) two, or (in case of a triangular grid) three lists of
grid axes. The following figures shows some examples.  
  
A grid may support a rectangular layout as shown in Figure 1, a radial layout
as shown in Figure 2, or a triangular layout as shown in Figure 3.  
  
> NOTE  The _PredefinedType_ denotes the type of grid that is represented by
> _IfcGrid_. The instantiation of _IfcGridAxis_''s has to agree to the
> _PredefinedType_, if provided.  
  
> NOTE  The grid axes, defined within the design grid, are those elements to
> which project objects will be placed relatively using the
> _IfcGridPlacement_.  
  
  
  
  
  
![1](figures/ifcdesigngrid-type1.gif)  
  
|  
![2](figures/ifcdesigngrid-type2.gif)  
  
|  
![3](figures/ifcdesigngrid-type3.gif)  
  
  
---|---|---  
  
  
  

Figure 1 -- Grid rectangular layout

  
  
|  

Figure 2 -- Grid radial layout

  
  
|  

Figure 3 -- Grid triangular layout

  
  
  
  
  
  
  
> HISTORY  New entity in IFC1.0.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The attribute _PredefinedType_ has been added at the end of the
> attribute list.  
  
  
  
{ .spec-head}  
Informal Propositions:  
  
  
  
  

  

  1. Grid axes, which are referenced in different lists  
of axes (UAxes, VAxes, WAxes) shall not be parallel.  

  

  2. Grid axes should be defined such as there are no  
two grid axes which intersect twice (see Figure 189).  

  

  

>  
>  NOTE  Left side: ambiguous intersections A1 and  
>  A2, a grid containing such grid axes is not a valid  
>  design grid;  Right side: the conflict can be  
>  resolved by splitting one grid axis in a way, such as  
>  no ambiguous intersections exist.  
>

  
  
|  
![IP2](figures/ifcdesigngrid-ip2.gif)  

Figure 4 -- Grid intersections

  
  
  
---|---  
  
  
[_bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcproductextension/lexical/ifcgrid.htm)


