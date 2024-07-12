# IfcSurfaceStyleRendering

IfcSurfaceStyleRendering holds the properties for visualization related to a particular surface style. Three lighting models are supported:
<!-- end of short definition -->

- Phong lighting model
- Physically based lighting model
- Flat lighting model that ignores light sources

The material parameters are specified as scalars or RGB colors. Every material parameter can be adjusted using a texture. This allows to vary this parameter across the surface. The information sampled from the texture is always multiplied by the simple scalar/color fields.

> NOTE Refer to the ISO/IEC 19775-1 X3D [17 Lighting component](https://www.web3d.org/specifications/X3Dv4Draft/ISO-IEC19775-1v4-CD/Part01/components/lighting.html) section for a detailed description of the lighting model equations.

> HISTORY New entity in IFC2x.

## Attributes

### DiffuseColour
In a PHONG ReflectanceMethod, the DiffuseColour correlates to the diffuseColor attribute in the X3D Phong lighting model. The diffuse colour reflects all X3D light sources depending on the angle of the surface with respect to the light source. The more directly the surface faces the light, the more diffuse light reflects. In a PHYSICAL ReflectanceMethod, a physical based lighting model is assumed, and so the DiffuseColour correlates to the baseColor attribute used in the X3D physical lighting model. In a FLAT ReflectanceMethod, the DiffuseColour correlates to the emissiveColor attribute used in the X3D unlit lighting model.

> IFC4.3.0.0 CHANGE Attribute has been repurposed to fit the X3D reflectance methods.

### TransmissionColour
The transmissive part of the reflectance equation can be given as either a colour or a scalar factor. It only applies to materials which Transparency field is greater than zero.
The transmissive colour field specifies the colour that passes through a transparent material (like the colour that shines through a glass).
The transmissive factor defines the transmissive part, the transmissive colour is then defined by surface colour \* transmissive factor.

> IFC4.3.0.0 DEPRECATION This attribute is deprecated and shall no longer be used.

### DiffuseTransmissionColour
The diffuse transmission part of the reflectance equation can be given as either a colour or a scalar factor. It only applies to materials whose Transparency field is greater than zero.
The diffuse transmission colour specifies how much diffuse light is reflected at the opposite side of the material surface.
The diffuse transmission factor field specifies how much diffuse light from light sources this surface shall reflect on the opposite side of the material surface. The diffuse transmissive colour is then defined by surface colour \* diffuse transmissive factor.

> IFC4.3.0.0 DEPRECATION This attribute is deprecated and shall no longer be used.

### ReflectionColour
The reflection (or mirror) part of the reflectance equation can be given as either a colour or a scalar factor. Applies to "glass" and "mirror" reflection models.
The reflection colour specifies the contribution made by light from the mirror direction, i.e. light being reflected from the surface.
The reflection factor specifies the amount of contribution made by light from the mirror direction. The reflection colour is then defined by surface colour \* reflection factor.

> IFC4.3.0.0 DEPRECATION This attribute is deprecated and shall no longer be used.

### SpecularColour
In a PHONG ReflectanceMethod, the SpecularColour correlates to the specularColor attribute in the X3D Phong lighting model. The specular colour determine the colour of the specular highlights ( e.g., the shiny spots on an apple). In a PHYSICAL ReflectanceMethod, a physical based lighting model is assumed, and so the SpecularColour is specified as a IfcNormalisedRatioMeasure, which correlates to the metallic attribute used in the X3D physical lighting model. In a FLAT ReflectanceMethod, the SpecularColour has no effect.

> IFC4.3.0.0 CHANGE Attribute has been repurposed to fit the X3D reflectance methods.

### SpecularHighlight
In a PHONG ReflectanceMethod, the SpecularHighlight is specified as a IfcSpecularRoughness and correlates to the inverse of the shininess attribute in the X3D Phong lighting model. The SpecularHighlight determines the nature of the specular highlights ( e.g., the shiny spots on an apple). Lower shininess values produce soft glows, while higher values result in sharper, smaller highlights. In a PHYSICAL ReflectanceMethod, a physical based lighting model is assumed, and so the SpecularHighlight is specified as a IfcSpecularRoughness, which correlates to the roughness attribute used in the X3D physical lighting model. In a FLAT ReflectanceMethod, the SpecularHighlight has no effect.

> IFC4.3.0.0 CHANGE Attribute has been repurposed to fit the X3D reflectance methods.

### ReflectanceMethod
Identifies the predefined types of reflectance method from which the method required may be set. PHONG correlates to the X3D Phong lighting model. PHYSICAL correlates to the X3D Physical lighting model. FLAT correlates to the X3D Unlit lighting model. The exact behaviour of other reflectance methods may be determined by view definitions or implementer agreements.

> IFC4.3.0.0 CHANGE Attribute has been repurposed to fit the X3D reflectance methods.
