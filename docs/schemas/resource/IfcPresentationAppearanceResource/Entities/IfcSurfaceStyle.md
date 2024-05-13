# IfcSurfaceStyle

_IfcSurfaceStyle_ is an assignment of one or many surface style elements to a surface, defined by subtypes of _IfcSurface_, _IfcFaceBasedSurfaceModel_, _IfcShellBasedSurfaceModel_, or by subtypes of _IfcSolidModel_. The positive direction of the surface normal relates to the positive side. In case of solids the outside of the solid is to be taken as positive side.<!-- end of definition -->

> NOTE  The surface style is often referred to as material definition in rendering applications.

> NOTE  Corresponding ISO 10303 entity: surface_style_usage and surface_side_style. Please refer to ISO/IS 10303-46:1994 for the final definition of the formal standard. The surface style definition in regard to support of rendering has been greatly expanded beyond the scope of ISO/IS 10303-46.

> HISTORY  New entity in IFC2x.

## Attributes

### Side
An indication of which side of the surface to apply the style.

### Styles
A collection of different surface styles.

## Formal Propositions

### MaxOneShading
The _IfcSurfaceStyleShading_ shall only be used zero or one time within the set of _Styles_.

### MaxOneLighting
The _IfcSurfaceStyleLighting_ shall only be used zero or one time within the set of _Styles_.

### MaxOneRefraction
The _IfcSurfaceStyleRefraction_ shall only be used zero or one time within the set of _Styles_.

### MaxOneTextures
The _IfcSurfaceStyleWithTextures_ shall only be used zero or one time within the set of _Styles_.

### MaxOneExtDefined
The _IfcExternallyDefinedSurfaceStyle_ shall only be used zero or one time within the set of _Styles_.
