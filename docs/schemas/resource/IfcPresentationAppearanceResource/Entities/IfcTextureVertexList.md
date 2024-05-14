# IfcTextureVertexList

The _IfcTextureVertexList_ defines an ordered collection of texture vertices. Each texture vertex is a two-dimensional vertex provided by a fixed list of two texture coordinates. The attribute _TexCoordsList_ is a two-dimensional list, where<!-- end of definition -->

* first dimension is an unbounded list representing each texture vertex;
* second dimension is a fixed list of two list members, where [1] is the S-coordinate, and [2] the T-coordinate of the texture vertex.

> NOTE The _IfcTextureVertexList_ is introduced to provide a compact representation of an indexable representation of texture coordinates for texture maps in tessellated items.

> HISTORY New entity in IFC4.

## Attributes

### TexCoordsList
List of texture vertices defined by S-coordinate and T-coordinate.
