# IfcSurfaceStyleRefraction

_IfcSurfaceStyleRefraction_ extends the surface style lighting, or the surface style rendering definition for properties for calculation of physically exact illuminance by adding seldom used properties. Currently this includes the refraction index (by which the light ray refracts when passing through a prism) and the dispersion factor (or Abbe constant) which takes into account the wavelength dependency of the refraction.
<!-- end of short definition -->


> NOTE If such refraction properties are used, the _IfcSurfaceStyle_ should include within its set of _Styles_ (depending on whether rendering or lighting is used) an instance of _IfcSurfaceStyleLighting_ and _IfcSurfaceStyleRefraction_, or an instance of _IfcSurfaceStyleRendering_ and _IfcSurfaceStyleRefraction_.

> HISTORY New entity in IFC2x2.

## Attributes

### RefractionIndex
The index of refraction for all wave lengths of light. The refraction index is the ratio between the speed of light in a vacuum and the speed of light in the medium. E.g. glass has a refraction index of 1.5, whereas water has an index of 1.33

### DispersionFactor
The Abbe constant given as a fixed ratio between the refractive indices of the material at different wavelengths. A low Abbe number means a high dispersive power. In general this translates to a greater angular spread of the emergent spectrum.
