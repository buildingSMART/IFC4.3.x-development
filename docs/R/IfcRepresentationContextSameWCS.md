IfcRepresentationContextSameWCS
===============================
If there are several instances of _IfcGeometricRepresentationContext_ within
one project file, the XY plane of all _WorldCoordinateSystem_''s shall be
coplanar and identical.  
  
> NOTE\S\ The instances of  
 _IfcGeometricRepresentationSubContext_ do not define their  
own world coordinate system, they refer to the world coordinate  
system of the _ParentContext_.  
  
> HISTORY\S\ New global rule  
in Release IFC2x  


