# IfcTextureCoordinateGenerator

The _IfcTextureCoordinateGenerator_ describes a procedurally defined mapping function with input parameter to map 2D texture coordinates to 3D geometry vertices. The allowable _Mode_ values and input _Parameter_ need to be agreed upon in view definitions and implementer agreements.

> NOTE  It is recommended to use the texture coordinate generation modes as defined in X3D.

{ .extDef}
> NOTE  Definition according to ISO/IEC 19775-1:  
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

> NOTE  The definitions of texturing within this standard have been developed in dependence on the texture component of X3D. See ISO/IEC 19775-1.2:2008 X3D Architecture and base components Edition 2, Part 1, 18 Texturing component for the definitions in the international standard.

> HISTORY  New entity in IFC2x2.

{ .change-ifc2x2}
> IFC2x2 Add2 CHANGE  The attribute Texture has been deleted.

## Attributes

### Mode
The _Mode_ attribute describes the algorithm used to compute texture coordinates.
> NOTE  The applicable values for the _Mode_ attribute are determined by view definitions or implementer agreements. It is recommended to use the modes described in ISO/IES 19775-1.2:2008 X3D Architecture and base components Edition 2, Part 1. See [18.4.8 TextureCoordinateGenerator](http://www.web3d.org/x3d/specifications/ISO-IEC-19775-1.2-X3D-AbstractSpecification/Part01/components/texturing.html#TextureCoordinateGenerator) for recommended values.

### Parameter
The parameters used as arguments by the function as specified by _Mode_.
{ .change-ifc2x4}
> IFC4 CHANGE&nbsp: Data type restricted to REAL.
