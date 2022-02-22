# IfcTextureCoordinateIndices

The _IfcTextureCoordinateIndices_ provide the texture coordinates for an _IfcIndexedPolygonalFace_. The list of _TexCoordIndex_ holds the indices into the _IfcTextureVertexList_ that correspond to the list of _CoordIndex_ at _TexCoordsOf_.

> HISTORY&nbsp; New entity in IFC4.3.0.0

## Attributes

### TexCoordsOf
The _IndexedPolygonalFace_ for which the texture coordinates are provided.

### TexCoordIndex
List of index pointers into the _IfcTextureVertexList_ referenced by the inherited attribute _TexCoords_.
