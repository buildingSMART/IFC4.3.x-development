# IfcIndexedPolygonalTextureMap

The _IfcIndexedPolygonalTextureMap_ provides the mapping of the 2-dimensional texture coordinates to a set of polygonal bounded faces onto which it is mapped. It is used for mapping the texture to faces of an _IfcPolygonalFaceSet_. Such faces may have inner loops.

The _TexCoords_ defined at supertype _IfcIndexedTextureMap_ are a two-dimensional list of texture coordinates provided by two parameter values. Each member of the set of _TexCoordIndices_ defines an unbounded index list corresponding to the vertices of the assigned polygonal face that points to the texture coordinates in _TexCoords_ for that vertex.

Figure 1 shows how to use _IfcIndexedPolygonalTextureMap_ to provide the texture and texture coordinates for _IfcPolygonalFaceSet_.

!["Instantiation diagram showing the use of _IfcIndexedPolygonalTextureMap_"](../../../../figures/ifcindexedpolygonaltexturemap_01.png "Figure 1 &mdash; Use of _IfcIndexedPolygonalTextureMap_")

> HISTORY&nbsp; New entity in IFC4.3.0.0

## Attributes

### TexCoordIndices
Set of texture coordinate indices for polygonal faces with and without inner loops.
