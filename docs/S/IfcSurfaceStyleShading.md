IfcSurfaceStyleShading
======================
The _IfcSurfaceStyleShading_ allows for colour information and transparency
used for shading and simple rendering. The surface colour is used for
colouring or simple shading of the assigned surfaces and the transparency for
identifying translucency, where 0.0 is completely opaque, and 1.0 is
completely transparent.  
  
> HISTORY  New entity in IFC2x.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpresentationappearanceresource/lexical/ifcsurfacestyleshading.htm)


Attribute definitions
---------------------
| Attribute    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Transparency | The transparency field specifies how "clear" an object is, with 1.0 being completely transparent, and 0.0 completely opaque. If not given, the value 0.0 (opaque) is assumed.\X\0D> NOTE  The definition of 1 being transparent and 0 being opaque is the opposite of the definition in alpha channels, where 0.0 is completely transparent and 1.0 is completely opaque. This definition is due to upward compatibility to previous versions of this standard in different to the definition in _IfcIndexedColourMap_. |

Associations
------------
| Attribute     | Description   |
|---------------|---------------|
| SurfaceColour |               |

