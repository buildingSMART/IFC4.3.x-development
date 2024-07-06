An _IfcImageTexture_ provides a 2-dimensional texture that can be applied to a surface of an geometric item and that provides lighting parameters of a surface onto which it is mapped. The texture is provided as an image file at an external location for which an URL is provided.

<!-- end of short definition -->


The following definitions from ISO/IEC 19775-1 X3D Architecture and base components ([X3D Specification](http://www.web3d.org/x3d/specifications/)) apply:

* Greyscale pixels without alpha or simple transparency are treated as intensity textures.
* Greyscale pixels with alpha or simple transparency are treated as intensity plus alpha textures.
* RGB pixels without alpha channel or simple transparency are treated as full RGB textures.
* RGB pixels with alpha channel or simple transparency are treated as full RGB plus alpha textures.
* If the image specifies colours as indexed-colour (that is, palettes or colourmaps), the following semantics should be used (note that `greyscale' refers to a palette entry with equal red, green, and blue values):
 1. If all the colours in the palette are greyscale and there is no transparency chunk, it is treated as an intensity texture.
 2. If all the colours in the palette are greyscale and there is a transparency chunk, it is treated as an intensity plus opacity texture.
 3. If any colour in the palette is not grey and there is no transparency chunk, it is treated as a full RGB texture.
 4. If any colour in the palette is not grey and there is a transparency chunk, it is treated as a full RGB plus alpha texture.
* Texture nodes that require support for JPEG files shall interpret JPEG files as follows:
 1. Greyscale files (number of components equals 1) are treated as intensity textures.
 2. YCbCr files are treated as full RGB textures.
 3. No other JPEG file types are required. It is recommended that other JPEG files are treated as a full RGB textures.
* Texture nodes that recommend support for GIF files shall follow the applicable semantics described above for the PNG format.

The Uniform Resource Locator (URL) is a form of an URI and specified in [RFC1738](http://www.ietf.org/rfc/rfc1738.txt?number=1738) by IETF. It supports resources located on a particular server being accessed by a particular protocol (usually http), and resources located at a local machine.

> NOTE Exchange files following the ifcZIP convention may include a sub directory structure for image resources to be stored together with the product data set.

>> NOTE The definitions of texturing within this standard have been developed in dependence on the texture component of X3D. See ISO/IEC 19775-1.2:2008 X3D Architecture and base components Edition 2, Part 1, 18 Texturing component for the definitions in the international standard.
>

> HISTORY New entity in IFC2x2.

## Attributes

### URLReference
Location, provided as an URI, at which the image texture is electronically published.
