# IfcSurfaceStyleWithTextures

The entity _IfcSurfaceStyleWithTextures_ allows to include image textures in surface styles. These image textures can be applied repeating across the surface or mapped with a particular scale upon the surface.

The entity _IfcSurfaceStyleWithTextures_ is part of the surface style table for presentation information assigned to surfaces for shading, rendering and lighting with textures. The mapping of the texture onto the surface or the solid is determined by the texture coordinates, in absense of an _IfcTextureCoordinate_ assigned to each surface texture, a default mapping of the texture to the geometric face or surface applies.

Surface textures included in the _IfcSurfaceStyleWithTextures_ are two dimensional map formats. They define 2D images that contain an array of colour values describing the texture. Depending on the number of _IfcSurfaceTextures_ being included in the list of _Textures_ the _IfcSurfaceStyleWithTextures_ either describes a single texture, or a multi texture.

* single texture: a single surface texture is applied to the styled geometric item (entirely or partly) with optional repetition and texture transformation
* multi texture: two or more surface textures are applied to the styled geometric item (entirely or partly) with optional repetition, texture transformation or texture coordinate mapping being specific for each texture.

{ .spec-head}
Informal Propositions:

1. Only one instance of _IfcSurfaceStyleWithTextures_ shall be referenced by an _IfcStyledItem_ and be assigned to an _IfcGeometricRepresentationItem_

> NOTE&nbsp; The definitions of texturing within this standard have been developed in dependence on the texture component of X3D. See ISO/IEC 19775-1.2:2008 X3D Architecture and base components Edition 2, Part 1, 18 Texturing component for the definitions in the international standard.

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x3}
> IFC2x3 CHANGE&nbsp; inverse attribute _HasTextureCoordinates_ deleted.

## Attributes

### Textures
The textures applied to the surface. In case of more than one surface texture is included, the _IfcSurfaceStyleWithTexture_ defines a multi texture.
