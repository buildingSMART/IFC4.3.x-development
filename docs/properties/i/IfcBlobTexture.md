IfcBlobTexture
==============

An _IfcBlobTexture_ provides a 2-dimensional distribution of the lighting parameters of a surface onto which it is mapped. The texture itself is given as a single binary blob, representing the content of a pixel format file. The file format of the pixel file is given by the _RasterFormat_ attribute and allowable formats are guided by where rule _SupportedRasterFormat_.

> NOTE&nbsp; Toolbox specific implementations of the binary datatype may restrict the maximum length of the binary blob to capture the raster file content.

For interpretation of the texture nodes see _IfcImageTexture_ definition.

> HISTORY&nbsp; New entity in IFC2x3.

{ .change-ifc2x4}
> IFC4 CHANGE&nbsp; Data type of _RasterCode_ has been corrected to BINARY.
