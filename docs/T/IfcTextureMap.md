IfcTextureMap
=============
An _IfcTextureMap_ provides the mapping of the 2-dimensional texture
coordinates to the surface onto which it is mapped. It is used for mapping the
texture to surfaces of vertex based geometry models, such as  
  
* _IfcFacetedBrep_   
* _IfcFacetedBrepWithVoids_   
* _IfcFaceBasedSurfaceModel_   
* _IfcShellBasedSurfaceModel_   
  
The _IfcTextureMap_ has a list of _TextureVertex_, that corresponds to the
points of the outer face bound of the vertex based geometry item. The
corresponding pair of lists is:  
  
1\. the list of _Polygon_ of the _IfcFaceOuterBound_ of type
_IfcCartesianPoint_, and  
2\. the list of _Vertices_ of type _IfcTextureVertex_.  
  
Each _IfcTextureVertex_ (given as S, T coordinates of the 2-dimension texture
coordinate system) corresponds to the geometric coordinates of the
_IfcCartesianPoint_ (given as 3-dimension X, Y, and Z coordinates within the
object coordinate system of the geometric item).  
  
{ .extDef}  
> NOTE  Definition according to ISO/IEC 19775-1:  
> The TextureCoordinate node is a geometry property node that specifies a set
> of 2D texture coordinates used by vertex-based geometry nodes to map
> textures to vertices.  
  
> NOTE  In contrary to the X3D vertext based geometry, for example
> IndexedFaceSet and ElevationGrid, the vertext based geometry in IFC may
> include inner loops. The areas of inner loops have to be cut-out from the
> texture applied to the outer loop.  
  
  
  
  
![IfcTextureMap_fig-1.png 35,6 KB](../figures/ifctexturemap_fig-1.png)  
  
\X\09\X\09\X\09\X\09| Figure 1 illustrates applying a texture map to a vertex  
based geometry.  
\X\09\X\09\X\09\X\09  
  
---|---  
  
  
  

Figure 1 -- Texture map

  
  
\X\09\X\09\X\09\X\09|  
  
  
  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x3}  
> IFC2x3 CHANGE  The attribute Texture is deleted, and the attribute
> TextureMaps is added.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The attribute TextureMap is replaced by _Vertices_, and the
> attribute _AppliedTo_ is added.  
  
{ .spec-head}  
Informal Propositions:  
  
1\. The _IfcFace_ referenced in _AppliedTo_ shall be used by the vertex based
geometry, to which this texture map is assigned to by through the
_IfcStyledItem_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpresentationappearanceresource/lexical/ifctexturemap.htm)


