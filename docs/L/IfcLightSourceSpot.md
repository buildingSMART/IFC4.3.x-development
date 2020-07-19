IfcLightSourceSpot
==================
{ .extDef}  
> NOTE  Definition according to ISO 10303-46:  
> The light source spot entity is a subtype of light source. Spot light source
> entities have a light source colour, position, direction, attenuation
> coefficients, concentration exponent, and spread angle. If a point lies
> outside the cone of influence of a light source of this type as determined
> by the light source position, direction and spread angle its colour is not
> affected by that light source.  
  
> NOTE  The _IfcLightSourceSpot_ adds the _BeamWidthAngle_ which defines the
> inner cone in which the light source emits light at uniform full intensity.
> The light source''s emission intensity drops off from the inner solid angle
> (_BeamWidthAngle_) to the outer solid angle (_SpreadAngle_).  
  
{ .extDef}  
> NOTE  Definition according to ISO/IEC 14772-1:1997:  
> The Spot light node defines a light source that emits light from a specific
> point along a specific direction vector and constrained within a solid
> angle. Spot lights may illuminate geometry nodes that respond to light
> sources and intersect the solid angle defined by the Spot light. Spot light
> nodes are specified in the local coordinate system and are affected by
> ancestors'' transformations. Figure 1 shows the definition of spot light.
> !["spot light"](../figures/ifclightsourcespot_fig1.gif "Figure 1 -- Light
> source spot")  
  
> NOTE  Corresponding ISO 10303 entity: light_source_spot. Please refer to
> ISO/IS 10303-46:1994, p. 33 for the final definition of the formal standard.  
  
> NOTE  In addition to the attributes as defined in ISO10303-46 the additional
> property from ISO/IEC 14772-1:1997 (VRML) _Radius_, _BeamWidth_, and
> _QuadricAttenuation_ are added to this subtype and the _AmbientIntensity_
> and _Intensity_ are inherited from the supertype.  
  
> HISTORY  New entity in IFC2x, renamed and enhanced in IFC2x2.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpresentationorganizationresource/lexical/ifclightsourcespot.htm)


