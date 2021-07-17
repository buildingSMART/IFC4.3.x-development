IfcFillAreaStyleTiles
=====================

The _IfcFillAreaStyleTiles_ defines the filling of an _IfcAnnotationFillArea_ by recurring patterns of styled two dimensional geometry, called a tile. The recurrence pattern is determined by two vectors, that multiply the tile in regular form.

The two vectors act as a two dimensional repeat factor that determins eight new positions for the tiles.

{ .extDef}
> NOTE&nbsp; Definition according to ISO 10303-46:  
> The fill area style tiles defines a two dimensional tile to be used for the filling of annotation fill areas or other closed regions. The content of a tile is defined by the tile set, and the placement of each tile determined by the filling pattern which indicates how to place tiles next to each other. Tiles or parts of tiles outside of the annotation fill area or closed region shall be clipped at the of the area or region.

{ .extDef}
> _I + k~1~\* R~1~ +
k~2~\* R~2~_ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_k~1~,k~2~_= -1,0,1 , ![formula](../../../../../../figures/ifcfillareastyletilesymbolwithstyle_fig1.gif)
> 
> Figure 1 shows the use of a vector for hatch line distances
> 
> !["IfcFillAreaStyleTiles_Fig1.gif 12,9 KB"](../../../../../../figures/ifcfillareastyletiles_fig1.gif "Figure 1 &mdash; two vectors as two direction repeat factor")

> NOTE&nbsp; Entity adapted from **fill_area_style_tiles** defined in ISO10303-46

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; _TilingPattern_ changed to list of two _IfcVector_, _Tiles_ refer directly to _IfcStyledItem_.
