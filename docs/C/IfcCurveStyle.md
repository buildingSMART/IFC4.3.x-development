IfcCurveStyle
=============
An _IfcCurveStyle_ provides the style table for presentation information
assigned to geometric curves. The style is defined by a color, a font and a
width. The _IfcCurveStyle_ defines curve patterns as model patterns, that is,
the distance between visible and invisible segments of curve patterns are
given in model space dimensions (that have to be scaled using the target plot
scale).  
  
Styles are intended to be shared by multiple _IfcStyledItem_''s, assigning the
style to occurrences of (subtypes of) _IfcGeometricRepresentationItem_''s.
Measures given to a font pattern or a curve width are given in global drawing
length units.  
  
> NOTE  global units are defined at the single _IfcProject_ instance, given by
> _UnitsInContext:IfcUnitAssignment_, the same units are used for the
> geometric representation items and for the style definitions.  
  
The measure values for font pattern and curve width apply to the model space
with a target plot scale provided for the correct appearance in the default
plot scale.. For different scale and projection dependent curve styles a
different instance of _IfcCurveStyle_ needs to be used by
_IfcPresentationStyleAssignment_ for different
_IfcGeometricRepresentationSubContext_ dependent representations.  
  
> NOTE  the target plot scale is given by
> _IfcGeometricRepresentationSubContext.TargetScale_.  
  
An _IfcCurveStyle_ can be assigned to _IfcGeometricRepresentationItem_''s via
the _IfcPresentationStyleAssignment_ through an intermediate _IfcStyledItem_
or _IfcAnnotationCurveOccurrence_.  
  
{ .extDef}  
> NOTE  Definition according to ISO/CD 10303-46:1992  
> A curve style specifies the visual appearance of curves.  
  
> NOTE  Corresponding ISO 10303 name: curve_style. Please refer to ISO/IS
> 10303-46:1994 for the final definition of the formal standard.  
  
> HISTORY  New entity in IFC2x2.  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcpresentationappearanceresource/lexical/ifccurvestyle.htm)


