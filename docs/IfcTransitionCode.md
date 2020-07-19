IfcTransitionCode
=================
The _IfcTransitionCode_ indicated the continuity between consecutive segments
of a curve or surface.  
  
> EXAMPLE  In ContSameGradient the tangent vectors of successive segments will
> have the same direction, but may have different magnitude.  
  
Figure 1 illustrates transition types  
  
> NOTE  The figure is quoted from ISO 10303-42.  
  
!["transition code"](figures/ifctransitioncode.gif "Figure 1 -- Transition
code")  
  
{ .extDef}  
> NOTE  Definition according to ISO/CD 10303-42:1992  
> This type conveys the continuity properties of a composite curve or surface.
> The continuity referred to is geometric, not parametric continuity.  
  
> NOTE  Type adapted from **transition_code** defined in ISO 10303-42.  
  
> HISTORY  New Type in IFC1.0  
[ _bSI
Documentation_](https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometryresource/lexical/ifctransitioncode.htm)


Attributes
----------
| Attribute                     | Definition   |
|-------------------------------|--------------|
| CONTINUOUS                    |              |
| CONTSAMEGRADIENT              |              |
| CONTSAMEGRADIENTSAMECURVATURE |              |
| DISCONTINUOUS                 |              |
