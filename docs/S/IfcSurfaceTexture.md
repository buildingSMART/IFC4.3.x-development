IfcSurfaceTexture
=================
An _IfcSurfaceTexture_ provides a 2-dimensional image-based texture map. It
can either be given by referencing an external image file through an URL
reference (_IfcImageTexture_), including the image file as a blob (long
binary) into the data set (_IfcBlobTexture_), or by explicitly including an
array of pixels (_IfcPixelTexture_).  
  
The following definitions from ISO/IEC 19775-1 X3D Architecture and base
components ([X3D Specification](http://www.web3d.org/x3d/specifications/))
apply:  
  

  

  * Texture: An image  
used in a texture map to create visual appearance effects when  
applied to geometry nodes.

  

  * Texture map: A  
texture plus the general parameters necessary for mapping the  
texture to geometry.

  

  
Texture are defined by 2D images that contain an array of colour values
describing the texture. The texture values are interpreted differently
depending on the number of components in the texture and the specifics of the
image format. In general, texture may be described using one of the following
forms:  
  
1\. Intensity textures (one-component)  
2\. Intensity plus alpha opacity textures (two-component)  
3\. Full RGB textures (three-component)  
4\. Full RGB plus alpha opacity textures (four-component)  
  
> NOTE  Image formats specify an alpha opacity, not transparency (where alpha
> = 1 - transparency).  
>  
  
  
Figure 1 illustrates the texture coordinate system.  
  
!["texture coordinates"](../figures/ifcsurfacetexture_fig-1.png "Figure 1 --
Surface texture coordinates")  
  
The following definitions from ISO/IEC 19775-1 X3D Architecture and base
components ([X3D Specification](http://www.web3d.org/x3d/specifications/)) on
texture coordinates apply:  
  
* Texture maps are defined in a 2D coordinate system (s, t) that ranges from [0.0, 1.0] in both directions. The bottom edge of the image corresponds to the S-axis of the texture map, and left edge of the image corresponds to the T-axis of the texture map. The lower-left pixel of the image corresponds to s=0, t=0, and the top-right pixel of the image corresponds to s=1, t=1. Texture maps may be viewed as two dimensional colour functions that, given an _(s,  t)_ coordinate, return a colour value _colour(s,  t)_.  
  
If multiple surface textures are included in the _IfcSurfaceStyleWithTextures_
applying them to a geometric item, a mode and optional parameters can be
included that blending operations.  
  
The _RepeatS_ and _RepeatT_ Boolean flags control whether the texture map is
repeated outside the [0.0, 1.0] texture coordinate range, when applied to a
geometric surface, or clamped to lie within the [0.0, 1.0] range. The
_TextureTransform_ applies a 2D non-uniform transformation to the texture
before it is applied to a geometric surface.  
  
The following definitions from ISO/IEC 19775-1 X3D Architecture and base
components ([X3D Specification](http://www.web3d.org/x3d/specifications/))
apply:  
  

  

  * These parameters  
support changes to the size, orientation, and position of textures  
on shapes. Note that these operations appear reversed when viewed  
on the surface of geometry. For example, a _scale_ value of (2  
2) will scale the texture coordinates and have the net effect of  
shrinking the texture size by a factor of 2 (texture coordinates  
are twice as large and thus cause the texture to repeat). A  
translation of (0.5 0.0) translates the texture coordinates +.5  
units along the S-axis and has the net effect of translating the  
texture −0.5 along the S-axis on the geometry''s surface. A  
rotation of π/2 of the texture coordinates results in a  
−π/2 rotation of the texture on the geometry.

  

  * The _center_  
field specifies a translation offset in texture coordinate space  
about which the _rotation_ and _scale_ fields are  
applied. The _scale_ field specifies a scaling factor in S and  
T of the texture coordinates about the _center_ point.  
 _scale_ values shall be in the range (−∞,∞).  
The _rotation_ field specifies a rotation in radians of the  
texture coordinates about the _center_ point after the scale  
has been applied. A positive rotation value makes the texture  
coordinates rotate counterclockwise about the centre, thereby  
rotating the appearance of the texture itself clockwise. The  
 _translation_ field specifies a translation of the texture  
coordinates.  
  
The following conventions  
apply:  
  

    * center =  
 _TextureTransform.LocalOrigin_ ;  
  
rotation = _TextureTransform.Axis1_  
  
scale S = _TextureTransform.Scale_  
  
scale T = _TextureTransform.Scale2_

  
  

  

  
> NOTE  The definitions of texturing within this standard have been developed
> in dependence on the texture component of X3D. See ISO/IEC 19775-1.2:2008
> X3D Architecture and base components Edition 2, Part 1, 18 Texturing
> component for the definitions in the international standard.  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  Attribute TextureType replaces by _Mode_, attributes
> _Parameter_ and _MapsTo_ aded, new inverse attribute _UsedInStyle_.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpresentationappearanceresource/lexical/ifcsurfacetexture.htm)


Attribute definitions
---------------------
| Attribute   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RepeatS     | The _RepeatS_ field specifies how the texture wraps in the S direction. If _RepeatS_ is TRUE (the default), the texture map is repeated outside the [0.0, 1.0] texture coordinate range in the S direction so that it fills the shape. If _RepeatS_ is FALSE, the texture coordinates are clamped in the S direction to lie within the [0.0, 1.0] range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| RepeatT     | The _RepeatT_ field specifies how the texture wraps in the T direction. If _RepeatT_ is TRUE (the default), the texture map is repeated outside the [0.0, 1.0] texture coordinate range in the T direction so that it fills the shape. If _RepeatT_ is FALSE, the texture coordinates are clamped in the T direction to lie within the [0.0, 1.0] range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Mode        | The _Mode_ attribute is provided to control the appearance of a multi textures. The mode then controls the type of blending operation. The mode includes a MODULATE for a lit appearance, a REPLACE for a unlit appearance, and variations of the two.\X\0D> NOTE  The applicable values for the _Mode_ attribute are determined by view definitions or implementer agreements. It is recommended to use the modes described in ISO/IES 19775-1.2:2008 X3D Architecture and base components Edition 2, Part 1. See [18.4.3 MultiTexture](http://www.web3d.org/x3d/specifications/ISO-IEC-19775-1.2-X3D-AbstractSpecification/Part01/components/texturing.html#MultiTexture) for recommended values.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  New attribute replacing previous TextureType.                                                                                                                                                                                  |
| Parameter   | The _Parameter_ attribute is provided to control the appearance of a multi textures. The applicable parameters depend on the value of the _Mode_ attribute.\X\0D> NOTE  The applicable values for the list of _Parameter_ attributes are determined by view definitions or implementer agreements. It is recommended to use the source and the function fields described in ISO/IES 19775-1.2:2008 X3D Architecture and base components Edition 2, Part 1. See [18.4.3 MultiTexture](http://www.web3d.org/x3d/specifications/ISO-IEC-19775-1.2-X3D-AbstractSpecification/Part01/components/texturing.html#MultiTexture) for recommended values. \X\0D> By convention, _Parameter[1]_ shall then hold the source value, _Parameter[2]_ the function value, _Parameter[3]_ the base RGB color for select operations, and _Parameter[4]_ the alpha value for select operations.\X\0D\X\0D{ .change-ifc2x4}\X\0D> IFC4 CHANGE  New attribute added at the end of the attribute list. |

Associations
------------
| Attribute        | Description   |
|------------------|---------------|
| TextureTransform |               |
| UsedInStyles     |               |
| IsMappedBy       |               |

