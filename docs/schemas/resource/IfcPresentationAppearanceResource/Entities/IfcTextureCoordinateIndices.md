# IfcTextureCoordinateIndices

The _IfcTextureCoordinateIndices_ provide the texture coordinates for an _IfcIndexedPolygonalFace_. The _TexCoordIndex_ holds a list of indices pointing into the _IfcTextureVertexList_ for texture coordinates that correspond to the _TexCoordsOf.CoordIndex_ holding a list of indices pointing into the _IfcCartesianPointList3D_ for vertex coordinates.
> HISTORY&nbsp; New entity in IFC4.3.0.0

## Attributes

### TexCoordsOf
The _IndexedPolygonalFace_ for which the texture coordinates are provided.

### TexCoordIndex
List of index pointers into the _IfcTextureVertexList_ referenced by the inherited attribute _TexCoords_.