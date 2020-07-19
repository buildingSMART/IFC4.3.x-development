IfcSurfaceStyleRefraction
=========================
_IfcSurfaceStyleRefraction_ extends the surface style lighting, or the surface
style rendering definition for properties for calculation of physically exact
illuminance by adding seldomly used properties. Currently this includes the
refraction index (by which the light ray refracts when passing through a
prism) and the dispersion factor (or Abbe constant) which takes into account
the wavelength dependency of the refraction.  
  
> NOTE  If such refraction properties are used, the _IfcSurfaceStyle_ should
> include within its set of _Styles_ (depending on whether rendering or
> lighting is used) an instance of _IfcSurfaceStyleLighting_ and
> _IfcSurfaceStyleRefraction_, or an instance of _IfcSurfaceStyleRendering_
> and _IfcSurfaceStyleRefraction_.  
  
> HISTORY  New entity in IFC2x2.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpresentationappearanceresource/lexical/ifcsurfacestylerefraction.htm)


