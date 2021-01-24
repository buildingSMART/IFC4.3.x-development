# IfcSegmentedReferenceCurve

A segmented reference curve is constructed from a reference base curve that should in most cases (there can be exceptions) be used for positioning of a list of _IfcReferenceSegment_. The type of the base curve that IfcReferenceSegment references provide the information of the interpolation method between the start point of the segment and its end point defined by the segment length (measured along the segments IfcLinearPacement.PlacmeentMeasuredAlong curve).

Figure 1 shows a cross section of a _IfcSegmentedReferenceCurve_ usage for an alignmnent representation featuring cant

!["segmented reference curve usage"](../../../../../../figures/IfcSegmentedReferenceCurve.JPG "Figure 1 &mdash; use of a segmented reference curve on a cant segment based on a gradient curve")

## Attributes

### BaseCurve


### Segments


### EndPoint

