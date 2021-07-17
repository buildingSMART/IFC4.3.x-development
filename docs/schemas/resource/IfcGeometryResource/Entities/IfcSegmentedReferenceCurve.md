# IfcSegmentedReferenceCurve

A segmented reference curve is constructed from a referenced base curve (_BaseCurve_) that should in most cases (there can be exceptions) be used for positioning of a list of _IfcCurveSegment_ occurrences. The type of the base curve that _IfcCurveSegment_ references provides the information of the interpolation method between the start point of the segment and its end point defined by the segment length of the _IfcCurveSegment_._ParentCurve_.

The parametrization of _IfcSegmentReferenceCurve_ is based on the parametrization of _BaseCurve_ and is not altered by the _Segments_.

Figure 1 shows a cross section of a _IfcSegmentedReferenceCurve_ usage for an alignmnent representation featuring cant

!["segmented reference curve usage"](../../../../figures/IfcSegmentedReferenceCurve.JPG "Figure 1 &mdash; use of a segmented reference curve on a cant segment based on a gradient curve")

## Attributes

### BaseCurve


### EndPoint

