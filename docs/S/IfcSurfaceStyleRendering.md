IfcSurfaceStyleRendering
========================
_IfcSurfaceStyleRendering_ holds the properties for visualization related to a
particular surface side style. It allows rendering properties to be defined
by:  
  
* a colour component (_SurfaceColour_ attribute inherited from _IfcSurfaceStyleShading_)  
* a transparency component (_Transparency_ attribute inherited from _IfcSurfaceStyleShading_)  
* a reflectance component, given either by   
* applying reflectance factors to the surface colour:   
* diffuse component (_SurfaceColour \\\\* DiffuseFactor_)  
* transmission component (_SurfaceColour \\\\* TransmissionFactor_)  
* diffuse transmission component (_SurfaceColour \\\\* DiffuseTransmissionFactor_)  
* reflection component (_SurfaceColour \\\\* ReflectionFactor_)  
* specular component (_SurfaceColour \\\\* SpecularFactor_ attribute together with _SpecularHighlight_)   
* or, by explicitly defining such factors as colours (_DiffuseColour_, _TransmissionColour_, _DiffuseTransmissionColour_, _ReflectionColour_ and _SpecularColour_)   
* a displacement component, currently only given by a texture map with the TextureType = bump  
* a coverage component, currently only given by the alpha component of the texture map (2 or 4 component colour texture)  
  
> NOTE  The inherited attribute _SurfaceColour_ is treated as the ambient
> colour and specifies how much ambient light from light sources this surface
> shall reflect. Ambient light is omnidirectional and depends only on the
> number of light sources, not their positions with respect to the surface.  
  
> NOTE  If the reflectance method, as given by the _IfcReflectanceMethodEnum_
> is "GLASS", the transmission factor controls the level of transparency in
> the glass, In this case the transparency factor is interpreted as
> transmission factor.  
  
> NOTE  If both _Transparency_ and _TransmissionColour_ (or factor) are
> included, the following definitions apply: > * Transparency is the ratio of
> the transmitted flux in a solid angle of 2 \\\\* PI sr (one hemisphere). It
> is a simple colour filtration that does not account for refraction.  
> * Transmission factor of a material is the ratio of transmitted flux in a
> given solid angle to the transmitted flux of a completely diffuse material
> with 100% transmission in the same solid angle. It is the portion of light
> that goes through the material and may be refracted.  
  
> NOTE  For reflectance equations and further information about the surface
> style properties and its processing, see: > * ISO/IEC 14772-1: 1997: The
> Virtual Reality Modeling Language  
  
> HISTORY  New entity in IFC2x.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpresentationappearanceresource/lexical/ifcsurfacestylerendering.htm)


Attribute definitions
---------------------
| Attribute                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DiffuseColour             | The diffuse part of the reflectance equation can be given as either a colour or a scalar factor.\X\0DThe diffuse colour field reflects all light sources depending on the angle of the surface with respect to the light source. The more directly the surface faces the light, the more diffuse light reflects.\X\0DThe diffuse factor field specifies how much diffuse light from light sources this surface shall reflect. Diffuse light depends on the angle of the surface with respect to the light source. The more directly the surface faces the light, the more diffuse light reflects. The diffuse colour is then defined by surface colour \\\\* diffuse factor. |
| TransmissionColour        | The transmissive part of the reflectance equation can be given as either a colour or a scalar factor. It only applies to materials which Transparency field is greater than zero.\X\0DThe transmissive colour field specifies the colour that passes through a transparant material (like the colour that shines through a glass).\X\0DThe transmissive factor defines the transmissive part, the transmissive colour is then defined by surface colour \\\\* transmissive factor.                                                                                                                                                                                           |
| DiffuseTransmissionColour | The diffuse transmission part of the reflectance equation can be given as either a colour or a scalar factor. It only applies to materials whose Transparency field is greater than zero.\X\0DThe diffuse transmission colour specifies how much diffuse light is reflected at the opposite side of the material surface.\X\0DThe diffuse transmission factor field specifies how much diffuse light from light sources this surface shall reflect on the opposite side of the material surface. The diffuse transmissive colour is then defined by surface colour \\\\* diffuse transmissive factor.                                                                        |
| ReflectionColour          | The reflection (or mirror) part of the reflectance equation can be given as either a colour or a scalar factor. Applies to "glass" and "mirror" reflection models.\X\0DThe reflection colour specifies the contribution made by light from the mirror direction, i.e. light being reflected from the surface.\X\0DThe reflection factor specifies the amount of contribution made by light from the mirror direction. The reflection colour is then defined by surface colour \\\\* reflection factor.                                                                                                                                                                       |
| SpecularColour            | The specular part of the reflectance equation can be given as either a colour or a scalar factor.\X\0DThe specular colour determine the specular highlights (e.g., the shiny spots on an apple). When the angle from the light to the surface is close to the angle from the surface to the viewer, the specular colour is added to the diffuse and ambient colour calculations.\X\0DThe specular factor defines the specular part, the specular colour is then defined by surface colour \\\\* specular factor.                                                                                                                                                             |
| SpecularHighlight         | The exponent or roughness part of the specular reflectance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ReflectanceMethod         | Identifies the predefined types of reflectance method from which the method required may be set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

