IfcTextureCoordinate
====================
The _IfcTextureCoordinate_ is an abstract supertype of the different kinds to
apply texture coordinates to geometries. For vertex based geometries an
explicit assignment of 2D texture vertices to the 3D geometry points is
supported by the subtype _IfcTextureMap_, in addition there can be a
procedural description of how texture coordinates shall be applied to
geometric items. If no _IfcTextureCoordinate_ is provided for the
_IfcSurfaceTexture_, the default mapping shall be used.  
  
> NOTE  See relevant subtypes of _IfcGeometricRepresentationItem_ for default
> texture mapping description.  
  
> NOTE  The definitions of texturing has been adapted from X3D Architecture
> and base components, section 18 **Texturing component** as defined in
> ISO/IEC 19775-1.2  
  
> HISTORY  New entity in IFC2x2.  
  
{ .change-ifc2x3}  
> IFC2x3 CHANGE  The attribute Texture is deleted.  
  
{ .change-ifc2x4}  
> IFC4 CHANGE  The inverse attribute AnnotatedSurface isdeleted, and the
> attribute _Maps_ is added.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpresentationappearanceresource/lexical/ifctexturecoordinate.htm)


Associations
------------
| Attribute   | Description   |
|-------------|---------------|
| Maps        |               |

