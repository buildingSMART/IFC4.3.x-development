IfcTextureCoordinateGenerator
=============================

The _IfcTextureCoordinateGenerator_ describes a procedurally defined mapping function with input parameter to map 2D texture coordinates to 3D geometry vertices. The allowable _Mode_ values and input _Parameter_ need to be agreed upon in view definitions and implementer agreements.

> NOTE&nbsp; It is recommended to use the texture coordinate generation modes as defined in X3D.

{ .extDef}
> NOTE&nbsp; Definition according to ISO/IEC 19775-1:  
>   
> The TextureCoordinateGenerator supports the automatic generation of texture coordinates for geometric shapes.  
> The mode field describes the algorithm used to compute texture coordinates. { .std}
> * SPHERE, 
> * CAMERASPACENORMAL, 
> * CAMERASPACEPOSITION, 
> * CAMERASPACEREFLECTIONVECTOR, 
> * SPHERE-LOCAL, 
> * COORD, 
> * COORD-EYE, 
> * NOISE, 
> * NOISE-EYE, 
> * SPHERE-REFLECT, 
> * SPHERE-REFLECT-LOCAL

> NOTE&nbsp; The definitions of texturing within this standard have been developed in dependence on the texture component of X3D. See ISO/IEC 19775-1.2:2008 X3D Architecture and base components Edition 2, Part 1, 18 Texturing component for the definitions in the international standard.

> HISTORY&nbsp; New entity in IFC2x2.

{ .change-ifc2x2}
> IFC2x2 Add2 CHANGE&nbsp; The attribute Texture has been deleted.
