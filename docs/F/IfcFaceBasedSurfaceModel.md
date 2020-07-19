IfcFaceBasedSurfaceModel
========================
The _IfcFaceBasedSurfaceModel_ represents the a shape by connected face sets.
The connected faces have a dimensionality 2 and are placed in a coordinate
space of dimensionality 3.  
  
{ .extDef}  
> NOTE  Definition according to ISO/CD 10303-42:1992  
> A face based surface model is described by a set of connected face sets of
> dimensionality 2. The connected face sets shall not intersect except at
> edges and vertices, except that a face in one connected face set may overlap
> a face in another connected face set, provided the face boundaries are
> identical. There shall be at least one connected face set.  
> A connected face set may exist independently of a surface model.  
  
> NOTE  Entity adapted from **face_based_surface_model** defined in ISO
> 10303-42.  
  
> HISTORY  New entity in IFC2x.  
  
{ .spec-head}  
Informal Propositions:  
  
1\. The connected face sets shall not overlap or intersect except at common
faces, edges or vertices.  
2\. The fbsm faces have dimensionality 2.  
  
{ .deprecated}  
> IFC4 CHANGE  The entity has been deprecated and shall not be used. The
> entity _IfcFacetedBrep_ shall be used instead.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricmodelresource/lexical/ifcfacebasedsurfacemodel.htm)


