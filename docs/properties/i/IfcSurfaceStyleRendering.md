IfcSurfaceStyleRendering
========================

_IfcSurfaceStyleRendering_ holds the properties for visualization related to a particular surface side style. It allows rendering properties to be defined by:

* a colour component (_SurfaceColour_ attribute inherited from _IfcSurfaceStyleShading_)
* a transparency component (_Transparency_ attribute inherited from _IfcSurfaceStyleShading_)
* a reflectance component, given either by 
    * applying reflectance factors to the surface colour: 
        * diffuse component (_SurfaceColour \* DiffuseFactor_)
        * transmission component (_SurfaceColour \* TransmissionFactor_)
        * diffuse transmission component (_SurfaceColour \* DiffuseTransmissionFactor_)
        * reflection component (_SurfaceColour \* ReflectionFactor_)
        * specular component (_SurfaceColour \* SpecularFactor_ attribute together with _SpecularHighlight_) 
    * or, by explicitly defining such factors as colours (_DiffuseColour_, _TransmissionColour_, _DiffuseTransmissionColour_, _ReflectionColour_ and _SpecularColour_) 
* a displacement component, currently only given by a texture map with the TextureType = bump
* a coverage component, currently only given by the alpha component of the texture map (2 or 4 component colour texture)

> NOTE&nbsp; The inherited attribute _SurfaceColour_ is treated as the ambient colour and specifies how much ambient light from light sources this surface shall reflect. Ambient light is omnidirectional and depends only on the number of light sources, not their positions with respect to the surface.

> NOTE&nbsp; If the reflectance method, as given by the _IfcReflectanceMethodEnum_ is "GLASS", the transmission factor controls the level of transparency in the glass, In this case the transparency factor is interpreted as transmission factor.

> NOTE&nbsp; If both _Transparency_ and _TransmissionColour_ (or factor) are included, the following definitions apply: > * Transparency is the ratio of the transmitted flux in a solid angle of 2 \* PI sr (one hemisphere). It is a simple colour filtration that does not account for refraction.
> * Transmission factor of a material is the ratio of transmitted flux in a given solid angle to the transmitted flux of a completely diffuse material with 100% transmission in the same solid angle. It is the portion of light that goes through the material and may be refracted.

> NOTE&nbsp; For reflectance equations and further information about the surface style properties and its processing, see: > * ISO/IEC 14772-1: 1997: The Virtual Reality Modeling Language

> HISTORY&nbsp; New entity in IFC2x.
