IfcReparametrisedCompositeCurveSegment
======================================

The _IfcReparametrisedCompositeCurveSegment_ is geometrically identical to a _IfcCompositeCurveSegment_ but with the additional capability of reparametrization.

{ .extDef}
> NOTE&nbsp; Definition according to ISO/CD 10303-42:1992  
> The reparametrised composite curve segment is a special type of composite curve segment which provides the capability to re-define its parametric length without changing its geometry.   
>   
> If t~<small>0</small>~ &le; t &le; t~<small>1</small>~ is the parameter range of _ParentCurve_, the new parameter . for the reparametrised composite curve segment is given by the equation: 
{ .extDef}
>> ![Image](../../../../../../figures/ifcreparametrisedcompositecurvesegment-math1.gif) if _SameSense_ = TRUE;
>  or by the equation: 
{ .extDef}
>> ![Image](../../../../../../figures/ifcreparametrisedcompositecurvesegment-math2.gif) if _SameSense_ = FALSE;


> 
> NOTE&nbsp; Entity adapted from **reparametrised_composite_curve_segment** in ISO 10303-42.

> HISTORY&nbsp; New entity in IFC4
