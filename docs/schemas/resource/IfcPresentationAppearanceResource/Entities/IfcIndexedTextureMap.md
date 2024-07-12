# IfcIndexedTextureMap

The _IfcIndexedTextureMap_ provides the mapping of the 2-dimensional texture coordinates to the surface onto which it is mapped. It is used for mapping the texture to faces of tessellated face sets.<!-- end of definition -->

The _IfcIndexedTextureMap_ defines an index into an indexed list of texture coordinates. The _TexCoords_ are a two-dimensional list of texture coordinates provided by two parameter values. Subtypes of _IfcIndexedTextureMap_ establish the index attribute corresponding to subtypes of _IfcTessellatedFaceSet_ defining the corresponding index lists of vertices.

> HISTORY New entity in IFC4.

## Attributes

### MappedTo
Reference to the _IfcTessellatedFaceSet_ to which it applies the texture map.

### TexCoords
Indexable list of texture vertices.
